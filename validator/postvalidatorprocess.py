# encoding: utf-8

import gvsig

from gvsig import logger, LOGGER_WARN
import os.path

import sys

import java.lang.Exception
import java.lang.Throwable
from java.lang import Thread, Runnable
from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.app import ApplicationLocator
from org.gvsig.fmap.dal import DALLocator, DataTransaction
from org.gvsig.fmap.dal.feature import FeatureStore
from org.gvsig.tools.dispose import DisposeUtils
from org.gvsig.tools import ToolsLocator
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator, ExpressionUtils, ExpressionBuilder

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager

class PostTransformProcess(Runnable):
  def __init__(self, importManager, workspace, report, status=None, expressionFilter=None, transforms = None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.expressionFilter = expressionFilter
    self.transforms = transforms
    self.report = report
    self.__count = 0
    self.__actions = list()

  def add(self, action):
    self.__actions.append(action)
    
  def __len__(self):
    return self.__count

  def getName(self):
    return "posttransform"

  def run(self):
    trans = None
    try:

      storeAccidentes = None
      if self.transforms == None or len(self.transforms)==0:
        self.status.message("No hay transformaciones activas")
        self.status.abort()
        return
      title = self.status.getTitle()
      repo = self.workspace.getStoresRepository()
      dataManager = DALLocator.getDataManager()
      trans = dataManager.createTransaction()
      trans.begin()
      storeAccidentes = repo.getStore("ARENA2_ACCIDENTES")
      trans.add(storeAccidentes)
      if  self.expressionFilter != None and not self.expressionFilter.isEmpty():
        fsetAccidentes = storeAccidentes.getFeatureStore().getFeatureSet(self.expressionFilter)
      else:
        fsetAccidentes = storeAccidentes.getFeatureStore().getFeatureSet() ### SET FILTER
      
      count = fsetAccidentes.getSize()
      n = 0
      title = "Transformando accidentes (Accidentes)..."
      self.status.message(title)
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)
      storeAccidentes.edit(FeatureStore.MODE_PASS_THROUGH)
      for feature in fsetAccidentes:
        if self.status.isCancellationRequested():
          self.status.cancel()
          break
        n+=1
        efeature = feature.getEditable()
        #apply transforms
        for transform in self.transforms:
          transform.apply(efeature)
          
        if efeature.isModified():
          fsetAccidentes.update(efeature)
        self.status.incrementCurrentValue()
        self.status.setTitle("%s (%d/%d)" % (title, n, count))
      trans.commit()
    except java.lang.Throwable, ex:
      logger("Error transformando accidentes.", LOGGER_WARN, ex)
      DataTransaction.rollbackQuietly(trans)
      self.status.message("Error transformando accidentes (%s)")
      self.status.abort()
      raise ex
    except:
      logger("Error transformando accidentes.")
      ex = sys.exc_info()[1]
      logger("Error transformando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error transformando accidentes")
      DataTransaction.rollbackQuietly(trans)
      
    finally:
      logger("Finalizando proceso..")
      DisposeUtils.disposeQuietly(trans)
      self.status.setTitle("Finalizado proceso")
      self.status.setCurValue(0)
      self.status.abort()
      logger("..Finalizado proceso")

  
class PostUpdateProcess(Runnable):
  def __init__(self, importManager, workspace, report, status=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.report = report
    self.__count = 0
    self.__actions = list()

  def add(self, action):
    self.__actions.append(action)
    
  def __len__(self):
    return self.__count

  def getName(self):
    return "postupdate"

  def run(self):
    print "post update process"
    trans = None
    try:
      repo = self.workspace.getStoresRepository()
      issues = self.report.getIssuesAsList()
      dataManager = DALLocator.getDataManager()
      trans = dataManager.createTransaction()
      trans.begin()
      storeAccidentes = repo.getStore("ARENA2_ACCIDENTES")
      trans.add(storeAccidentes)
      storeAccidentes.edit(FeatureStore.MODE_PASS_THROUGH)
      n = 0
      count = len(issues)
      title = "Actualizando accidentes (Accidentes)..."
      self.status.message(title)
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)
      for issue in issues:
        if self.status.isCancellationRequested():
          self.status.cancel()
          storeAccidentes.cancelEditing()
          return
        n+=1
        self.status.incrementCurrentValue()
        self.status.setTitle("%s (%d/%d)" % (title, n, count))
        
        if not issue.get("SELECTED"):
          logger("Issue is not selected (%s)"% (issue.get("ID_ACCIDENTE")))
          continue
        feature = storeAccidentes.findFirst("ID_ACCIDENTE='%s'" % issue.get("ID_ACCIDENTE"))
        efeature = feature.getEditable()
        self.report.fixIssueFeature(issue, efeature)
        if efeature.isModified():
          storeAccidentes.update(efeature)
          
      trans.commit()
    except java.lang.Throwable, ex:
      DataTransaction.rollbackQuietly(trans)
      logger("Error actualizando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error actualizando accidentes (%s)")
      self.status.abort()
      raise ex
    except:
      DataTransaction.rollbackQuietly(trans)
      ex = sys.exc_info()[1]
      logger("Error actualizando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error actualizando accidentes (%s)")
    finally:
      DisposeUtils.dispose(trans)


      
class PostValidatorProcess(Runnable):
  def __init__(self, importManager, report, workspace=None, status=None, rules=None, expressionFilter=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.expressionFilter = expressionFilter
    self.report = report
    if rules == None:
      self.rules = self.importManager.getRules(workspace=self.workspace)
    else:
      self.rules = rules
    self.__count = 0
    self.__actions = list()

  def add(self, action):
    self.__actions.append(action)
    
  def __len__(self):
    return self.__count
    
  def getName(self):
    return "postvalidator"
    
  def getReport(self):
    return self.report
    
    
    
  def run(self):
    try:
      self.__count = 0
      count_files = 0
      title = self.status.getTitle()
      repo = self.workspace.getStoresRepository()
      accidentesStore = repo.getStore("ARENA2_ACCIDENTES")
      accidentesFeatureType = accidentesStore.getDefaultFeatureType()
      if  self.expressionFilter != None and not self.expressionFilter.isEmpty():
        fsetAccidentes = accidentesStore.getFeatureStore().getFeatureSet(self.expressionFilter)
      else:
        fsetAccidentes = accidentesStore.getFeatureStore().getFeatureSet()

      count = fsetAccidentes.getSize()
      # Regla por las tablas principales
      mainTables = {"ARENA2_CONDUCTORES", 
      "ARENA2_PASAJEROS", 
      "ARENA2_PEATONES",
      "ARENA2_VEHICULOS"}
      expressionTransform = ExpresionTransform(accidentesFeatureType)
      
      for mainTable in mainTables:
        self.status.message("Comprobando %s..." % mainTable)
        storeToValidate = repo.getStore(mainTable)
        if  self.expressionFilter != None and not self.expressionFilter.isEmpty():
          fset = storeToValidate.getFeatureSet(expressionTransform.applyTransform(self.expressionFilter))
        else:
          fset = storeToValidate.getFeatureSet()
        count += fset.size()
        DisposeUtils.disposeQuietly(fset)
        DisposeUtils.dispose(storeToValidate)
        
      n = 0
      self.status.message("Comprobando accidentes...")
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)

      for feature in fsetAccidentes:
        if self.status.isCancellationRequested():
          self.status.cancel()
          break
        n+=1
        self.status.setTitle("%s (%d/%d)" % (title, n, count))

        rules = self.rules

        # Regla para Accidentes
        for rule in rules:
          if rule != None:
            #print "Feature: ", feature.get("ID_ACCIDENTE"), "Rule:", rule.getName(), "\n"
            rule.execute(self.report, feature)
        self.__count += 1
        self.status.incrementCurrentValue()

      # Regla por las tablas principales
      mainTables = {"ARENA2_CONDUCTORES", 
      "ARENA2_PASAJEROS", 
      "ARENA2_PEATONES",
      "ARENA2_VEHICULOS"}
      expressionTransform = ExpresionTransform(accidentesFeatureType)
      
      for mainTable in mainTables:
        if self.status.isCancellationRequested():
          self.status.cancel()
          break
        self.status.message("Comprobando %s..." % mainTable)
        storeToValidate = repo.getStore(mainTable)
        if  self.expressionFilter != None and not self.expressionFilter.isEmpty():
          fset = storeToValidate.getFeatureSet(expressionTransform.applyTransform(self.expressionFilter))
        else:
          fset = storeToValidate.getFeatureSet()
        
        if fset!=None and fset.getSize()>0:
          for feature in fset:
            n+=1
            if self.status.isCancellationRequested():
              self.status.cancel()
              break

            for rule in rules:
              if rule != None:
                rule.execute(self.report, feature)
            self.status.incrementCurrentValue()
        DisposeUtils.disposeQuietly(fset)
        DisposeUtils.dispose(storeToValidate)
        storeToValidate = None
        
        self.status.message("Comprobacion completada")
      DisposeUtils.disposeQuietly(fsetAccidentes)
      self.status.terminate()
      for action in self.__actions:
        action(self)

    except java.lang.Throwable, ex:
      logger("Error validando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error validando accidentes (%s)" % "Accidentes")
      self.status.abort()
      raise ex
    except:
      ex = sys.exc_info()[1]
      logger("Error validando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error validando accidentes (%s)"  % "Accidentes")
    finally:
      pass


from java.io import File

import addons.Arena2Importer.loggertaskstatus
reload(addons.Arena2Importer.loggertaskstatus)

from addons.Arena2Importer.loggertaskstatus import LoggerTaskStatus
from addons.Arena2Importer.integrity.report import Report
from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager
from addons.Arena2Reader.arena2reader import Arena2ReaderFactory

class MyReport(Report):
  def __init__(self, importManager):
    Report.__init__(self, importManager)
    self.count = 0
    
  def add(self, accidentId, errcode, description, selected=None, fixerId=None, **args):
    gvsig.logger("add issue[%03d]: accidentId=%r errcode=%r description=%r" % (
        self.count,
        accidentId,
        errcode,
        description
      )
    )
    selected=True
    self.count+=1
    Report.add(self,accidentId, errcode, description, selected, fixerId, **args)

def connectToWorkspace(name, status=None):
  if status == None:
    status = LoggerTaskStatus("ImportArena2Files")
    
  dataManager = DALLocator.getDataManager()
  pool = dataManager.getDataServerExplorerPool()
  poolentry = pool.get(name)
  if poolentry==None:
    status.logger("Can't locate connection %r" % name, gvsig.LOGGER_WARN)
    return False
  conn = poolentry.getExplorerParameters()
  workspace = dataManager.createDatabaseWorkspaceManager(conn)
  workspace.connect()
  status.logger("Connected to workspace %r" % name)
  return True

def validateData(issues_pathname, workspaceName):
  status = LoggerTaskStatus("ValidateArena2DB")
    
  #issues_pathname = issues_pathname % slot
  #status.logger("validate slot %d/%d" % (slot, slots))
  print "Printing"
  if not connectToWorkspace(workspaceName, status):
    print "out 1"
    return
  print "Printing 2"
  importManager = getArena2ImportManager()
  report = MyReport(importManager)
  report.setEnabledEvents(False)
  print "Checking access to database work space.."
  dataManager = DALLocator.getDataManager()
  workspace = dataManager.getDatabaseWorkspace('ARENA2_DB')
  
  if workspace==None:
    print "..out"
    status.logger("Can't access to workspace ARENA2_DB", gvsig.LOGGER_WARN)
    return

  print "PostValidating process.."
  p = PostValidatorProcess(importManager, report, workspace, status)
  print ".. preparing.."
  p.run()
  print ".. after run."

  if os.path.exists(issues_pathname):
    status.logger("removing file %r" % issues_pathname)
    os.unlink(issues_pathname)
  explorer = dataManager.openServerExplorer("FilesystemExplorer")
  store = report.getStore()
  status.logger("export issues to %r" % issues_pathname)
  import ntpath
  base = ntpath.basename(issues_pathname)
  #store.export(explorer,"CSV",explorer.getAddParameters(File(issues_pathname)), base)
  print "## DONE EXPORT"

def main2(*args):
  application = ApplicationLocator.getApplicationManager()

  arguments = application.getArguments()

  #issues_pathname = "/home/osc/gva_arena2/develtest/issuesB-%s.csv"
  workspaceName = "a2testquincena1"
  closeAtFinish = False
  from gvsig.utils import getTempFile
  issues_pathname = getTempFile('a2testquincena1', '.csv', tempdir='/home/fdiaz/gva_arena2/develtest')
  print issues_pathname

  workspaceName = arguments.get("workspaceName",workspaceName)
  issues_pathname = arguments.get("issues",issues_pathname)
  closeAtFinish = arguments.get("closeAtFinish",closeAtFinish)
  #validate = arguments.get("validate", True)
 
  #if arguments.contains("generateScript","true"):
  #  genetareScript(folderData, slotsize)

  #if arguments.contains("calculateSlots","true"):
  #  calculateSlots(folderData, slotsize)

  #if arguments.contains("validate","true"):
  validateData(issues_pathname, workspaceName)
  print "Validated data"
  
  if closeAtFinish:
    application.close(True)
  print "Done test"

def main(*args):
  expressionEvaluatorManager = ExpressionEvaluatorLocator.getExpressionEvaluatorManager()
  expression = expressionEvaluatorManager.createExpression()
  expression.setPhrase("(FECHA_ACCIDENTE >=  DATE '2021-12-01' ) and (FECHA_ACCIDENTE <=  DATE '2021-12-02')" )
  expressionTransform = ExpresionTransform()
  print expressionTransform.applyTransform(expression)
  
class ExpresionTransform(ExpressionBuilder.Visitor):
  def __init__(self, featureType = None):
    self.replacements = []
    self.featType = featureType

  def visit(self, value):
    if not isinstance(value,ExpressionBuilder.Variable) :
      return
    if self.featType != None:
      attr = self.featType.get(value.name())
      if attr == None:
        return
    builder = ExpressionUtils.createExpressionBuilder()
    v = builder.function("FOREING_VALUE",builder.constant("ID_ACCIDENTE."+value.name()))
    self.replacements.append((value,v))

  def applyTransform(self,expression):
    value = expression.getCode().toValue()
    value.accept(self, None)
    for r in self.replacements:
      value.replace(r[0], r[1])
    return value.toString()
