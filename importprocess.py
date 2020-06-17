# encoding: utf-8

import gvsig

from gvsig import logger, LOGGER_WARN
import os.path

import sys
import traceback

import java.lang.Exception
import java.lang.Throwable

from java.lang import Thread, Runnable
from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature import FeatureStore

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
      ex = sys.exc_info()
      logger("Error cargando accidentes. %s\n%s" % (ex[1], "".join(traceback.format_exception(*ex))), LOGGER_WARN)
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
        
        self.input_store = self.openStore(fname)
        if self.input_store == None:
          self.status.abort()
          return
          
        children = self.input_store.getChildren()
  
        count = 0
        for name in children.keySet():
          sourceStore = children.get(name)
          count += sourceStore.getFeatureCount()
    
        self.status.setRangeOfValues(0,count)
        self.status.setCurValue(0)
  
        name = "ARENA2_ACCIDENTES"
        self.status.message("Importando %s (%s)..." % (name,fname_tail))
        #print "Import "+name+"..."
        sourceStore = self.input_store
        targetStore = ( repo.getStore(name), repo.getStore(name))
        self.copyTableAccidentes(sourceStore, targetStore)
        
        for name in children.keySet():
            self.status.message("Importando %s (%s)..." % (name,fname_tail))
            #print "Import "+name+"..."
            sourceStore = children.get(name)
            targetStore = repo.getStore(name)
            if name == "ARENA2_INFORMES":
              self.copyTableInformes(sourceStore, targetStore)
            else:
              self.copyTable(sourceStore, targetStore)
    
        self.status.message("Creacion completada")
        self.status.terminate()
        
        for action in self.__actions:
          action(self)
  
    
    except java.lang.Exception, ex:
      logger("Error importando accidentes.", LOGGER_WARN, ex)
      self.status.abort()

    except:
      ex = sys.exc_info()
      logger("Error importando accidentes. %s\n%s" % (ex[1], "".join(traceback.format_exception(*ex))), LOGGER_WARN)
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
      for f_src in sourceStore:
        if report==None or report.isSelected(f_src.get("ID_ACCIDENTE")):
          f_dst = targetStore.createNewFeature(f_src)
          for transform in transforms:
            transform.apply(f_dst)
          if report!=None:
            report.fix(f_dst)
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
        if report==None or report.isSelected(f_src.get("ID_ACCIDENTE")):
          f_dst = targetStore.createNewFeature(f_src)
          for transform in transforms:
            transform.apply(f_dst)
          if report!=None:
            report.fix(f_dst)
          targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex
      
  def copyTableAccidentes(self, sourceStore, targetStore):
    try:
      report = self.report
      targetStore[0].edit(FeatureStore.MODE_APPEND)
      targetStore[1].edit(FeatureStore.MODE_FULLEDIT)
      transforms = self.transforms
      targetType = targetStore[1].getDefaultFeatureType()
      sourceType = sourceStore.getDefaultFeatureType()
      for f_src in sourceStore:
        accidentId = f_src.get("ID_ACCIDENTE")
        if report==None or report.isSelected(accidentId):
          f_dst = targetStore[1].findFirst("ID_ACCIDENTE = '%s'" % accidentId)
          if f_dst == None:
            f_dst = targetStore[0].createNewFeature(f_src)
            for transform in transforms:
              transform.apply(f_dst)
            if report!=None:
              report.fix(f_dst)
            targetStore[0].insert(f_dst)
          else:
            f_dst = f_dst.getEditable()
            for attr in targetType:
              if attr==None or attr.isAutomatic() or attr.isReadOnly() or attr.isComputed():
                continue
              if targetType.get(attr.getName()+"_DGT")!=None:
                continue
              if sourceType.get(attr.getName())!=None:
                value = f_src.get(attr.getName())
                if value == None and not attr.allowNull():
                    continue
                f_dst.set(attr.getIndex(), value)
            for transform in transforms:
              transform.apply(f_dst)
            if report!=None:
              report.fix(f_dst)
            self.deleteChilds(accidentId)
            targetStore[1].update(f_dst)
        self.__count += 1
        self.status.incrementCurrentValue()
      targetStore[0].finishEditing()
      targetStore[1].finishEditing()
    except Throwable as ex:
      targetStore[0].cancelEditing()
      targetStore[1].cancelEditing()
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
      delete.where().eq(
              builder.column("ID_ACCIDENTE"),
              builder.expression().constant(accidentId)
      )
      sql = delete.toString()
      sql = """DELETE FROM "%s" WHERE ID_ACCIDENTE = '%s'""" % (
        tableName,
        accidentId
      )
      gvsig.logger("deleteChilds %r" % sql)
      
      server.execute(sql)

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
      ex = sys.exc_info()
      logger("Error cargando accidentes. %s\n%s" % (ex[1], "".join(traceback.format_exception(*ex))), LOGGER_WARN)
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
        count = self.input_store.getFeatureCount()
    
        self.status.setRangeOfValues(0,count)
        self.status.setCurValue(0)
        rules = self.rules
  
        self.status.message("Comprobando accidentes (%s)..." % fname_tail)
        for feature in self.input_store:
          for rule in rules:
            if rule != None:
              rule.execute(self.report, feature)
          self.__count += 1
          self.status.incrementCurrentValue()
    
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
      ex = sys.exc_info()
      logger("Error validando accidentes. %s\n%s" % (ex[1], "".join(traceback.format_exception(*ex))), LOGGER_WARN)
      self.status.message("Error validando accidentes (%s)" % fname )
      
    finally:
      pass


def testValidate():
  import addons.Arena2Importer.loggertaskstatus
  reload(addons.Arena2Importer.loggertaskstatus)
  
  from java.io import File
  from addons.Arena2Reader.arena2reader import Arena2ReaderFactory
  from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager
  from addons.Arena2Importer.integrity.report import Report
  from addons.Arena2Importer.loggertaskstatus import LoggerTaskStatus

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
    

  factory = Arena2ReaderFactory()
  folder = '/home/jjdelcerro/arena2/quincenas'
  fnames = list()
  for root, dirs, files in os.walk(folder, followlinks=True):
     for name in files:
       pathname = os.path.join(root, name)
       if pathname.lower().endswith(".xml"):
        if factory.accept(File(pathname)):
          gvsig.logger("found file: %r" % pathname)
          fnames.append(pathname)
        else:
          gvsig.logger("skip file: %r" % pathname, gvsig.LOGGER_WARN)
  fnames.sort()
  sufix = "all"
  
  #fnames = fnames[:1] ; sufix="00"
  
  #fnames = fnames[  0: 30] ; sufix="0"
  #fnames = fnames[ 31: 60] ; sufix="1"
  #fnames = fnames[ 61: 90] ; sufix="2"
  #fnames = fnames[121:150] ; sufix="3"
  #fnames = fnames[151:180] ; sufix="4"
  #fnames = fnames[181:210] ; sufix="5"
  #fnames = fnames[211:240] ; sufix="6"
  #fnames = fnames[241:270] ; sufix="7"
  #fnames = fnames[271:] ; sufix="8"
  
  issues_pathname = "/home/jjdelcerro/arena2/issues-%s.csv" % sufix
  gvsig.logger("block %r" % sufix)

  importManager = getArena2ImportManager()
  report = MyReport(importManager)
  status = LoggerTaskStatus("CheckArena2Files")
  dataManager = DALLocator.getDataManager()
  workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")
  if workspace==None:
    gvsig.logger("Can't access to workspace ARENA2_DB", gvsig.LOGGER_WARN)
    
  p = ValidatorProcess(importManager, fnames, report, workspace, status)
  p.run()

  if os.path.exists(issues_pathname):
    gvsig.logger("removing file %r" % issues_pathname)
    os.unlink(issues_pathname)
  explorer = dataManager.openServerExplorer("FilesystemExplorer")
  store = report.getStore()
  gvsig.logger("export issues to %r" % issues_pathname)
  store.export(explorer,"CSV",explorer.getAddParameters(File(issues_pathname)))

def testInsert():
  import addons.Arena2Importer.loggertaskstatus
  reload(addons.Arena2Importer.loggertaskstatus)
  
  from java.io import File
  from addons.Arena2Reader.arena2reader import Arena2ReaderFactory
  from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager
  from addons.Arena2Importer.integrity.report import Report
  from addons.Arena2Importer.loggertaskstatus import LoggerTaskStatus


  factory = Arena2ReaderFactory()
  folder = '/home/jjdelcerro/arena2/quincenas'
  fnames = list()
  for root, dirs, files in os.walk(folder, followlinks=True):
     for name in files:
       pathname = os.path.join(root, name)
       if pathname.lower().endswith(".xml"):
        if factory.accept(File(pathname)):
          gvsig.logger("found file: %r" % pathname)
          fnames.append(pathname)
        else:
          gvsig.logger("skip file: %r" % pathname, gvsig.LOGGER_WARN)
  fnames.sort() 
  sufix = "all"
  
  #fnames = fnames[  0:  1] ; sufix="0"
  
  #fnames = fnames[  0: 30] ; sufix="0"
  #fnames = fnames[ 31: 60] ; sufix="1"
  #fnames = fnames[ 61: 90] ; sufix="2"
  #fnames = fnames[121:150] ; sufix="3"
  #fnames = fnames[151:180] ; sufix="4"
  #fnames = fnames[181:210] ; sufix="5"
  #fnames = fnames[211:240] ; sufix="6"
  #fnames = fnames[241:270] ; sufix="7"
  #fnames = fnames[271:] ; sufix="8"
  
  issues_pathname = "/home/jjdelcerro/arena2/issues-%s.csv" % sufix
  gvsig.logger("block %r" % sufix)

  importManager = getArena2ImportManager()
  report = Report(importManager)
  status = LoggerTaskStatus("ImportArena2Files")
  dataManager = DALLocator.getDataManager()
  workspace = dataManager.getDatabaseWorkspace("ARENA2_DB")
  if workspace==None:
    gvsig.logger("Can't access to workspace ARENA2_DB", gvsig.LOGGER_WARN)
    return

  issues = dataManager.openStore("CSV","File", issues_pathname)
  report.addIssues(issues.getFeatureSet())
  if len(report) != issues.getFeatureCount():
    gvsig.logger("Can't load issues in repprt", gvsig.LOGGER_WARN)
    return
    
  p = ImportProcess(importManager, fnames, workspace, report, status)
  p.run()
    
def main(*args):
  testValidate()
  #testInsert()
  pass
