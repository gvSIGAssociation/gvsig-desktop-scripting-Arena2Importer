# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from gvsig.commonsdialog import msgbox

from java.awt import Component
from java.awt import BorderLayout
from java.lang import Thread
from javax.swing import JButton
from javax.swing import SwingUtilities
from javax.swing import DefaultComboBoxModel, DefaultListModel

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.observer import Observer
from org.gvsig.tools.swing.api import ToolsSwingLocator
from org.gvsig.tools.util import LabeledValueImpl

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.fmap.dal.swing.AbstractDALActionFactory import AbstractDALActionContext
from org.gvsig.expressionevaluator import ExpressionUtils
from org.gvsig.fmap.dal.store.jdbc import JDBCServerExplorerParameters

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
    table = self.panel.tblIssues
    return table.getSelectedRowCount()

  def getFilterForSelecteds(self):
    table = self.panel.tblIssues
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
    self.report = self.importManager.createReport()
    self.initComponents()

  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    dataManager = DALLocator.getDataManager()
    dataSwingManager = DALSwingLocator.getSwingManager()
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()
    workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")

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
    
    model = DefaultListModel()
    for factory in self.importManager.getTransformFactories():
      model.addElement(factory.getName())
    self.lstTransforms.setModel(model)
    
    model = DefaultListModel()
    for factory in self.importManager.getRuleFactories():
      model.addElement(factory.getName())
    self.lstRules.setModel(model)

    pool = dataManager.getDataServerExplorerPool()
    model = DefaultComboBoxModel()
    select = -1
    n = 0
    for entry in pool:
      if isinstance(entry.getExplorerParameters(), JDBCServerExplorerParameters):
        conn = entry.getExplorerParameters()
        workspace = dataManager.createDatabaseWorkspaceManager(conn)
        if workspace.isValidStoresRepository():
          model.addElement(workspace)
          if "arena" in workspace.getId().lower():
            select = n
          n += 1
    self.cboWorkspace.setModel(model)
    self.cboWorkspace.setSelectedIndex(select)
    self.cboWorkspace.addActionListener(self.doFileChanged)

    self.tblIssues.setModel(self.report.getTableModel())
    
    self.tabImportar.setEnabledAt(1,True)
    self.tabImportar.setEnabledAt(2,True)

    if workspace == None:
      self.btnVerAccidente1.setEnabled(False)
      self.arena2filePicker.setEnabled(False)
      self.lblCount.setText("No se tiene acceso al espacio de trabajo.")
      
    self.setPreferredSize(700,500)
    
  def setVisibleTaskStatus(self, visible):
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    self.lblTaskMessage.setVisible(visible)
    
  def doFileChanged(self, *args):
    arena2file = self.arena2filePicker.get()
    arena2workspace = self.cboWorkspace.getSelectedItem()
    if arena2file==None or arena2workspace==None:
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
    try:
      self.input_store = dataManager.openStore("ARENA2", "file", f, "CRS", "EPSG:25830")
    except:
      self.input_store = None
      self.btnImportar.setEnabled(False)
      
    if self.input_store == None:
      msgbox("No se ha podido cargar el fichero indicado.")
      return
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
          self.btnCheckIntegrity.setEnabled(True)
          if not observable.isAborted():
            self.setVisibleTaskStatus(False)
            self.btnImportar.setEnabled(False)
          else:
            self.btnImportar.setEnabled(True)

      elif self.process.getName()=="validator":
        if not isRunning():
          self.btnClose.setEnabled(True)
          self.btnCheckIntegrity.setEnabled(True)
          self.btnImportar.setEnabled(True)
          #self.tblIssues.setModel(report.getTableModel())
          self.tabImportar.setEnabledAt(1,True)
          self.tabImportar.setSelectedIndex(1)
          self.lblCountIncidents.setText("%s Incidenias" % self.report.getRowCount())
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
      self.report,
      status
    )
    th = Thread(self.process, "ARENA2_validator")
    th.start()
    
  def btnImportar_click(self, *args):
      
    status = self.importManager.createStatus("ARENA2 Importador", self)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
        
    self.process = self.importManager.createImportProcess(
      self.input_store,
      self.cboWorkspace.getSelectedItem(),
      self.report,
      status
    )
    th = Thread(self.process, "ARENA2_import")
    th.start()


def main(*args):
  pass  
