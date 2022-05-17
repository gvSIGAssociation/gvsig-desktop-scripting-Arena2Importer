# encoding: utf-8

import gvsig


class Transform(object):
  def __init__(self, factory):
    self.__factory = factory

  def getName(self):
    return self.__factory.getName()

  def apply(self, *args):
    pass

  def restart(self):
    pass


class TransformFactory(object):
  def __init__(self, id):
    self.__id = id
    self.values = {}
    
  def getName(self):
    return self.__id
    
  def getWorkspace(self):
    if "workspace" in self.values.keys():
      return self.values["workspace"]
    return None
    
  def checkRequirements(self):
    return None

  def create(self, *args):
    transform = Transform(self)
    self.values.update(args)
    return transform
    
  def isSelectedByDefault(self):
    return True
    
  def selfConfigure(self): 
    # Crea los requisitos como tablas o nuevas columnas
    return
    
def main(*args):
    pass
