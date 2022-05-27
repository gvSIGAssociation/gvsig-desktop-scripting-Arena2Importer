# encoding: utf-8

import gvsig
import threading

from gvsig import logger, LOGGER_WARN
import sys

from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel
from org.gvsig.tools.dispose import DisposeUtils
from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.dynobject import DynObjectValueItem
from org.gvsig.fmap.geom import GeometryUtils, Geometry
from org.gvsig.fmap.dal import DALLocator

from javax.swing import AbstractCellEditor, Timer
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

class ShowLabelCellRenderer(DefaultTableCellRenderer):
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
    self.__eventsEnableds = True
    self.__lastSize = None
    self.__lastFeature = None
    self.__lastFeatureIndex = None
    self.__updateUI = True

  def setEnableUpdateUI(self, enable):
    self.__updateUI = enable
    self.fireTableDataChanged()    
    
  def setEnabledEvents(self, enable):
    self.__eventsEnableds = enable
    
  def __fireDelayedsEvents(self, *args):
    if not self.__eventsEnableds:
      return
    if self.__issues_list != None:
      self.__issues_list.getFeaturePagingHelper().dispose()
    self.__issues_list = None
    self.fireTableDataChanged()

  def __delayfireTableDataChanged(self):
    if not self.__eventsEnableds:
      return
    if self.__timer!=None:
      self.__timer.restart()
      return
    self.__timer = Timer(4000,self.__fireDelayedsEvents)
    #self.__timer.setName("ARENA2_REPORT_DELAYEVENTS")
    self.__timer.setRepeats(False)
    self.__timer.start()
  
  def __len__(self):
    return self.getIssuesAsList().size64()
    
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
        col.setCellRenderer(ShowLabelCellRenderer(values))
        if attr.getTags().getBoolean("editable",True):
          col.setCellEditor(DropDownCellEditor(values, readOnly=False))
        else:
          col.setCellEditor(DropDownCellEditor(values, readOnly=True))
          
  def getStore(self):
    return self.__issues

  def removeAll(self):
    self.__issues = self.createH2Store()
    self.__lastSize = None
    self.__lastFeature = None
    self.__lastFeatureIndex = None
    self.__delayfireTableDataChanged()
  
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
    eft.add("DESCRIPTION", "STRING", 1000).setLabel("Descripcion").getTags().set("editable",False)
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
    
    serverExplorer.add("H2Spatial",storeparams,False)
    store = dataManager.openStore("H2Spatial", serverExplorer.get("issues"))
    self.__ftype = store.getDefaultFeatureType()
    self.__issues_list = None
    serverExplorer.dispose()
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
    eft.add("DESCRIPTION", "STRING", 1000).setLabel("Descripcion").getTags().set("editable",False)
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
    if self.__lastSize != None:
      self.__lastSize += 1
    self.__delayfireTableDataChanged()
    return issue

  def updateIssue(self, issue):
    if issue == None:
      return
    self.__issues.edit()
    self.__issues.update(issue)
    self.__issues.finishEditing()

    if self.__lastFeature != None and not(self.__lastFeature.getReference().equals(issue.getReference())):
      self.__lastFeature = issue
    self.__delayfireTableDataChanged()
    return issue

  def addIssues(self, issues_fset):
    self.__issues.edit()
    self.__issues.insert(issues_fset)
    self.__issues.finishEditing()
    if self.__lastSize != None:
      self.__lastSize += issues_fset.size64()
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
    
  def hasToProcessIssue(self, basestring):
      issue = self.__issues.findFirst("ID_ACCIDENTE = '%s'") # Si no hay accidente con incidencia se importa
      if issue==None:
        return True;
      issue = self.__issues.findFirst("ID_ACCIDENTE = '%s' AND SELECTED=False" % basestring)
      return issue==None # Si no se encuentra desactivado en ninguno de sus reportes, hay que importarlo

  def putIssue(self, row, issue):
    trace("put(%s,%s)" % (row, issue))
    self.__issues.edit()
    self.__issues.update(issue)
    self.__issues.finishEditing()
    if self.__lastFeature != None and not(self.__lastFeature.getReference().equals(issue.getReference())):
      self.__lastFeature = issue

  def refresh(self):
    self.__delayfireTableDataChanged()

  def fixIssueFeature(self, issue, editableFeature):
    fixerID=issue.get("FIXERID")
    if fixerID==None:
      return
    trace("fix(%s) fixerID %r" % (editableFeature.get("ID_ACCIDENTE"), fixerID))
    fixer = self.__importManager.getFixer(fixerID)
    if fixer==None:
      return
    fixer.fix(editableFeature, issue)
    
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
        self.fixIssueFeature(issue, feature)
    finally:
      issues.dispose()
      
  def getAccidenteId(self, row):
    issue = self.getIssue(row)
    return issue.get("ID_ACCIDENTE")
    
  def setSelectedAll(self, value):
    self.__issues.edit()
    fset = self.__issues.getFeatureSet()
    itera = fset.iterable()
    for issue in itera:
      editable = issue.getEditable()
      editable.set("SELECTED", value)
      fset.update(editable)
    self.__issues.finishEditing()
      
  def setSelected(self, row, value):
    trace("setSelected(row=%s,value=%s)" % (row, value))
    issue = self.getIssue(row)
    if issue == None:
      return
    issue = issue.getEditable()
    issue.set("SELECTED",value)
    self.putIssue(row, issue)
    self.__delayfireTableDataChanged()
  
  def isSelected(self, accidentId):
    #trace("isSelected(%r)" % accidentId)
    issue = self.__issues.findFirst("ID_ACCIDENTE = '%s'" % accidentId)
    if issue == None:
      return False
    if issue.get("SELECTED") :
      return True
    return False
     
  def getTableModel(self):
    return self

  def getRowCount(self):
    if not self.__updateUI:
      return 0
    if self.__lastSize != None and self.__lastSize > 0:
      return self.__lastSize
    try:
      self.__lastSize = self.getIssuesAsList().size64()
      return self.__lastSize
    except:
      self.__issues_list = None
      try:
        self.__lastSize = self.getIssuesAsList().size64()
        return self.__lastSize
      except:
        return 0
    
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

  def getValueAt0(self, rowIndex, columnIndex):
    issue = self.getIssue(rowIndex)
    if issue == None:
      return None
    attr = self.getAttributeByColumnIndex(columnIndex)
    self.__lastFeature = issue
    self.__lastFeatureIndex = rowIndex
    return issue.get(attr.getName())
  
  def getValueAt(self, rowIndex, columnIndex):
    if not self.__updateUI:
      return None
    try:
      if rowIndex == self.__lastFeatureIndex and self.__lastFeature != None:
        try:
          attr = self.getAttributeByColumnIndex(columnIndex)
          return self.__lastFeature.get(attr.getName())
        except:
          ex = sys.exc_info()[1]
          logger("Error transformando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
          return None
      return self.getValueAt0(rowIndex, columnIndex)
    except:
      ex = sys.exc_info()[1]
      self.__issues_list = None
      try:
        return self.getValueAt0(rowIndex, columnIndex)
      except:
        return None

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

def hola(*args):
  print "hola"
  
def main(*args):
  timer = Timer(5000,hola)
  timer.setRepeats(False)
  timer.start()
  
  