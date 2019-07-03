# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from org.gvsig.tools import ToolsLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.tools.swing.api import ToolsSwingLocator
from java.lang import Thread

from addons.Arena2Importer.creartablas import CrearTablasProceso

class Arena2CrearTablasPanel(FormPanel):
  def __init__(self):
    FormPanel.__init__(self,getResource(__file__,"creartablaspanel.xml"))
    self.connectionPicker = None
    self.taskStatusController = None
    self.initComponents()

  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    self.connectionPicker = DALSwingLocator.getSwingManager().createJDBCConnectionPickerController(
            self.cboConnection,
            self.btnConnection
    )
    self.connectionPicker.addChangeListener(self.doConnectionChanged)
    
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()
    self.taskStatusController = taskManager.createTaskStatusController(
      self.lblTaskTitle,
      self.lblTaskMessage,
      self.pgbTaskProgress
    )
    self.btnAccept.setEnabled(False)
    self.setVisibleTaskStatus(False)
    self.setPreferredSize(500,270)

  def setVisibleTaskStatus(self, visible):
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    #self.lblTaskMessage.setVisible(visible)
    
  def doConnectionChanged(self, *args):
    conn = self.connectionPicker.get()
    if conn == None:
      self.btnAccept.setEnabled(False)
    else:
      self.btnAccept.setEnabled(True)
      
  def processCompleted(self):
    self.btnClose.setEnabled(True)
    self.setVisibleTaskStatus(False)
    
  def btnAccept_click(self, *args):
    status = ToolsLocator.getTaskStatusManager().createDefaultSimpleTaskStatus("ARENA2 Importador")
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
        
    process = CrearTablasProceso(
      self.connectionPicker.get(),
      status,
      self,
      self.chkCreateBaseTables.isSelected(),
      self.chkCreateDicTables.isSelected(),
      self.chkCreateLogTables.isSelected(),
      self.chkLoadDic.isSelected(),
      self.chkCreateWorkspace.isSelected()
    )
    th = Thread(process, "ARENA2_import")
    th.start()

    

def main(*args):
  panel = Arena2CrearTablasPanel()
  panel.showWindow("ARENA2 Crear tablas de accidentes")
  
