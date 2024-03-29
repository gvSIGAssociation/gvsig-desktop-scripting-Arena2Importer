# encoding: utf-8

import gvsig

import os, sys
from gvsig import logger
from gvsig import LOGGER_WARN,LOGGER_INFO,LOGGER_ERROR
from gvsig import getResource
from gvsig.commonsdialog import filechooser, confirmDialog, YES_NO_CANCEL, YES, CANCEL, QUESTION

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
from org.gvsig.tools.swing.api import ToolsSwingLocator, ToolsSwingUtils
from org.gvsig.tools.util import LabeledValueImpl

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.fmap.dal.swing.AbstractDALActionFactory import AbstractDALActionContext
from org.gvsig.expressionevaluator import ExpressionUtils
from org.gvsig.fmap.dal.store.jdbc import JDBCServerExplorerParameters

#from addons.Arena2Importer.tablas.ARENA2_ACCIDENTES import configurar_featuretype_ARENA2_ACCIDENTES
from addons.Arena2Reader.arena2readerutils import createArena2XMLFileFilter, isArena2File

from javax.swing import JFileChooser

from org.gvsig.tools.dynform import DynFormLocator
from org.gvsig.tools.util import ToolsUtilLocator
from org.gvsig.tools.swing.api import ToolsSwingLocator
def createFileChooserDialog(title, type, selectionMode, multiselection, initialPath, filter, fileHidingEnabled):
    fcdManager = ToolsUtilLocator.getFileDialogChooserManager()
    dialog = fcdManager.create("arena2_importxml")
    dialog.setDialogTitle(title)
    dialog.setDialogType(type)
    dialog.setFileSelectionMode(selectionMode)
    dialog.setMultiSelectionEnabled(multiselection)
    dialog.setCurrentDirectory(fcdManager.getLastPath("arena2_importxml",initialPath))
    dialog.setFileFilter(filter)
    dialog.setFileHidingEnabled(fileHidingEnabled)
    return dialog

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
    dialog = createFileChooserDialog(
      "Seleccione fichero ARENA2",
      JFileChooser.OPEN_DIALOG,
      JFileChooser.FILES_ONLY,
      True, # Multiseleccion
      None, # root path
      createArena2XMLFileFilter(), # Filter
      False # ocultar archivos ocultos
    )
    dialog.showOpenDialog(None)
    files = dialog.getSelectedFiles()
    if files==None or len(files)<1:
      return
    model = self.lstFileNames.getModel()
    for f in files:
     model.addElement(f.getAbsolutePath())
    self.fireChengeEvent()
    
  def btnAddFolder_click(self, *args):
    dialog = createFileChooserDialog(
      "Seleccione carpeta",
      JFileChooser.OPEN_DIALOG,
      JFileChooser.DIRECTORIES_ONLY,
      False, # Multiseleccion
      None, # root path
      None, # Filter
      False # ocultar archivos ocultos
    )
    dialog.showOpenDialog(None)
    folder = dialog.getSelectedFile()
    if folder==None:
      return
    folder = folder.getAbsolutePath()
    paths = list()
    for root, dirs, files in os.walk(folder, followlinks=True):
       for name in files:
         pathname = os.path.join(root, name)
         if isArena2File(pathname):
           paths.append(pathname)
    paths.sort()
    model = self.lstFileNames.getModel()
    for pathname in paths:
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
    
class ImportPanel(FormPanel):
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
    self.cltPostProcesses = toolsSwingManager.createJListWithCheckbox(self.lstPostProcesses)

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

    model = DefaultListModel()
    for factory in self.importManager.getPostProcessFactories():
      model.addElement(factory.getName())
    self.cltPostProcesses.setModel(model)

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

    n = 0
    for factory in self.importManager.getPostProcessFactories():
      if factory.isSelectedByDefault():
        self.cltPostProcesses.toggleCheck(n)
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
          label = workspace.getLabelOrId()
          if label in (None,""):
            label = conn.getUrl()
          else:
            label = label + " [" + conn.getUrl() + "]"
          if workspace.isConnected():
            label = "<html><b>%s</b></html>"%label
          model.addElement(LabeledValueImpl(label, workspace))
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
    
    swingManager = ToolsSwingLocator.getToolsSwingManager()
    swingManager.createTableColumnAdjuster(self.tblIssues)
    self.btnVerAccidente2.setEnabled(False)
    self.btnModifyIssues.setEnabled(False)

    ToolsSwingUtils.ensureRowsCols(self.asJComponent(),25,100,30,150)

  def btnImportAll_click(self, *args):
    self.doSelectImport(True)
    
  def btnImportNone_click(self, *args):
    self.doSelectImport(False)

  def doSelectImport(self, select):
    report = self.report
    selectionModel = self.tblIssues.getSelectionModel()
    if selectionModel.isSelectionEmpty():
      report.setSelectedAll(select)
      #for row in range(len(report)):
      #  report.setSelected(row, select)
    else:
      for row in xrange(selectionModel.getMinSelectionIndex(), selectionModel.getMaxSelectionIndex()+1):
        if selectionModel.isSelectedIndex(row):
          row = self.tblIssues.convertRowIndexToModel(row)
          report.setSelected(row, select)
  
  def btnModifyIssues_click(self, *args):
    selectionModel = self.tblIssues.getSelectionModel()
    if selectionModel.isSelectionEmpty():
      return
    report = self.report
    store = report.getStore()
    ft = store.getDefaultFeatureType().getCopy()
    for attr in ft:
      isHidden = not attr.getTags().getBoolean("editable",False)
      attr.setHidden(isHidden)
      #print "%s.isHidden() %s" % (attr.getName(), isHidden)
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

  def updateComponents(self, process=None):
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.updateComponents())
      return
    try:
      if self.process == None:
        self.btnClose.setEnabled(True)
        self.btnCheckIntegrity.setEnabled(True)
        self.btnImportar.setEnabled(True)
        if self.report != None:
         self.report.setEnableUpdateUI(True)
        return

      status = self.process.getStatus()
      self.btnClose.setEnabled(not status.isRunning())
      self.btnCheckIntegrity.setEnabled(not status.isRunning())
      self.btnImportar.setEnabled(not status.isRunning())
      if self.report != None:
        self.report.setEnableUpdateUI(not status.isRunning())

      self.setVisibleTaskStatus(status.isAborted())
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
    status = self.importManager.createStatus("ARENA2 validando", self)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    ws = self.cboWorkspace.getSelectedItem().getValue()
    if not ws.isConnected():
      n = confirmDialog(u"No está conectado al espacio de trabajo '%s' \n¿Desea conectarse antes de continuar?"%ws.getLabelOrId(),"ARENA2 Importar accidentes", YES_NO_CANCEL, QUESTION)
      if n==CANCEL:
        return
      if n == YES:
        ws.connect()
    for rule in self.importManager.getRuleFactories():
      if self.cltRules.getCheckedModel().isSelectedIndex(n):
        rules.append(rule.create(workspace=ws))
      n+=1
    if len(rules)==0 :
      self.btnClose.setEnabled(True)
      self.btnImportar.setEnabled(True)
      self.btnCheckIntegrity.setEnabled(True)
      return 

    self.report.setEnableUpdateUI(False)
    self.process = self.importManager.createValidatorProcess(
      files,
      self.report,
      status=status,
      rules = rules,
      workspace=ws
    )
    self.process.add(self.showValidatorFinishMessage)
    self.process.add(self.updateComponents)    
    th = Thread(self.process, "ARENA2_validator")
    th.start()

  def showValidatorFinishMessage(self, process):
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.showValidatorFinishMessage(process))
      return

    if not process.getStatus().isAborted():
      self.message("Total %s incidencias en %s accidentes" % (
          len(process.getReport()),
          len(process)
        )
      )

  def showImportFinishMessage(self, process):
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.showImportFinishMessage(process))
      return

    if not process.getStatus().isAborted():
      self.message(u"Importación terminada")
  
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
    ws = self.cboWorkspace.getSelectedItem().getValue()
    if not ws.isConnected():
      n = confirmDialog(u"No está conectado al espacio de trabajo '%s' \n¿Desea conectarse antes de continuar?"%ws.getLabelOrId(),"ARENA2 Importar accidentes", YES_NO_CANCEL, QUESTION)
      if n==CANCEL:
        return
      if n == YES:
        ws.connect()
    for transform in self.importManager.getTransformFactories():
      if self.cltTransforms.getCheckedModel().isSelectedIndex(n):
        transforms.append(transform.create(workspace=ws))
      n+=1

    names = list()
    checkModel = self.cltPostProcesses.getCheckedModel()
    for n in range(checkModel.getMinSelectionIndex(), checkModel.getMaxSelectionIndex()+1):
      if checkModel.isSelectedIndex(n):
        names.append(self.cltPostProcesses.getModel().getElementAt(n))
    postprocess = None
    if len(names) > 0:
      postprocess = self.importManager.createPostProcessProcess(
        ws,
        names,
        expressionFilter=None,
        status=status
      )

    self.process = self.importManager.createImportProcess(
      files,
      ws,
      self.report,
      status,
      transforms = transforms,
      postprocess = postprocess
      #, deleteChildrensAlways = ??
    )

    self.process.add(self.showImportFinishMessage)
    self.process.add(self.updateComponents)

    th = Thread(self.process, "ARENA2_import")
    th.start()

def main(*args):
    from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager
    
    manager = getArena2ImportManager()
    messages = manager.checkRequirements()
    if messages!=None:
      msgbox("\n".join(messages))
      return
    dialog = manager.createImportDialog()
    dialog.showWindow("ARENA2 Importar accidentes")

def main0(*args):
  pass  
    