# encoding: utf-8

import gvsig

import os

from gvsig import getResource
from gvsig.commonsdialog import filechooser

from gvsig.libs.formpanel import FormPanel, FormComponent
from gvsig.commonsdialog import msgbox

from java.awt import Component, Dimension
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
from addons.Arena2Reader.arena2readerutils import createArena2XMLFileFilter, isArena2File

from javax.swing import JFileChooser

from org.gvsig.tools.dynform import DynFormLocator

class ShowFormFromIssueActionContext(AbstractDALActionContext):
  def __init__(self, panel):
    AbstractDALActionContext.__init__(self,"Arena2ImportPanelShowFormFromIssue")
    self.panel = panel

  def getStore(self):
    return self.panel.report.getStore()
    
  def getSelectedsCount(self):
    table = self.panel.tblIssues
    return table.getSelectedRowCount()

  def getFilterForSelecteds(self):
    table = self.panel.tblIssues
    n = table.getSelectedRow()
    if n<0:
      return None
    n = table.convertRowIndexToModel(n)
    ID_ACCIDENTE = table.getModel().getAccidenteId(n)
    exp = ExpressionUtils.createExpression("ID_ACCIDENTE = '%s'" % ID_ACCIDENTE)
    return exp

class FilesPickerController(FormComponent):
  def __init__(self, lstFileNames, btnAddFile, btnAddFolder, btnRemoveFile):
    self.__changeListener = None
    self.lstFileNames = lstFileNames
    self.btnAddFile = btnAddFile
    self.btnAddFolder = btnAddFolder
    self.btnRemoveFile = btnRemoveFile
    self.lstFileNames.setModel(DefaultListModel())
    self.autobind()
    
  def addChangeListener(self, listener):
    self.__changeListener = listener

  def setEnabled(self, enabled):
    self.lstFileNames.setEnabled(enabled)
    self.btnAddFile.setEnabled(enabled)
    self.btnAddFolder.setEnabled(enabled)
    self.btnRemoveFile.setEnabled(enabled)

  def coerceAndSet(self, fname):
    if fname==None:
      return
    model = self.lstFileNames.getModel()
    model.addElement(fname)
    self.fireChengeEvent()

  def fireChengeEvent(self):
    if self.__changeListener==None:
      return
    self.__changeListener()
    
  def btnAddFile_click(self, *args):
    manager = ToolsSwingLocator.getThreadSafeDialogsManager()
    files = dialog = manager.showChooserDialog(
      "Seleccione fichero ARENA2",
      JFileChooser.OPEN_DIALOG,
      JFileChooser.FILES_AND_DIRECTORIES,
      True, # Multiseleccion
      None, # root path
      createArena2XMLFileFilter(), # Filter
      False # ocultar archivos ocultos
    )
    if files==None or len(files)<1:
      return
    model = self.lstFileNames.getModel()
    for f in files:
     model.addElement(f.getAbsolutePath())
    self.fireChengeEvent()
    
  def btnAddFolder_click(self, *args):
    manager = ToolsSwingLocator.getThreadSafeDialogsManager()
    files = dialog = manager.showChooserDialog(
      "Seleccione carpeta",
      JFileChooser.OPEN_DIALOG,
      JFileChooser.DIRECTORIES_ONLY,
      False, # Multiseleccion
      None, # root path
      None, # Filter
      False # ocultar archivos ocultos
    )
    if files==None or len(files)<1:
      return
    folder = files[0].getAbsolutePath()
    model = self.lstFileNames.getModel()
    for root, dirs, files in os.walk(folder, followlinks=True):
       for name in files:
         pathname = os.path.join(root, name)
         if isArena2File(pathname):
          model.addElement(pathname)
    self.fireChengeEvent()

  def btnRemoveFile_click(self, *args):
    n = self.lstFileNames.getSelectedIndex()
    if n<0:
      return
    self.lstFileNames.getModel().removeElementAt(n)
    self.fireChengeEvent()
    
  def get(self):
    model = self.lstFileNames.getModel()
    if model.getSize()<1:
      return None
    files = list()
    for n in xrange(model.getSize()):
      files.append(model.getElementAt(n))
    return files
    
class ExportFromIssueActionContext(AbstractDALActionContext):
  def __init__(self, panel):
    AbstractDALActionContext.__init__(self,"Arena2ImportPanelExportFromIssue")
    self.panel = panel

  def getStore(self):
    return self.panel.report.getStore()
    
class ImportPanel(FormPanel, Observer):
  def __init__(self, importManager):
    FormPanel.__init__(self,getResource(__file__,"importpanel.xml"))
    self.importManager = importManager
    self.connectionPicker = None
    self.taskStatusController = None
    self.currentFile = None
    self.process = None
    self.report = self.importManager.createReport()
    self.cltTransforms = None
    self.cltRules = None
    self.initComponents()

  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    dataManager = DALLocator.getDataManager()
    dataSwingManager = DALSwingLocator.getSwingManager()
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()
    workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")

    self.cltTransforms = toolsSwingManager.createJListWithCheckbox(self.lstTransforms)
    self.cltRules = toolsSwingManager.createJListWithCheckbox(self.lstRules)

    self.arena2filePicker = FilesPickerController(
      self.lstArena2Files,
      self.btnArena2FilesAddFile,
      self.btnArena2FilesAddFolder,
      self.btnArena2FilesRemoveFile
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

    dataSwingManager.setStoreAction(self.btnVerAccidente2, "ShowForm", True, ShowFormFromIssueActionContext(self))
    dataSwingManager.setStoreAction(self.btnExportIssues, "Export", True, ExportFromIssueActionContext(self))

    model = DefaultListModel()
    for factory in self.importManager.getTransformFactories():
      model.addElement(factory.getName())
    self.cltTransforms.setModel(model)
    
    model = DefaultListModel()
    for factory in self.importManager.getRuleFactories():
      model.addElement(factory.getName())
    self.cltRules.setModel(model)

    n = 0
    for factory in self.importManager.getRuleFactories():
      if factory.isSelectedByDefault():
        self.cltRules.toggleCheck(n)
      n+=1

    n = 0
    for factory in self.importManager.getTransformFactories():
      if factory.isSelectedByDefault():
        self.cltTransforms.toggleCheck(n)
      n+=1

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
    self.report.setCellEditors(self.tblIssues)
    
    if workspace == None:
      self.arena2filePicker.setEnabled(False)

    self.lblIssuesMessage.setText("")
    self.tblIssues.getSelectionModel().addListSelectionListener(self.issuesSelectionChanged)
    self.tblIssues.setAutoCreateRowSorter(True)
    self.btnVerAccidente2.setEnabled(False)
    self.btnModifyIssues.setEnabled(False)
    
    self.setPreferredSize(800,500)

  def btnModifyIssues_click(self, *args):
    selectionModel = self.tblIssues.getSelectionModel()
    if selectionModel.isSelectionEmpty():
      return
    report = self.report
    store = report.getStore()
    ft = store.getDefaultFeatureType().getCopy()
    for attr in ft:
      attr.setHidden(not attr.getTags().getBoolean("editable",False))
      #print "%s.isHidden() %s" % (attr.getName(), attr.isHidden())
    f = store.createNewFeature(ft,False)
    dynformManager = DynFormLocator.getDynFormManager()
    x = f.getAsDynObject()
    form = dynformManager.createJDynForm(ft)
    winManager = ToolsSwingLocator.getWindowManager()
    form.asJComponent().setPreferredSize(Dimension(400,200))
    dialog = winManager.createDialog(form.asJComponent(), "Modificar incidencias", None, winManager.BUTTONS_OK_CANCEL)
    dialog.show(winManager.MODE.DIALOG)
    if dialog.getAction() == winManager.BUTTON_OK:
      form.getValues(x)
      for row in xrange(selectionModel.getMinSelectionIndex(), selectionModel.getMaxSelectionIndex()+1):
        if selectionModel.isSelectedIndex(row):
          row = self.tblIssues.convertRowIndexToModel(row)
          issue = report.getIssue(row).getEditable()
          for attr in ft:
            if not attr.isHidden():
              issue.set(attr.getName(), f.get(attr.getName()))
          report.putIssue(row,issue)
      report.refresh()
      
  def setVisibleTaskStatus(self, visible):
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    self.lblTaskMessage.setVisible(visible)

  def message(self, s):
    self.lblIssuesMessage.setText(s)
    
  def issuesSelectionChanged(self, event):
    row = self.tblIssues.getSelectedRow()
    if row<0 :
      self.btnVerAccidente2.setEnabled(False)
      self.btnModifyIssues.setEnabled(False)
      return 
    self.btnVerAccidente2.setEnabled(True)
    self.btnModifyIssues.setEnabled(True)
    model = self.tblIssues.getModel()
    x = model.getValueAt(row,model.getColumnCount()-1)
    self.message(x)
    
  def doFileChanged(self, *args):
    arena2files = self.arena2filePicker.get()
    arena2workspace = self.cboWorkspace.getSelectedItem()
    if arena2files==None or arena2workspace==None:
      self.btnCheckIntegrity.setEnabled(False)
      self.btnImportar.setEnabled(False)
      return
    if self.currentFile==arena2files[0] :
      return
    self.btnCheckIntegrity.setEnabled(True)
    self.btnImportar.setEnabled(True)
    self.btnClose.setEnabled(True)

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
          if not observable.isAborted():
            self.setVisibleTaskStatus(False)

    except:
      print "Ups!, se ha producido un error"

  def btnRemoveIssues_click(self, *args):
    self.report.removeAll()
  
  def btnCheckIntegrity_click(self, *args):
    files = self.arena2filePicker.get()
    if files == None:
      return
    
    self.btnClose.setEnabled(False)
    self.btnImportar.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)

    rules = list()
    n = 0
    for rule in self.importManager.getRuleFactories():
      if self.cltRules.getCheckedModel().isSelectedIndex(n):
        rules.append(rule.create(workspace=self.cboWorkspace.getSelectedItem()))
      n+=1
    if len(rules)==0 :
      self.btnClose.setEnabled(True)
      self.btnImportar.setEnabled(True)
      self.btnCheckIntegrity.setEnabled(True)
      return 
      
    status = self.importManager.createStatus("ARENA2 validando", self)
    self.taskStatusController.bind(status)
        
    self.setVisibleTaskStatus(True)

    self.process = self.importManager.createValidatorProcess(
      files,
      self.report,
      status=status,
      rules = rules,
      workspace=self.cboWorkspace.getSelectedItem()
    )
    self.process.add(self.showValidatorFinishMessage)
    th = Thread(self.process, "ARENA2_validator")
    th.start()

  def showValidatorFinishMessage(self, process):
    self.message("Total %s incidencias en %s accidentes" % (
        len(process.getReport()),
        len(process)
      )
    )
    
  
  def btnImportar_click(self, *args):
    files = self.arena2filePicker.get()
    if files == None:
      return
      
    status = self.importManager.createStatus("ARENA2 Importador", self)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)

    transforms = list()
    n = 0
    for transform in self.importManager.getTransformFactories():
      if self.cltTransforms.getCheckedModel().isSelectedIndex(n):
        transforms.append(transform.create())
      n+=1
    
    self.process = self.importManager.createImportProcess(
      files,
      self.cboWorkspace.getSelectedItem(),
      self.report,
      status,
      transforms = transforms
    )
    th = Thread(self.process, "ARENA2_import")
    th.start()


def main(*args):
  pass  
