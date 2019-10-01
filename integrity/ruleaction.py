# encoding: utf-8

import gvsig

class RuleAction(object):
  def __init__(self, factory, id):
    self.__factory = factory
    self.__id = id
    
  def getId(self):
    return self.__id

  def getFactory(self):
    return self.__factory
    
  def execute(self,report, selection, *args):
    # Report report, ListSelectionModel selection 
    if selection.isSelectionEmpty():
      return
    for row in range(selection.getMinSelectionIndex(), selection.getMaxSelectionIndex()+1):
      if selection.isSelectedIndex(row):
        accidentId = report.getAccidenteId(row)
        self.check(accidentId, report)
        
  def check(self, report, row, accidentId):
    # if need fix accidentId
    #   report.setFix(row,self, None)
    pass
    
  def fix(self, feature, args):
    pass
    

def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
