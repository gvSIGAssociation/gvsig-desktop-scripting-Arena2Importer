# encoding: utf-8

import gvsig


class Transform(object):
  def __init__(self, factory):
    self.__factory = factory

  def getName(self):
    return self.__factory.getName()

  def apply(self, *args):
    pass


class TransformFactory(object):
  def __init__(self, id):
    self.__id = id
    
  def getName(self):
    return self.__id

  def create(self, *args):
    transform = Transform(self)
    return transform
    
  def isSelectedByDefault(self):
    return True

def main(*args):
    pass
