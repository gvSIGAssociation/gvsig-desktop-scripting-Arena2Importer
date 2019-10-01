# encoding: utf-8

import gvsig

from java.lang import Throwable, String, Boolean, Integer

from javax.swing.table import AbstractTableModel


class Report(AbstractTableModel):
  def __init__(self, importManager):
    self.__importManager = importManager
    self.__issues = list()
    self.__columnNames = ("", "Cod. accidente", "Type", "Issue")
    self.__columnTypes = (Boolean, String, String, String)

  def add(self, accidentId, type, issue):
    self.__issues.append([False, accidentId, type, issue, None, None])
    return len(self.__issues)-1

  def setFix(self, row, action, value=None):
    self.__issues[row][4] = action
    self.__issues[row][5] = value
    self.__issues[row][0] = True

  def fix(self, feature):
    accidentId = feature.get("ID_ACCIDENTE")
    for line in self.__issues:
      if line[1] == accidentId:
        action = line[4]
        if action!=None:
          args = line[5]
          action.fix(feature, args)
    
  def getAccidenteId(self, row):
    return self.__issues[row][1]
    
  def setSelected(self, row, value):
    self.__issues[row][0] = value
    self.fireTableDataChanged()
  
  def isSelected(self, accidentId):
    for line in self.__issues:
      if line[1] == accidentId:
        return line[0]
    return True
     
  def getTableModel(self):
    return self

  def getRowCount(self):
    return len(self.__issues)

  def getColumnCount(self):
    return len(self.__columnNames)

  def getColumnName(self, columnIndex):
    return self.__columnNames[columnIndex]

  def getColumnClass(self, columnIndex):
    return self.__columnTypes[columnIndex]

  def isCellEditable(self, rowIndex, columnIndex):
    return columnIndex == 0

  def getValueAt(self, rowIndex, columnIndex):
    line = self.__issues[rowIndex]
    return line[columnIndex]

  def setValueAt(self, aValue, rowIndex, columnIndex):
    if columnIndex == 0:
      self.__issues[rowIndex][columnIndex] = aValue


def main(*args):
    pass
