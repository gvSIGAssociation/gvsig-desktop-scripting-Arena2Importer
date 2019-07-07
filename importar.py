# encoding: utf-8

import gvsig

from java.lang import Runnable
from java.lang import Thread
from java.lang import Throwable

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature import FeatureStore

class ImportarProceso(Runnable):
  def __init__(self, status, callback, input_store, filter):
    self.status = status
    self.callback = callback
    self.input_store = input_store
    self.filter = filter

  def run(self):

    repo = DALLocator.getDataManager().getStoresRepository()
    try:
      children = self.input_store.getChildren()

      count = 0
      #sourceStore = self.input_store
      #count += sourceStore.getFeatureCount()
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
      self.copyTableAccidentes(sourceStore, targetStore, self.filter)
      
      for name in children.keySet():
          self.status.message("Importando "+name+"...")
          print "Import "+name+"..."
          sourceStore = children.get(name)
          targetStore = repo.getStore(name)
          self.copyTable(sourceStore, targetStore, self.filter)
          #self.status.incrementCurrentValue()
  
      self.status.message("Creacion completada")
    
    except Throwable as ex:
      raise ex
      
    finally:
      self.callback.processCompleted()

  def copyTable(self, sourceStore, targetStore, filter):
    try:
      targetStore.edit(FeatureStore.MODE_APPEND)
      for f_src in sourceStore:
        if filter!=None and filter.test(f_src):
          continue
        f_dst = targetStore.createNewFeature(f_src)
        targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex
      
  def copyTableAccidentes(self, sourceStore, targetStore, filter):
    try:
      targetStore.edit(FeatureStore.MODE_APPEND)
      for f_src in sourceStore:
        if filter!=None and filter.test(f_src):
          continue
        f_dst = targetStore.createNewFeature(f_src)
        # Copiar los atributos extra
        targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex
      
class ComprobarIntegridadProceso(Runnable):
  def __init__(self):
    pass

  def run(self):
    pass

def main(*args):
    print "hola mundo"
    pass
