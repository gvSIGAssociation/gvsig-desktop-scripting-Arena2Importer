# encoding: utf-8

import gvsig

import os.path

import sys
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

  def getName(self):
    return "import"

  def openStore(self, fname):
    dataManager = DALLocator.getDataManager()
    try:
      self.status.message("Cargando accidentes...(%s/%s)" % ( os.path.basename(os.path.dirname(fname)), os.path.basename(fname)) )
      store = dataManager.openStore("ARENA2", "file", fname, "CRS", "EPSG:25830")
      return store
    except java.lang.Throwable, ex:
      self.status.message("Error Cargando accidentes (%s)" % fname )
      ex.printStackTrace()
      return None
    except:
      self.status.message("Error Cargando accidentes (%s)" % fname )
      print "Error Cargando accidentes", sys.exc_info()[1]
      return None
    
  def run(self):
    repo = self.workspace.getStoresRepository()
    try:
      for fname in self.files:
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
        self.status.message("Importando "+name+"...")
        print "Import "+name+"..."
        sourceStore = self.input_store
        targetStore = ( repo.getStore(name), repo.getStore(name))
        self.copyTableAccidentes(sourceStore, targetStore)
        
        for name in children.keySet():
            self.status.message("Importando "+name+"...")
            print "Import "+name+"..."
            sourceStore = children.get(name)
            targetStore = repo.getStore(name)
            self.copyTable(sourceStore, targetStore)
    
        self.status.message("Creacion completada")
        self.status.terminate()
    
    except java.lang.Exception, ex:
      print "Error import data", str(ex)
      self.status.abort()
      ex.printStackTrace()

    except Exception, ex:
      print "Error import data", str(ex)
      self.status.abort()
    
    except:
      print "Error import data"
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
      
  def copyTableAccidentes(self, sourceStore, targetStore):
    try:
      report = self.report
      targetStore[0].edit(FeatureStore.MODE_APPEND)
      targetStore[1].edit(FeatureStore.MODE_FULLEDIT)
      transforms = self.transforms
      targetType = targetStore[1].getDefaultFeatureType()
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
            for attr in targetType:
              if attr==None or attr.isAutomatic() or attr.isReadOnly() or attr.isComputed():
                continue
              if targetType.get(attr.getName()+"_DGT")!=None:
                continue
              value = f_src.get(attr.getName())
              if value == None and not attr.allowNull():
                  continue
              f_dst.set(attr.getIndex(), value)
            for transform in transforms:
              transform.apply(f_dst)
            if report!=None:
              report.fix(f_dst)
            #self.deleteChilds(accidentId)
            targetStore[1].update(f_dst)
            
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
      builder.delete().where().eq(
              builder.column("ID_ACCIDENTE"),
              builder.expression().constant(accidentId)
      )
      builder.delete().table().database(params.getDBName()).schema(params.getSchema()).name(tableName)
      sql = builder.toString()
      
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

  def getName(self):
    return "validator"
    
  def getReport(self):
    return self.report
    
  def openStore(self, fname):
    dataManager = DALLocator.getDataManager()
    try:
      self.status.message("Cargando accidentes...(%s/%s)" % ( os.path.basename(os.path.dirname(fname)), os.path.basename(fname)) )
      store = dataManager.openStore("ARENA2", "file", fname, "CRS", "EPSG:25830")
      return store
    except java.lang.Throwable, ex:
      self.status.message("Error Cargando accidentes (%s)" % fname )
      ex.printStackTrace()
      return None
    except:
      self.status.message("Error Cargando accidentes (%s)" % fname )
      print "Error Cargando accidentes", sys.exc_info()[1]
      return None
    
    
  def run(self):
    fname = "???"
    try:
      for fname in self.files:
        self.input_store = self.openStore(fname)
        if self.input_store == None:
          self.status.abort()
          return
        count = self.input_store.getFeatureCount()
    
        self.status.setRangeOfValues(0,count)
        self.status.setCurValue(0)
        rules = self.rules
  
        self.status.message("Comprobando accidentes...")
        for feature in self.input_store:
          for rule in rules:
            if rule != None:
              rule.execute(self.report, feature)
          self.status.incrementCurrentValue()
    
        self.status.message("Comprobacion completada")
    
      self.status.terminate()

    except java.lang.Throwable, ex:
      ex.printStackTrace()
      self.status.message("Error validando accidentes (%s)" % fname )
      self.status.abort()
      raise ex

    except:
      print "Error validando accidentes", sys.exc_info()[1]
      self.status.message("Error validando accidentes (%s)" % fname )
      
    finally:
      pass


def main(*args):
    print "hola mundo"
    pass
