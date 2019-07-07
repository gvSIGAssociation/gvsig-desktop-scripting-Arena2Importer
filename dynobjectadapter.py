# encoding: utf-8

import gvsig

from java.lang import UnsupportedOperationException
from org.gvsig.tools.dynobject import DynObject

class DynObjectAdapter(DynObject):
  def __init__(self, delegated):
    self.__delegated = delegated
    
  def getDynClass(self):
    return None

  def implement(self, dynClass):
    pass

  def delegate(sewlf, dynObject):
    pass

  def getDynValue(self, name):
    return getattr(self.__delegated, name)

  def setDynValue(self, name, value):
    setattr(self.__delegated,name,value)
    
  def hasDynValue(self, name):
    return hasattr(self.__delegated, name)

  def invokeDynMethod(self, code, args):
    raise UnsupportedOperationException("Not supported yet.")

  def clear(self):
    raise UnsupportedOperationException("Not supported yet.")
        




def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
