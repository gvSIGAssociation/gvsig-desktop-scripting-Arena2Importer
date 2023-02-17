# encoding: utf-8

import gvsig

class PostProcess(object):
  
  def __init__(self, factory):
    self.__factory = factory

  def execute(self):
    pass

  def getFactory(self):
    return self.__factory
    


class PostProcessFactory(object):
  
  def __init__(self, id):
    self.__id = id
    
  def getName(self):
    return self.__id

  def create(self, workspace, expressionFilter, status):
    rule = PostProcess(self, workspace, expressionFilter, status)
    return rule

  def checkRequirements(self):
    return None
    
  def isSelectedByDefault(self):
    return True

  def selfConfigure(self): 
    # Crea los requisitos como tablas o nuevas columnas
    return

def main(*args):
  pass  
