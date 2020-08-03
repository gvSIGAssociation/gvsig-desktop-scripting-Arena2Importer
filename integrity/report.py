# encoding: utf-8

import gvsig
import threading

from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.dynobject import DynObjectValueItem
from org.gvsig.fmap.geom import GeometryUtils, Geometry
from org.gvsig.fmap.dal import DALLocator

from javax.swing import AbstractCellEditor
from javax.swing import DefaultComboBoxModel
from javax.swing import JLabel, JComboBox
from javax.swing.table import TableCellEditor, DefaultTableCellRenderer
from org.gvsig.tools.swing.api import ToolsSwingLocator

def trace(msg):
  #print "REPORT:", msg
  pass

class DropDownCellEditor(AbstractCellEditor,TableCellEditor):
  def __init__(self, availableValues, readOnly=False):
    self.__component = ToolsSwingLocator.getToolsSwingManager().createDropDown(JLabel())
    self.__component.setReadOnly(readOnly)
    self.__availableValues = availableValues
    self.__dropDownModel = DefaultComboBoxModel()
    self.__lastValue = None
    for v in availableValues:
      self.__dropDownModel.addElement(v)
    self.__component.setModel(self.__dropDownModel)

  def getTableCellEditorComponent(self, table, value, isSelected, rowIndex, vColIndex):
    self.__lastValue = value
    for n in xrange(len(self.__availableValues)):
      if value == self.__availableValues[n].getValue():
        self.__component.setSelectedIndex(n)
        break
    return self.__component.asJComponent()

  def getCellEditorValue(self):
    if self.__component.isReadOnly():
      return self.__lastValue
    n = self.__component.getSelectedItem()
    if n == None :
      return
    return n.getValue()

class ShowLabelCellEditor(DefaultTableCellRenderer):
  def __init__(self, availableValues):
    DefaultTableCellRenderer.__init__(self)
    self.__availableValues = availableValues

  def getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, column):
    x = DefaultTableCellRenderer.getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, column)
    for availableValue in self.__availableValues:
      if value == availableValue.getValue():
        x.setText(availableValue.getLabel())
        break
    return x

class Report(AbstractTableModel):

  def __init__(self, importManager):
    self.__dataManager = DALLocator.getDataManager()
    self.__importManager = importManager
    self.__ftype = None
    self.__columnNames = list()
    self.__issues_list = None    
    #self.__issues = self.createMemoryStore()
    self.__issues = self.createH2Store()
    for attr in self.__ftype:
      if not attr.isHidden():
        self.__columnNames.append(attr.getName())
    self.__timer = None
    self.__delayed_events = 0
    self.__eventsEnableds = True

  def setEnabledEvents(self, enable):
    self.__eventsEnableds = enable
    
  def __fireDelayedsEvents(self):
    if not self.__eventsEnableds:
      return
    self.__delayed_events = 0
    self.__issues_list = None
    self.fireTableDataChanged()

  def __delayfireTableDataChanged(self):
    if not self.__eventsEnableds:
      return
    if self.__timer!=None:
      self.__timer.cancel()
      self.__timer = None
    self.__delayed_events += 1
    if self.__delayed_events > 100:
      self.__fireDelayedsEvents()
    else:
      self.__timer = threading.Timer(4,self.__fireDelayedsEvents)
      self.__timer.setName("ARENA2_REPORT_DELAYEVENTS")
      self.__timer.start()
  
  def __len__(self):
    return len(self.getIssuesAsList())
    
  def getAttributeByColumnIndex(self, columnIndex):
    name = self.__columnNames[columnIndex]
    attr = self.__ftype.get(name)
    return attr

  def setCellEditors(self, jtable):
    trace("setCellEditors")
    columnModel = jtable.getColumnModel()
    for columnIndex in range(len(self.__columnNames)):
      name = self.__columnNames[columnIndex]
      attr = self.__ftype.get(name)
      trace("Report.setCellEditors() %r: %r" % (attr.getName(), attr.getAvailableValues()))
      values = attr.getAvailableValues()
      if values != None:
        col = columnModel.getColumn(columnIndex)
        col.setCellRenderer(ShowLabelCellEditor(values))
        if attr.getTags().getBoolean("editable",True):
          col.setCellEditor(DropDownCellEditor(values, readOnly=False))
        else:
          col.setCellEditor(DropDownCellEditor(values, readOnly=True))
          
  def getStore(self):
    return self.__issues

  def removeAll(self):
    self.__issues = self.createMemoryStore()
    self.fireTableDataChanged()
  
  def createH2Store(self):
    foldersManager = ToolsLocator.getFoldersManager()
    f = foldersManager.getUniqueTemporaryFile("arena2_import.db").getAbsolutePath()
    pathnamedb = f[:-3]
    dataManager = DALLocator.getDataManager()
    serverParameters = dataManager.createServerExplorerParameters("H2Spatial")
    serverParameters.setDynValue("database_file",pathnamedb)
    serverExplorer = dataManager.openServerExplorer("H2Spatial",serverParameters)
    storeparams = serverExplorer.getAddParameters()
    storeparams.setTable("issues")
    eft = storeparams.getDefaultFeatureType()
    eft.setLabel("Incidencias importacion ARENA2")
    eft.setHasOID(False)
    eft.add("ID", 'STRING', 40).setHidden(True).setIsPrimaryKey(True)
    eft.add("SELECTED", "BOOLEAN").setLabel("Importar").getTags().set("editable",True)
    eft.add("ID_ACCIDENTE", "STRING", 20).setLabel("Cod.accidente").getTags().set("editable",False)
    eft.get("ID_ACCIDENTE").setIsIndexed(True)
    eft.get("ID_ACCIDENTE").setAllowIndexDuplicateds(True)
    eft.add("ERRCODE", "INTEGER").setAvailableValues(self.__buildAvailableValues()).setLabel("Cod.error").getTags().set("editable",False)
    eft.add("FIXERID", "STRING", 45).setHidden(True).setLabel("FixerID").getTags().set("editable",False)
    for attr in self.__importManager.getReportAttributes():
      if attr.getSize() == None:
        desc = eft.add(attr.getName(), attr.getTypeName())
      else:
        desc = eft.add(attr.getName(), attr.getTypeName(), attr.getSize())
      desc.setAvailableValues(attr.getAvailableValues())
      desc.getTags().set("editable",attr.isEditable())
      desc.setLabel(attr.getLabel())
      #trace("Create ISSUES store: %s, size=%s, label=%r, editable=%s, values=%s" % (attr.getName(), attr.getSize(), attr.getLabel(), attr.isEditable(), attr.getAvailableValues()))
    eft.add("DESCRIPTION", "STRING", 200).setLabel("Descripcion").getTags().set("editable",False)
    serverExplorer.add("H2Spatial",storeparams,False)
    store = dataManager.openStore("H2Spatial", serverExplorer.get("issues"))
    self.__ftype = store.getDefaultFeatureType()
    self.__issues_list = None
    return store
  
  def createMemoryStore(self):    
    trace("Create ISSUES store")
    store = self.__dataManager.openStore("Memory")
    ft = store.getDefaultFeatureType()
    eft = ft.getEditable()
    eft.setLabel("Incidencias importacion ARENA2")
    eft.setHasOID(True)
    eft.add("ID", 'STRING', 40).setHidden(True)
    #eft.get("ID").setIsPrimaryKey(True)
    eft.add("SELECTED", "BOOLEAN").setLabel("Importar").getTags().set("editable",True)
    eft.add("ID_ACCIDENTE", "STRING", 20).setLabel("Cod.accidente").getTags().set("editable",False)
    eft.add("ERRCODE", "INTEGER").setAvailableValues(self.__buildAvailableValues()).setLabel("Cod.error").getTags().set("editable",False)
    eft.add("FIXERID", "STRING", 45).setHidden(True).setLabel("FixerID").getTags().set("editable",False)
    for attr in self.__importManager.getReportAttributes():
      if attr.getSize() == None:
        desc = eft.add(attr.getName(), attr.getTypeName())
      else:
        desc = eft.add(attr.getName(), attr.getTypeName(), attr.getSize())
      desc.setAvailableValues(attr.getAvailableValues())
      desc.getTags().set("editable",attr.isEditable())
      desc.setLabel(attr.getLabel())
      #trace("Create ISSUES store: %s, size=%s, label=%r, editable=%s, values=%s" % (attr.getName(), attr.getSize(), attr.getLabel(), attr.isEditable(), attr.getAvailableValues()))
    eft.add("DESCRIPTION", "STRING", 200).setLabel("Descripcion").getTags().set("editable",False)
    
    store.edit()
    store.update(eft)
    store.finishEditing()  
    self.__ftype = store.getDefaultFeatureType()
    self.__issues_list = None
    return store

  def __buildAvailableValues(self):
    x = self.__importManager.getRuleErrorCodes()
    l = list()
    for code,label in x.iteritems():
      l.append(DynObjectValueItem(code,label))
    return l
    
  def add(self, accidentId, errcode, description, selected=None, fixerId=None, **args):
    trace("add(accidentId=%r,errcode=%r,description=%r)" % (accidentId, errcode, description))
    self.__issues.edit()
    issue = self.__issues.createNewFeature()
    issue.set("ID", self.__dataManager.createUniqueID())
    if selected == None or not selected :
      issue.set("SELECTED",False)
    else:
      issue.set("SELECTED",True)
    issue.set("ID_ACCIDENTE",accidentId)
    issue.set("ERRCODE",errcode)
    issue.set("DESCRIPTION",description)
    issue.set("FIXERID",fixerId)
    for name,value in args.iteritems():
      issue.set(name,value)
    self.__issues.insert(issue)
    self.__issues.finishEditing()
    self.__delayfireTableDataChanged()

  def addIssues(self, issues_fset):
    self.__issues.edit()
    self.__issues.insert(issues_fset)
    self.__issues.finishEditing()
    self.__delayfireTableDataChanged()
    
  def getIssuesAsList(self):
    if self.__issues_list == None:
      self.__issues_list = self.__issues.getFeatures()
    return self.__issues_list
    
  def getIssue(self, index):
    if isinstance(index, basestring):
      issue = self.__issues.findFirst("ID_ACCIDENTE = '%s'" % index)
    else:
      issue = self.getIssuesAsList()[index]
    return issue

  def putIssue(self, row, issue):
    trace("put(%s,%s)" % (row, issue))
    self.__issues.edit()
    self.__issues.update(issue)
    self.__issues.finishEditing()

  def refresh(self):
    self.fireTableDataChanged()

      
  def fix(self, feature):
    accidentId = feature.get("ID_ACCIDENTE")
    issues = self.__issues.getFeatureSet("ID_ACCIDENTE = '%s'" % accidentId)
    if issues == None:
      return True
    try:
      for issue in issues:
        if issue.get("ID_ACCIDENTE") != accidentId:
          continue
        if not issue.get("SELECTED") :
          continue
        fixerID=issue.get("FIXERID")
        if fixerID==None:
          continue
        trace("fix(%s) fixerID %r" % (accidentId, fixerID))
        fixer = self.__importManager.getFixer(fixerID)
        if fixer==None:
          continue
        fixer.fix(feature, issue)
    finally:
      issues.dispose()
      
  def getAccidenteId(self, row):
    issue = self.getIssue(row)
    return issue.get("ID_ACCIDENTE")
    
  def setSelected(self, row, value):
    trace("setSelected(row=%s,value=%s)" % (row, value))
    issue = self.getIssue(row)
    if issue == None:
      return
    issue = issue.getEditable()
    issue.set("SELECTED",value)
    self.putIssue(row, issue)
    self.fireTableDataChanged()
  
  def isSelected(self, accidentId):
    #trace("isSelected(%r)" % accidentId)
    issues = self.__issues.getFeatureSet("ID_ACCIDENTE = '%s'" % accidentId)
    if issues == None:
      return True
    try:
      for issue in issues:
        if issue.get("ID_ACCIDENTE") != accidentId:
          continue
        if issue.get("SELECTED") :
          return True
      return False
    finally:
      issues.dispose()
     
  def getTableModel(self):
    return self

  def getRowCount(self):
    return len(self.getIssuesAsList())

  def getColumnCount(self):
    return len(self.__columnNames)

  def getColumnName(self, columnIndex):
    attr = self.getAttributeByColumnIndex(columnIndex)
    return attr.getLabel()

  def getColumnClass(self, columnIndex):
    attr = self.getAttributeByColumnIndex(columnIndex)
    return attr.getDataType().getDefaultClass()

  def isCellEditable(self, rowIndex, columnIndex):
    attr = self.getAttributeByColumnIndex(columnIndex)
    #trace("isCellEditable(row=%s,column=%s) %s" % (rowIndex, columnIndex, attr.getTags().getBoolean("editable",False)))
    if attr.getTags().getBoolean("editable",False):
      return True
    if attr.getAvailableValues()!=None:
      return True
    return False

  def getValueAt(self, rowIndex, columnIndex):
    issue = self.getIssue(rowIndex)
    if issue == None:
      return None
    attr = self.getAttributeByColumnIndex(columnIndex)
    return issue.get(attr.getName())

  def setValueAt(self, aValue, rowIndex, columnIndex):
    trace("setValueAt(value=%s,row=%s,column=%s)" % (aValue, rowIndex, columnIndex))
    attr = self.getAttributeByColumnIndex(columnIndex)
    if not attr.getTags().getBoolean("editable",False):
      return
    issue = self.getIssue(rowIndex)
    if issue == None:
      return
    issue = issue.getEditable()
    issue.set(attr.getName(),aValue)
    self.putIssue(rowIndex, issue)

def hola():
  print "hola"
  
def main(*args):
  timer = threading.Timer(5,hola)
  timer.setName("Hola")
  timer.start()
  
  