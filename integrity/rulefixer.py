# encoding: utf-8

import gvsig

class RuleFixer(object):
  def __init__(self, id, description, canBeUsedInBatchMode=False):
    self.__id = id
    self.__description = description
    self.__canBeUsedInBatchMode = canBeUsedInBatchMode
    
  def getId(self):
    return self.__id

  def getDescription(self):
    return self.__description

  def canBeUsedInBatchMode(self):
    return self.__canBeUsedInBatchMode
    
  def fix(self, feature, issue):
    pass
    

def main(*args):
    pass
