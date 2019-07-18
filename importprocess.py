# encoding: utf-8

import gvsig

from java.lang import Thread, Runnable
from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature import FeatureStore

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager

class ImportProcess(Runnable):
  def __init__(self, importManager, input_store, status=None, report=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.report = report
    self.input_store = input_store

  def getName(self):
    return "import"
    
  def run(self):
    repo = DALLocator.getDataManager().getStoresRepository()
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
    
    except Throwable as ex:
      raise ex
      
    finally:
      self.status.terminate()

  def copyTable(self, sourceStore, targetStore):
    try:
      report = self.report
      targetStore.edit(FeatureStore.MODE_APPEND)
      for f_src in sourceStore:
        if report.haveToImport(f_src.get("ID_ACCIDENTE")):
          f_dst = targetStore.createNewFeature(f_src)
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
      for f_src in sourceStore:
        if report.haveToImport(f_src.get("ID_ACCIDENTE")):
          f_dst = targetStore.createNewFeature(f_src)
          # Copiar los atributos extra
          targetStore.insert(f_dst)
        self.status.incrementCurrentValue()
      targetStore.finishEditing()
    except Throwable as ex:
      targetStore.cancelEditing()
      raise ex

class ValidatorProcess(Runnable):
  def __init__(self, importManager, input_store, status=None):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.input_store = input_store
    self.report = Report()

  def getName(self):
    return "validator"
    
  def getReport(self):
    return self.report
    
  def run(self):
    self.report = Report()
    try:
      count = self.input_store.getFeatureCount()
  
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)
      validator = self.importManager.getValidator()

      self.status.message("Comprobando accidentes...")
      for feature in self.input_store:
        if not validator.isValid(feature):
          self.report.add(feature.get("ID_ACCIDENTE"), validator.getMessage(), validator.getCause())
        self.status.incrementCurrentValue()
  
      self.status.message("Comprobacion completada")
    
    except Throwable as ex:
      raise ex
      
    finally:
      self.status.terminate()

class Report(AbstractTableModel):
  def __init__(self):
    self.__incidents = list()
    self.__columnNames = ("Importar", "Cod. accidente", "Titularidad", "Description")
    self.__columnTypes = (Boolean, String, Integer, String)
    self.__ownershipsOfRoads = dict()
    ownershipsOfRoads = getArena2ImportManager().getValidOwnershipOfRoads()
    for x in ownershipsOfRoads:
      self.__ownershipsOfRoads[x.getValue()] = x.getLabel()

  def add(self, accidentId, description, titularidad=None, cause=None):
    self.__incidents.append([False, accidentId, titularidad, description, cause])

  def setImport(self, row, value):
    self.__incidents[row][0] = value
    self.fireTableDataChanged()
  
  def setOwnershipOfRoad(self, row, value):
    self.__incidents[row][2] = value
    self.fireTableDataChanged()

  def getAccidenteId(self, row):
    return self.__incidents[row][1]
    
  def haveToImport(self, accidentId):
    for line in self.__incidents:
      if line[1] == accidentId:
        return line[0]
    return True
     
  def getTableModel(self):
    return self

  def getRowCount(self):
    return len(self.__incidents)

  def getColumnCount(self):
    return len(self.__columnNames)

  def getColumnName(self, columnIndex):
    return self.__columnNames[columnIndex]

  def getColumnClass(self, columnIndex):
    return self.__columnTypes[columnIndex]

  def isCellEditable(self, rowIndex, columnIndex):
    return columnIndex in (0,3)

  def getValueAt(self, rowIndex, columnIndex):
    line = self.__incidents[rowIndex]
    if columnIndex==2:
      return self.__ownershipsOfRoads.get(line[2],"")
    return line[columnIndex]

  def setValueAt(self, aValue, rowIndex, columnIndex):
    if columnIndex in (0,3):
      self.__incidents[rowIndex][columnIndex] = aValue


def main(*args):
    print "hola mundo"
    pass
