# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from gvsig.commonsdialog import msgbox

from java.awt import Component
from org.gvsig.tools import ToolsLocator
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.tools.swing.api import ToolsSwingLocator
from java.lang import Thread
from java.awt import BorderLayout
from javax.swing import JButton
from org.gvsig.fmap.dal.swing.AbstractDALActionFactory import AbstractDALActionContext
from org.gvsig.tools.observer import Observer
from org.gvsig.expressionevaluator import ExpressionUtils
from javax.swing import SwingUtilities

from addons.Arena2Importer.tablas.ARENA2_ACCIDENTES import configurar_featuretype_ARENA2_ACCIDENTES

class AccidentesActionContext(AbstractDALActionContext):
  def __init__(self, panel):
    AbstractDALActionContext.__init__(self,"Arena2ImportPanel")
    self.panel = panel

  def getStore(self):
    return self.panel.input_store
    
  def getSelectedsCount(self):
    table = self.panel.tblDatosImportar
    return table.getSelectedRowCount()

  def getFilterForSelecteds(self):
    table = self.panel.tblDatosImportar
    n = table.getSelectedRow()
    if n<0:
      return None
    f = table.getModel().get(n)
    exp = ExpressionUtils.createExpression("ID_ACCIDENTE = '%s'" % f.get("ID_ACCIDENTE"))
    return exp


class IncidenciasActionContext(AbstractDALActionContext):
  def __init__(self, panel):
    AbstractDALActionContext.__init__(self,"Arena2ImportPanel")
    self.panel = panel

  def getStore(self):
    return self.panel.input_store
    
  def getSelectedsCount(self):
    table = self.panel.tblincidents
    return table.getSelectedRowCount()

  def getFilterForSelecteds(self):
    table = self.panel.tblincidents
    n = table.getSelectedRow()
    if n<0:
      return None
    ID_ACCIDENTE = table.getModel().getAccidenteId(n)
    exp = ExpressionUtils.createExpression("ID_ACCIDENTE = '%s'" % ID_ACCIDENTE)
    return exp


class ImportPanel(FormPanel, Observer):
  def __init__(self, importManager):
    FormPanel.__init__(self,getResource(__file__,"importpanel.xml"))
    self.importManager = importManager
    self.connectionPicker = None
    self.taskStatusController = None
    self.currentFile = None
    self.input_store = None
    self.process = None
    self.initComponents()

  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    dataManager = DALLocator.getDataManager()
    dataSwingManager = DALSwingLocator.getSwingManager()
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()

    self.arena2filePicker = toolsSwingManager.createFilePickerController(
      self.txtArena2File, 
      self.btnArena2File
    )
    self.arena2filePicker.addChangeListener(self.doFileChanged)
    
    self.taskStatusController = taskManager.createTaskStatusController(
      self.lblTaskTitle,
      self.lblTaskMessage,
      self.pgbTaskProgress
    )
    self.btnImportar.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)
    self.setVisibleTaskStatus(False)

    ft = dataManager.createFeatureType()
    configurar_featuretype_ARENA2_ACCIDENTES(ft)
    self.tblDatosImportar.setModel(dataSwingManager.createSimpleFeaturesTableModel(ft, None, None))

    s = self.btnVerAccidente1.getText()
    factory = dataSwingManager.getStoreAction("ShowForm")
    self.btnVerAccidente1.setAction(factory.createAction(AccidentesActionContext(self)))
    self.btnVerAccidente2.setAction(factory.createAction(IncidenciasActionContext(self)))
    self.btnVerAccidente1.setText(s)
    self.btnVerAccidente2.setText(s)
    
    for titularidad in self.importManager.getValidOwnershipOfRoads():
      self.cboCambiarTitularidad.addItem(titularidad)
      
    self.tabImportar.setEnabledAt(1,False)
    self.tabImportar.setEnabledAt(2,False)
    self.setPreferredSize(700,500)

  def btnCambiarTitularidad_click(self, *args):
    rows = self.tblincidents.getSelectedRows()
    if rows==None or len(rows)<1:
      return
    value = self.cboCambiarTitularidad.getSelectedItem()
    if value == None:
      return
    value = value.getValue()
    model = self.tblincidents.getModel()
    for row in rows:
      model.setOwnershipOfRoad(row, value)
      model.setImport(row, True)
    
  def setVisibleTaskStatus(self, visible):
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    self.lblTaskMessage.setVisible(visible)
    
  def doFileChanged(self, *args):
    arena2file = self.arena2filePicker.get()
    if arena2file==None:
      self.btnCheckIntegrity.setEnabled(False)
      self.btnImportar.setEnabled(False)
      return
    if self.currentFile==arena2file :
      return
    self.setVisibleTaskStatus(False)
    self.btnClose.setEnabled(False)
    self.btnImportar.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)
    th = Thread(
      lambda : self.openArena2File(arena2file), 
      "ARENA2_import_openfile"
    )
    th.start()

  def openArena2File(self, f):
    dataManager = DALLocator.getDataManager()
    dataSwingManager = DALSwingLocator.getDataSwingManager()

    self.lblCount.setText("Cargando accidentes...")
    self.input_store = dataManager.openStore("ARENA2", "file", f)
    self.currentFile = f
    SwingUtilities.invokeLater(lambda : (
        self.btnCheckIntegrity.setEnabled(True),
        self.btnImportar.setEnabled(True),
        self.btnClose.setEnabled(True),
        self.lblCount.setText("%s registros" % self.input_store.getFeatureCount()),
        self.tblDatosImportar.setModel(dataSwingManager.createSimpleFeaturesTableModel(self.input_store))
      ) 
    )

  def update(self, observable, notification):
    try:
      if self.process == None:
        return
      isRunning = getattr(observable,"isRunning",None)
      if isRunning==None:
        return
      if self.process.getName()=="import":
        if not isRunning():
          self.btnClose.setEnabled(True)
          self.btnImportar.setEnabled(True)
          self.btnCheckIntegrity.setEnabled(True)
          if not observable.isAborted():
            self.setVisibleTaskStatus(False)
          
      elif self.process.getName()=="validator":
        if not isRunning():
          self.btnClose.setEnabled(True)
          self.btnCheckIntegrity.setEnabled(True)
          self.btnImportar.setEnabled(True)
          report = self.process.getReport()
          self.tblincidents.setModel(report.getTableModel())
          self.tabImportar.setEnabledAt(1,True)
          self.tabImportar.setSelectedIndex(1)
          self.lblCountIncidents.setText("%s Incidenias" % report.getRowCount())
          if not observable.isAborted():
            self.setVisibleTaskStatus(False)

    except:
      print "Ups!, se ha producido un error"
      
  def btnCheckIntegrity_click(self, *args):
    status = self.importManager.createStatus("ARENA2 validando", self)
    self.taskStatusController.bind(status)
        
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
    self.btnImportar.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)
    self.process = self.importManager.createValidatorProcess(
      self.input_store,
      status
    )
    th = Thread(self.process, "ARENA2_validator")
    th.start()
    
  def btnImportar_click(self, *args):
    workspace = DALLocator.getDataManager().getDatabaseWorkspace("ARENA2_DB")
    if workspace==None:
      msgbox("Debera contectarse al espacio de trabajo donde se encuentran las tablas de ARENA2")
      return
      
    status = self.importManager.createStatus("ARENA2 Importador", self)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
        
    self.process = self.importManager.createImportProcess(
      self.input_store,
      status
    )
    th = Thread(self.process, "ARENA2_import")
    th.start()


def main(*args):
  pass  
