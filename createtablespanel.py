# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from org.gvsig.tools import ToolsLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.tools.swing.api import ToolsSwingLocator
from java.lang import Thread
from org.gvsig.tools.observer import Observer


class CreateTablesDialog(FormPanel, Observer):
  def __init__(self, importManager):
    FormPanel.__init__(self,getResource(__file__,"createtablespanel.xml"))
    self.importManager = importManager
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
    self.lblTaskMessage.setVisible(visible)
    
  def doConnectionChanged(self, *args):
    conn = self.connectionPicker.get()
    if conn == None:
      self.btnAccept.setEnabled(False)
    else:
      self.btnAccept.setEnabled(True)
      
  def update(self, observable, notification):
    isRunning = getattr(observable,"isRunning",None)
    if isRunning==None:
      return
    if not isRunning():
      self.btnClose.setEnabled(True)
      if not observable.isAborted():
        self.setVisibleTaskStatus(False)
    
  def btnAccept_click(self, *args):
    status = self.importManager.createStatus("ARENA2 tablas", self)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
        
    process = self.importManager.createTablesProcess(
      self.connectionPicker.get(),
      status,
      createBaseTables=self.chkCreateBaseTables.isSelected(),
      createDicTables=self.chkCreateDicTables.isSelected(),
      loadDics=self.chkLoadDic.isSelected(),
      createWorkspace=self.chkCreateWorkspace.isSelected()
    )
    th = Thread(process, "ARENA2_createtables")
    th.start()

    

def main(*args):
  pass
  
