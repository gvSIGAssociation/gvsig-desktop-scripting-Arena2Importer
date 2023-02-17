# encoding: utf-8

import gvsig

import os
import sys

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
from org.gvsig.tools.swing.api import ToolsSwingLocator
from org.gvsig.tools.util import LabeledValueImpl

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator 
from org.gvsig.fmap.dal.swing.AbstractDALActionFactory import AbstractDALActionContext
from org.gvsig.expressionevaluator import ExpressionUtils
from org.gvsig.fmap.dal.store.jdbc import JDBCServerExplorerParameters
import addons.Arena2Importer
reload(addons.Arena2Importer)
#from addons.Arena2Importer.readerTablas.ARENA2_ACCIDENTES import configurar_featuretype_ARENA2_ACCIDENTES
from addons.Arena2Reader.arena2readerutils import createArena2XMLFileFilter, isArena2File

from javax.swing import JFileChooser

from org.gvsig.tools.dynform import DynFormLocator
from org.gvsig.tools.util import ToolsUtilLocator
from org.gvsig.tools.swing.api import ToolsSwingLocator
from org.gvsig.expressionevaluator.swing import ExpressionEvaluatorSwingLocator
from org.gvsig.fmap.dal.swing import DALSwingLocator

from org.gvsig.tools.swing.api import ToolsSwingUtils

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

class ExportFromIssueActionContext(AbstractDALActionContext):
  def __init__(self, panel):
    AbstractDALActionContext.__init__(self,"Arena2ImportPanelExportFromIssue")
    self.panel = panel

  def getStore(self):
    return self.panel.report.getStore()
    
class PostValidatorPanel(FormPanel):
  def __init__(self, importManager):
    FormPanel.__init__(self,getResource(__file__,"postvalidatorpanel.xml"))
    self.importManager = importManager
    self.connectionPicker = None
    self.taskStatusController = None
    self.currentFile = None
    self.process = None
    self.report = self.importManager.createReport()
    self.cltTransforms = None
    self.cltRules = None
    self.filterPicker = None
    self.initComponents()

  def getSelectedWorkspace(self):
    selectedItem = self.cboWorkspace.getSelectedItem()
    if selectedItem == None:
      return None
    return selectedItem.getValue()
    
  def initComponents(self):
    i18n = ToolsLocator.getI18nManager()
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    dataManager = DALLocator.getDataManager()
    dataSwingManager = DALSwingLocator.getSwingManager()
    taskManager = ToolsSwingLocator.getTaskStatusSwingManager()
    workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")

    #Filter
    self.cltTransforms = toolsSwingManager.createJListWithCheckbox(self.lstTransforms)
    self.cltRules = toolsSwingManager.createJListWithCheckbox(self.lstRules)
    self.cltPostProcesses = toolsSwingManager.createJListWithCheckbox(self.lstPostProcesses)
    
    self.taskStatusController = taskManager.createTaskStatusController(
      None,
      self.lblTaskTitle,
      self.lblTaskMessage,
      self.pgbTaskProgress,
      self.btnCancelTask,
      None
    )
    self.btnApplyUpdate.setEnabled(False)
    self.btnApplyTransform.setEnabled(False)
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

    #n = 0
    #for factory in self.importManager.getTransformFactories():
    #  if factory.isSelectedByDefault():
    #    self.cltTransforms.toggleCheck(n)
    #  n+=1

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
        try:
          try:
            gvsig.logger("Checking workspace %s" % workspace.getServerExplorerParameters().getUrl())
          except:
            gvsig.logger("Checking workspace %s" % workspace.getServerExplorerParameters())
          if workspace.isValidStoresRepository():
            model.addElement(LabeledValueImpl(workspace.getLabel(), workspace))
            if "arena" in workspace.getId().lower():
              select = n
            n += 1
        except:
          ex = sys.exc_info()[1]
          print "Not valid workspace. %s"% str(ex)
    self.cboWorkspace.setModel(model)
    self.cboWorkspace.setSelectedIndex(select)
    self.cboWorkspace.addActionListener(self.doDBChanged)
    self.doDBChanged()

    self.tblIssues.setModel(self.report.getTableModel())
    
    self.report.setCellEditors(self.tblIssues)
    
    if workspace == None:
      self.filterPicker.setEnabled(False)

    self.lblIssuesMessage.setText("")
    self.tblIssues.getSelectionModel().addListSelectionListener(self.issuesSelectionChanged)
    self.tblIssues.setAutoCreateRowSorter(True)
    
    swingManager = ToolsSwingLocator.getToolsSwingManager()
    swingManager.createTableColumnAdjuster(self.tblIssues)
    self.btnVerAccidente2.setEnabled(False)
    self.btnModifyIssues.setEnabled(False)

    ToolsSwingUtils.ensureRowsCols(self.asJComponent(), 20, 120, 30, 150)

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
          print "report.setSelected(%s, %s)" % (row, select)
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
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.setVisibleTaskStatus(visible))
      return
    self.lblTaskTitle.setVisible(visible)
    self.pgbTaskProgress.setVisible(visible)
    self.lblTaskMessage.setVisible(visible)
    self.btnCancelTask.setVisible(visible)

  def issuesMessage(self, s):
    self.lblIssuesMessage.setText(s)

  def message(self, s):
    self.lblTaskMessage.setText(s)
    self.lblTaskMessage.setVisible(True)

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
    self.issuesMessage(x)
    
  def doDBChanged(self, *args):
    arena2workspace = self.getSelectedWorkspace()
    if arena2workspace==None:
      self.btnCheckIntegrity.setEnabled(False)
      self.btnApplyUpdate.setEnabled(False)
      self.btnApplyTransform.setEnabled(False)
      return
    self.btnCheckIntegrity.setEnabled(True)
    self.btnApplyUpdate.setEnabled(True)
    self.btnApplyTransform.setEnabled(True)
    self.btnClose.setEnabled(True)

    repo = arena2workspace.getStoresRepository()
    accidentesStore = repo.getStore("ARENA2_ACCIDENTES")
    if self.filterPicker !=None:
      self.filterPicker.dispose()
    self.filterPicker = DALSwingLocator.getDataSwingManager().createExpressionPickerController(accidentesStore, self.txtFilter, self.btnFilter)

  def updateComponents(self, process=None):
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.updateComponents())
      return
    try:
      if self.process == None:
        self.btnClose.setEnabled(True)
        self.btnCheckIntegrity.setEnabled(True)
        self.btnApplyUpdate.setEnabled(True)
        self.btnApplyTransform.setEnabled(True)
        self.btnPostProcess.setEnabled(True)
        if self.report != None:
         self.report.setEnableUpdateUI(True)
        return

      status = self.process.getStatus()
      self.btnClose.setEnabled(not status.isRunning())
      self.btnCheckIntegrity.setEnabled(not status.isRunning())
      self.btnApplyUpdate.setEnabled(not status.isRunning())
      self.btnApplyTransform.setEnabled(not status.isRunning())
      self.btnPostProcess.setEnabled(not status.isRunning())
      if self.report != None:
        self.report.setEnableUpdateUI(not status.isRunning())

      self.setVisibleTaskStatus(status.isAborted())
    except:
      print "Ups!, se ha producido un error"

  def btnRemoveIssues_click(self, *args):
    self.report.removeAll()
  
  def btnCheckIntegrity_click(self, *args):
    
    self.btnClose.setEnabled(False)
    self.btnApplyUpdate.setEnabled(False)
    self.btnApplyTransform.setEnabled(False)
    self.btnCheckIntegrity.setEnabled(False)

    rules = list()
    n = 0
    for rule in self.importManager.getRuleFactories():
      if self.cltRules.getCheckedModel().isSelectedIndex(n):
        rules.append(rule.create(workspace=self.getSelectedWorkspace()))
      n+=1
    if len(rules)==0 :
      self.btnClose.setEnabled(True)
      self.btnApplyUpdate.setEnabled(True)
      self.btnApplyTransform.setEnabled(True)
      self.btnCheckIntegrity.setEnabled(True)
      return 
      
    status = self.importManager.createStatus("ARENA2 Post Validando", self)
    self.taskStatusController.bind(status)
        
    self.setVisibleTaskStatus(True)
    status.add()
    status.setAutoremove(True)

    self.process = self.importManager.createPostValidatorProcess(
      self.report,
      status=status,
      rules = rules,
      workspace=self.getSelectedWorkspace(),
      expressionFilter=self.filterPicker.get()
    )
    self.process.add(self.showValidatorFinishMessage)
    self.process.add(self.updateComponents)
    
    th = Thread(self.process, "ARENA2_postvalidator")
    th.start()
    
  def showValidatorFinishMessage(self, process):
    if not SwingUtilities.isEventDispatchThread():
      SwingUtilities.invokeLater(lambda :self.showValidatorFinishMessage(process))
      return
    msg = "Total %s incidencias en %s accidentes" % (
        len(process.getReport()),
        len(process)
    )
    gvsig.logger(msg)
    if not process.getStatus().isAborted() :
      self.issuesMessage(msg)
    
  def btnApplyTransform_click(self, *args):
    status = self.importManager.createStatus("ARENA2 Post transform Actualizando", self)
    status.add()
    status.setAutoremove(True)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
    
    transforms = list()
    n = 0
    for transform in self.importManager.getTransformFactories():
      if self.cltTransforms.getCheckedModel().isSelectedIndex(n):
        transforms.append(transform.create(workspace=self.getSelectedWorkspace()))
      n+=1
      
    self.process = self.importManager.createPostTransformProcess(
      self.getSelectedWorkspace(),
      self.report,
      status,
      expressionFilter=self.filterPicker.get(),
      transforms=transforms
    )
    self.process.add(self.updateComponents)
    th = Thread(self.process, "ARENA2_posttransform")
    th.start()
    
  def btnPostProcess_click(self, *args):
    names = list()
    checkModel = self.cltPostProcesses.getCheckedModel()
    if checkModel.isSelectionEmpty():
      self.message(u"Debe seleccionar algún postproceso a realizar")
      return

    for n in range(checkModel.getMinSelectionIndex(), checkModel.getMaxSelectionIndex()+1):
      if checkModel.isSelectedIndex(n):
        names.append(self.cltPostProcesses.getModel().getElementAt(n))

    status = self.importManager.createStatus("ARENA2 Post process")
    status.add()
    status.setAutoremove(True)
    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
    
    self.process = self.importManager.createPostProcessProcess(
      self.getSelectedWorkspace(),
      names,
      expressionFilter=self.filterPicker.get(),
      status=status
    )
    self.process.add(self.updateComponents)
    th = Thread(self.process, "ARENA2_postprocess")
    th.start()
    
  def btnApplyUpdate_click(self, *args):
      
    status = self.importManager.createStatus("ARENA2 Post Actualizando", self)
    status.add()
    status.setAutoremove(True)

    self.taskStatusController.bind(status)
    self.setVisibleTaskStatus(True)
    self.btnClose.setEnabled(False)
    
    self.process = self.importManager.createPostUpdateProcess(
      self.getSelectedWorkspace(),
      self.report,
      status
    )
    self.process.add(self.updateComponents)
    th = Thread(self.process, "ARENA2_postupdate")
    th.start()


def main(*args):
    from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager
    
    manager = getArena2ImportManager()
    messages = manager.checkRequirements()
    if messages!=None:
      msgbox("\n".join(messages))
      return
    dialog = manager.createPostValidatorDialog()
    dialog.showWindow("ARENA2 Validador accidentes")

def main0(*args):
  pass  
    
    