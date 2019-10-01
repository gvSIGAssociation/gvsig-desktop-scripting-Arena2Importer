# encoding: utf-8

import gvsig

import java.lang.Exception

from java.lang import Thread, Runnable
from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature import FeatureStore

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager

class ImportProcess(Runnable):
  def __init__(self, importManager, input_store, workspace, report, status=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.report = report
    self.input_store = input_store

  def getName(self):
    return "import"
    
  def run(self):
    repo = self.workspace.getStoresRepository()
    try:
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
      targetStore = repo.getStore(name)
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
      transforms = self.importManager.getTransforms()
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
      targetStore.edit(FeatureStore.MODE_APPEND)
      transforms = self.importManager.getTransforms()
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

class ValidatorProcess(Runnable):
  def __init__(self, importManager, input_store, report, status=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.input_store = input_store
    self.report = report

  def getName(self):
    return "validator"
    
  def getReport(self):
    return self.report
    
  def run(self):
    try:
      count = self.input_store.getFeatureCount()
  
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)
      rules = self.importManager.getRules()
      print "ValidatorProcess.run: ", rules

      self.status.message("Comprobando accidentes...")
      for feature in self.input_store:
        for rule in rules:
          if rule != None:
            rule.execute(self.report, feature)
        self.status.incrementCurrentValue()
  
      self.status.message("Comprobacion completada")
    
    except Throwable as ex:
      raise ex
      
    finally:
      self.status.terminate()


def main(*args):
    print "hola mundo"
    pass
