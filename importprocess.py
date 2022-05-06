# encoding: utf-8

import gvsig

from gvsig import logger, LOGGER_WARN, LOGGER_ERROR
import os.path

import sys

import java.lang.Exception
import java.lang.Throwable
from java.lang import Thread, Runnable
from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.app import ApplicationLocator
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature import FeatureStore
from org.gvsig.tools.dispose import DisposeUtils

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager

class ImportProcess(Runnable):
  def __init__(self, importManager, files, workspace, report, status=None, transforms=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.report = report
    self.files = files
    if transforms == None:
      self.transforms = self.importManager.getTransforms()
    else:
      self.transforms = transforms
    self.__count = 0
    self.__actions = list()

  def add(self, action):
    self.__actions.append(action)
    
  def __len__(self):
    return self.__count

  def getName(self):
    return "import"

  def openStore(self, fname):
    dataManager = DALLocator.getDataManager()
    try:
      fname_tail = os.path.sep.join(fname.split(os.path.sep)[-3:])
      self.status.message("Cargando accidentes...(%s)" % fname_tail )
      store = dataManager.openStore("ARENA2", "file", fname, "CRS", "EPSG:25830")
      return store
    except java.lang.Throwable, ex:
      logger("Error cargando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error Cargando accidentes (%s)" % fname )
      return None
    except:
      ex = sys.exc_info()[1]
      logger("Error cargando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error cargando accidentes (%s)" % fname )
      return None
    
  def run(self):
    repo = self.workspace.getStoresRepository()
    try:
      self.__count = 0
      count_files = 0
      title = self.status.getTitle()
      for fname in self.files:
        self.status.setTitle("%s (%d/%d)" % (title, count_files, len(self.files)))
        count_files+=1
        fname_tail = os.path.sep.join(fname.split(os.path.sep)[-3:])
        
        input_store = self.openStore(fname)
        if input_store == None:
          self.status.abort()
          return

        children = input_store.getChildren()
  
        count = 0
        #TODO: este count solo cuenta hijos directos, no hijos de hijos
        for name in children.keySet():
          sourceStore = children.get(name)
          count += sourceStore.getFeatureCount()
          DisposeUtils.dispose(sourceStore)
        
    
        self.status.setRangeOfValues(0,count)
        self.status.setCurValue(0)
  
        name = "ARENA2_ACCIDENTES"
        self.status.message("Importando %s (%s)..." % (name,fname_tail))
        #print "Import "+name+"..."
        #sourceStore = input_store
        targetStore = ( repo.getStore(name), repo.getStore(name))
        self.copyTableAccidentes(input_store, targetStore)
        DisposeUtils.dispose(targetStore[0])
        DisposeUtils.dispose(targetStore[1])
        
        for name in children.keySet():
            self.status.message("Importando %s (%s)..." % (name,fname_tail))
            #print "Import "+name+"..."
            sourceStore = children.get(name)
            targetStore = repo.getStore(name)
            if name == "ARENA2_INFORMES":
              self.copyTableInformes(sourceStore, targetStore)
            else:
              self.copyTable(sourceStore, targetStore)
            DisposeUtils.dispose(sourceStore)
            DisposeUtils.dispose(targetStore)
        
        DisposeUtils.dispose(input_store)
        input_store = None
        

        
      self.status.message("Creacion completada")
      self.status.terminate()
      
      for action in self.__actions:
        action(self)
  
    
    except java.lang.Exception, ex:
      logger("Error importando accidentes.", LOGGER_WARN, ex)
      self.status.abort()
    except:
      ex = sys.exc_info()[1]
      logger("Error importando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.abort()

    finally:
      pass      

  def copyTable(self, sourceStore, targetStore):
    try:
      if sourceStore.getDefaultFeatureType().get("ID_ACCIDENTE")==None:
        report = None
      else:
        report = self.report
      targetStore.edit(FeatureStore.MODE_APPEND)
      transforms = self.transforms
      count = 0
      for f_src in sourceStore:
        accidentId = f_src.get("ID_ACCIDENTE")
        ### comprobarsi el accidente esta fuera de la fecha de cierrr
        process = True
        if report != None: ### hasToProcess
          ### Cambiar
          ### si uno no se marca, que no siga
          issue = report.hasToProcessIssue(accidentId)
          #if issue!=None:
          #  process = False # Si alguno de los issue no estan marcados, no se importa
        print "copyTable [%3d] %s import %s" % (count, accidentId, process)
        count += 1
        ## Decidir procesamiento
        # Si hay al menos un issue que esta deseleccionado, no se importa.
        #process = True
        #if report != None:
        #  issue = report.getIssue(accidentId)
        #  if issue!=None:
        #    process = issue.get("SELECTED")
        ##
        
        if process:
          f_dst = targetStore.createNewFeature(f_src)
          if report!=None:
            report.fix(f_dst)
          for transform in transforms:
            transform.apply(f_dst)
          
          targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex
      
  def copyTableInformes(self, sourceStore, targetStore):
    try:
      if sourceStore.getDefaultFeatureType().get("ID_ACCIDENTE")==None:
        report = None
      else:
        report = self.report
      targetStore.edit(FeatureStore.MODE_FULLEDIT)
      transforms = self.transforms
      for f_src in sourceStore:
        # El fichero victimas.xml y danyos.xml comprten el mismo codigo
        # de informe, asi que si ya existe en la bbdd nos lo saltamos.
        lid_informe = f_src.get("LID_INFORME")
        f_dst = targetStore.findFirst("LID_INFORME = '%s'" % lid_informe)
        if f_dst!=None:
          continue
        f_dst = targetStore.createNewFeature(f_src)
        if report!=None:
          report.fix(f_dst)
        for transform in transforms:
          transform.apply(f_dst)
        targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex

  
  def updateFeatureWithValues(self, f_src, f_dst, sourceType, targetType):
    for attr in targetType:
      if attr==None or attr.isAutomatic() or attr.isReadOnly() or attr.isComputed():
        continue
      if attr.getName().endswith("_DGT"): # Rellenar los DGT que no existen en el parser
        notAttrDGT = attr.getName()[:-len("_DGT")]
        value = f_src.get(notAttrDGT)
        if value == None and not attr.allowNull():
            continue
        f_dst.set(attr.getIndex(), value)
        
      if sourceType.get(attr.getName())!=None:
        value = f_src.get(attr.getName())
        if value == None and not attr.allowNull():
            continue
        f_dst.set(attr.getIndex(), value)
  
  def copyTableAccidentes(self, sourceStore, targetStore):
    try:
      report = self.report
      targetStore[0].edit(FeatureStore.MODE_APPEND)
      targetStore[1].edit(FeatureStore.MODE_FULLEDIT)
      transforms = self.transforms
      targetType = targetStore[1].getDefaultFeatureType()
      sourceType = sourceStore.getDefaultFeatureType()
      count = 0
      for f_src in sourceStore:
        count += 1
        accidentId = f_src.get("ID_ACCIDENTE")
        process = True
        if report != None: ### hasToProcess
          ### Cambiar
          ### si uno no se marca, que no siga
          process = report.hasToProcessIssue(accidentId)
          #if issue!=None:
          #  process = False # Si alguno de los issue no estan marcados, no se importa
        print " copyTableAccidentes [%3d] %s import %s" % (count, accidentId, process)
        
        if process:
          f_dst = targetStore[1].findFirst("ID_ACCIDENTE = '%s'" % accidentId)
          if f_dst == None:
            f_dst = targetStore[0].createNewFeature(f_src)
            # update DGT with new features
            for attr in targetType:
              if attr==None or attr.isAutomatic() or attr.isReadOnly() or attr.isComputed():
                continue
              if attr.getName().endswith("_DGT"): # Rellenar los DGT que no existen en el parser
                notAttrDGT = attr.getName()[:-len("_DGT")]
                value = f_src.get(notAttrDGT)
                if value == None and not attr.allowNull():
                    continue
                f_dst.set(attr.getIndex(), value)
            if report!=None:
              report.fix(f_dst)
            for transform in transforms:
              transform.apply(f_dst)
            targetStore[0].insert(f_dst)
          else:
            f_dst = f_dst.getEditable()
            self.updateFeatureWithValues(f_src, f_dst, sourceType, targetType)
            if report!=None:
              report.fix(f_dst)
            for transform in transforms:
              transform.apply(f_dst)
            f_dst.set("ACTUALIZADO", True)
            self.deleteChilds(accidentId)  #poner el campo a actualizado a true
            targetStore[1].update(f_dst)
            
        self.__count += 1
        self.status.incrementCurrentValue()
      targetStore[0].finishEditing()
      targetStore[1].finishEditing()
    except Throwable as ex:
      logger("Error copiando a tabla accidentes.", LOGGER_ERROR, ex)
      self.status.message("Error copiando a tabla accidentes" )
      targetStore[0].cancelEditing()
      targetStore[1].cancelEditing()
      raise ex
    except:
      targetStore[0].cancelEditing()
      targetStore[1].cancelEditing()
      ex = sys.exc_info()[1]
      logger("Error copiando a tabla accidentes. ", gvsig.LOGGER_ERROR, ex)
      self.status.message("Error copiando a tabla accidentes")
      raise ex
      
    
  def deleteChilds(self, accidentId):
    server = self.workspace.getServerExplorer()
    params = server.getOpenParameters()
    for tableName in ("ARENA2_CROQUIS", 
      "ARENA2_PEATONES", 
      "ARENA2_PASAJEROS", 
      "ARENA2_CONDUCTORES", 
      "ARENA2_VEHICULOS"):      
      builder = server.createSQLBuilder()
      delete = builder.delete()
      delete.table().database(params.getDBName()).schema(params.getSchema()).name(tableName)
      delete.where().and(delete.where().eq(
              builder.column("ID_ACCIDENTE"),
              builder.expression().constant(accidentId)
      ))
      sql = delete.toString()
      #sql = """DELETE FROM "%s" WHERE ID_ACCIDENTE = '%s'""" % (
      #  tableName,
      #  accidentId
      #)
      #gvsig.logger("deleteChilds %r" % sql)
      
      server.execute(sql)
    DisposeUtils.dispose(server)

class ValidatorProcess(Runnable):
  def __init__(self, importManager, files, report, workspace=None, status=None, rules=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.files = files
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
    return "validator"
    
  def getReport(self):
    return self.report
    
  def openStore(self, fname):
    dataManager = DALLocator.getDataManager()
    try:
      fname_tail = os.path.sep.join(fname.split(os.path.sep)[-3:])
      self.status.message("Cargando accidentes...(%s)" % fname_tail )
      store = dataManager.openStore("ARENA2", "file", fname, "CRS", "EPSG:25830")
      return store

    except java.lang.Throwable, ex:
      logger("Error cargando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error cargando accidentes (%s)" % fname )
      return None
    except:
      ex = sys.exc_info()[1]
      logger("Error cargando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error cargando accidentes (%s)" % fname )
      return None
    
    
  def run(self):
    fname = "???"
    try:
      self.__count = 0
      count_files = 0
      title = self.status.getTitle()
      for fname in self.files:
        self.status.setTitle("%s (%d/%d)" % (title, count_files, len(self.files)))
        count_files+=1
        fname_tail = os.path.sep.join(fname.split(os.path.sep)[-3:])
        self.input_store = self.openStore(fname)
        
        if self.input_store == None:
          self.status.abort()
          return
        # TODO
        #Si el featureType tiene tags de errores de valores no encontrados
        # 
        tags = self.input_store.getDefaultFeatureType().getTags()
        if tags.get("notSupportedKeys")!=None:
           print "Tags new found: ", tags
        #
        
        count = self.input_store.getFeatureCount()
    
        self.status.setRangeOfValues(0,count)
        self.status.setCurValue(0)
        rules = self.rules
  
        self.status.message("Comprobando accidentes (%s)..." % fname_tail)
        input_features = self.input_store.iterator()
        
        for feature in input_features:
          for rule in rules:
            if rule != None:
              rule.execute(self.report, feature)
          self.__count += 1
          self.status.incrementCurrentValue()

        DisposeUtils.disposeQuietly(input_features)

        print "processing children"
        children = self.input_store.getChildren()
        count = 0
        for name in children.keySet():
          print "process child ", name
          childStore = children.get(name)
          if childStore==None: 
            continue
          fset = childStore.iterator()
          for feature in fset:
            for rule in rules:
              if rule != None:
                rule.execute(self.report, feature)
          DisposeUtils.disposeQuietly(fset)
          DisposeUtils.dispose(childStore)


        
        self.input_store.dispose()
        self.input_store = None
        
        self.status.message("Comprobacion completada")
    
      self.status.terminate()
      
      for action in self.__actions:
        action(self)

    except java.lang.Throwable, ex:
      logger("Error validando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error validando accidentes (%s)" % fname )
      self.status.abort()
      raise ex
    except:
      ex = sys.exc_info()[1]
      logger("Error validando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error validando accidentes (%s)" % fname )
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

def calculateSlots(folderData, slotsize, slot=0, status=None):
  if status == None:
    status = LoggerTaskStatus("ImportArena2Files")

  status.logger("Searching files in %r" % folderData)
  factory = Arena2ReaderFactory()
  fnames = list()
  for root, dirs, files in os.walk(folderData, followlinks=True):
     for name in files:
       pathname = os.path.join(root, name)
       if pathname.lower().endswith(".xml"):
        if factory.accept(File(pathname)):
          fnames.append(pathname)
        else:
          status.logger("skip file: %r" % pathname, gvsig.LOGGER_WARN)
  fnames.sort() 

  status.logger("Found %d files" % len(fnames))
  for n in range(0,len(fnames)):
    status.logger("File: %r" % fnames[n])

  slots = (len(fnames)/slotsize)
  if (len(fnames) % slotsize) > 0 :
    slots += 1
  status.logger("Slots:")
  for n in range(0,slots):
    slide_start = n*slotsize
    slide_end = (n+1)*slotsize -1
    if slide_end > len(fnames):
      slide_end = len(fnames)
    status.logger("Slot %3d: [%3d : %3d]" %  (n, slide_start, slide_end))
  
  slide_start = slot*slotsize
  slide_end = (slot+1)*slotsize -1
  if slide_end > len(fnames):
    slide_end = len(fnames)
  status.logger("Slot size   : %d" % slotsize)
  status.logger("Total files : %d" % len(fnames))
  status.logger("Total slots : %d" % slots)
  status.logger("Current slot: %d [%3d : %3d]" % (slot, slide_start, slide_end))
  if slot+1 > slots :
    status.logger("Next slot   : None (process finished)")
  else:
    status.logger("Next slot   : %d" % (slot+1))

  return fnames[slide_start:slide_end], slots
  
def validateData(folderData, issues_pathname, slot, slotsize, workspaceName):
  status = LoggerTaskStatus("ValidateArena2Files")
    
  issues_pathname = issues_pathname % slot
  fnames, slots = calculateSlots(folderData, slotsize, slot, status)
  status.logger("validate slot %d/%d" % (slot, slots))

  if not connectToWorkspace(workspaceName, status):
    return
    
  importManager = getArena2ImportManager()
  report = MyReport(importManager)
  report.setEnabledEvents(False)
  dataManager = DALLocator.getDataManager()
  workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")
  if workspace==None:
    status.logger("Can't access to workspace ARENA2_DB", gvsig.LOGGER_WARN)
    
  p = ValidatorProcess(importManager, fnames, report, workspace, status)
  p.run()

  if os.path.exists(issues_pathname):
    status.logger("removing file %r" % issues_pathname)
    os.unlink(issues_pathname)
  explorer = dataManager.openServerExplorer("FilesystemExplorer")
  store = report.getStore()
  status.logger("export issues to %r" % issues_pathname)
  store.export(explorer,"CSV",explorer.getAddParameters(File(issues_pathname)))

def importData(folderData, issues_pathname, slot, slotsize, workspaceName):
  status = LoggerTaskStatus("ImportArena2Files")

  issues_pathname = issues_pathname % slot
  fnames, slots = calculateSlots(folderData, slotsize, slot, status)
  status.logger("import slot %d/%d" % (slot, slots))

  if not connectToWorkspace(workspaceName, status):
    return
    
  importManager = getArena2ImportManager()
  report = Report(importManager)
  report.setEnabledEvents(False)
  dataManager = DALLocator.getDataManager()
  workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")
  if workspace==None:
    status.logger("Can't access to workspace ARENA2_DB", gvsig.LOGGER_WARN)
    return

  issues = dataManager.openStore("CSV","File", issues_pathname)
  report.addIssues(issues.getFeatureSet())
  if len(report) != issues.getFeatureCount():
    status.logger("Can't load issues in report", gvsig.LOGGER_WARN)
    return
    
  p = ImportProcess(importManager, fnames, workspace, report, status)
  p.run()

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

def genetareScript(folderData, slotsize):
  fnames, slots = calculateSlots(folderData, slotsize)
  
  for slot in range(0,slots):
    print "./gvSIG.sh --splash=false --showgui=false --consolelogger=false --runScript=/addons/Arena2Importer/importprocess --closeAtFinish --slotsize=%d --validate --slot=%d" % (slotsize,slot)   
  for slot in range(0,slots):
    print "./gvSIG.sh --splash=false --showgui=false --consolelogger=false --runScript=/addons/Arena2Importer/importprocess --closeAtFinish --slotsize=%d --import --slot=%d" % (slotsize,slot)   

def main(*args):
  application = ApplicationLocator.getApplicationManager()

  arguments = application.getArguments()

  folderData = '/home/jjdelcerro/arena2/quincenas'
  issues_pathname = "/home/jjdelcerro/arena2/issuesB-%s.csv"
  workspaceName = "a2_1"
  slot = 0
  slotsize = 10
  closeAtFinish = False
  
  workspaceName = arguments.get("workspaceName",workspaceName)
  folderData = arguments.get("folderData",folderData)
  issues_pathname = arguments.get("issues",issues_pathname)
  slotsize = arguments.get("slotsize",slotsize)
  slot = arguments.get("slot",slot)
  closeAtFinish = arguments.get("closeAtFinish",closeAtFinish)
 
  if arguments.contains("generateScript","true"):
    genetareScript(folderData, slotsize)

  if arguments.contains("calculateSlots","true"):
    calculateSlots(folderData, slotsize)

  if arguments.contains("validate","true"):
    validateData(folderData, issues_pathname, slot, slotsize, workspaceName)
  
  if True or arguments.contains("import","true"):
    importData(folderData, issues_pathname, slot, slotsize, workspaceName)
  
  if closeAtFinish:
    application.close(True)
  
