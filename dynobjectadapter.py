# encoding: utf-8

import gvsig

from java.lang import UnsupportedOperationException, Runnable
from org.gvsig.tools.dynobject import DynObject
from org.gvsig.tools.util import Callable, Invocable, GetItemByKey

class DynObjectAdapter(DynObject, Runnable, Callable, Invocable):
  def __init__(self, delegated):
    self.__delegated = delegated
    
  def getDynClass(self):
    return None

  def implement(self, dynClass):
    pass

  def delegate(self, dynObject):
    pass

  def wrap(self, value):
    if value == None:
      return None
    for t in (int, long, float, double,basestring, tuple, list, dict):
      if isinstance(value, t):
        return value
    return DynObjectAdapter(value)

  def get(self, name):
    return self.wrap(getattr(self.__delegated, name))

  def getDynValue(self, name):
    return self.wrap(getattr(self.__delegated, name))

  def setDynValue(self, name, value):
    setattr(self.__delegated,name,value)
    
  def hasDynValue(self, name):
    return hasattr(self.__delegated, name)

  def invokeDynMethod(self, name, args):
    if name.lower() == "_get":
      return self.__delegated
    fn = getattr(self.__delegated, name)
    r = fn(*args)
    return self.wrap(r)

  def run(self):
    if hasattr(self.__delegated,"run"):
      self.__delegated.run()
    elif callable(self.__delegated):
      self.__delegated()
      
  def call(self, *args):
    if hasattr(self.__delegated,"call"):
      r = self.__delegated.call(*args)
    elif callable(self.__delegated):
      r = self.__delegated(*args)
    elif len(args)>0:
      fn = getattr(self.__delegated,args[0])
      r = fn(*(args[1:]))
    else:
      raise Error("Can't invoke call method")

    return self.wrap(r)
      
  def clear(self):
    pass

  def __getattr__(self, name):
    value = getattr(self.__delegated, name, None)
    print "return attribute ", repr(name), " value is ", repr(value), " from ", repr(self.__delegated) 
    return value
    
  def _get(self):
    return self.__delegated
    
def createDynObjectAdapter(obj):
  return DynObjectAdapter(obj)


def main(*args):
    print "hola mundo"
    pass
