# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from java.awt import Component
from org.gvsig.tools import ToolsLocator
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.tools.swing.api import ToolsSwingLocator
from java.lang import Thread
from java.awt import BorderLayout
from javax.swing import JButton

from addons.Arena2Importer.importar import ImportarProceso
from addons.Arena2Importer.importar import ComprobarIntegridadProceso

class Arena2ImportadorPanel(FormPanel):
  def __init__(self):
    FormPanel.__init__(self,getResource(__file__,"importarpanel.xml"))
    i18n = ToolsLocator.getI18nManager()
    self.setPreferredSize(600,400)

    self.connectionPicker = None
    self.taskStatusController = None
    self.currentFile = None
    self.initComponents()

  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    dalSwingManager = DALSwingLocator.getSwingManager()
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()

    self.connectionPicker = dalSwingManager.createJDBCConnectionPickerController(
            self.cboConnection,
            self.btnConnection
    )
    self.connectionPicker.addChangeListener(self.doFileOrConnectionChanged)
    
    self.arena2filePicker = toolsSwingManager.createFilePickerController(
      self.txtArena2File, 
      self.btnArena2File
    )
    self.arena2filePicker.addChangeListener(self.doFileOrConnectionChanged)
    
    self.taskStatusController = taskManager.createTaskStatusController(
      self.lblTaskTitle,
      self.lblTaskMessage,
      self.pgbTaskProgress
    )
    self.btnImportar.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)
    self.btnCambiarTitularidad.setEnabled(False)
    self.btnVerFichaAccidente.setEnabled(False)
    self.setVisibleTaskStatus(False)
    self.tabImportar.setEnabledAt(1,False)
    self.setPreferredSize(700,500)

  def setVisibleTaskStatus(self, visible):
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    #self.lblTaskMessage.setVisible(visible)
    
  def doFileOrConnectionChanged(self, *args):
    conn = self.connectionPicker.get()
    arena2file = self.arena2filePicker.get()

    if arena2file!=None and self.currentFile!=arena2file :
      self.openArena2File(arena2file)
      
    if conn == None or arena2file==None:
      self.btnCheckIntegrity.setEnabled(False)
    else:
      self.btnCheckIntegrity.setEnabled(True)

  def openArena2File(self, f):
    dataManager = DALLocator.getDataManager()
    store = dataManager.openStore("ARENA2", "file", f)
    panel = DALSwingLocator.getSwingManager().createFeatureStoreSearchPanel(store)
    self.tabImportar.setComponentAt(0, panel.asJComponent())
    self.currentFile = f
  
  def processCompleted(self):
    self.btnClose.setEnabled(True)
    self.setVisibleTaskStatus(False)
    
  def btnImportar_click(self, *args):
    status = ToolsLocator.getTaskStatusManager().createDefaultSimpleTaskStatus("ARENA2 Importador")
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
        


def main(*args):
  panel = Arena2ImportadorPanel()
  panel.showWindow("ARENA2 Importar accidentes")
  
