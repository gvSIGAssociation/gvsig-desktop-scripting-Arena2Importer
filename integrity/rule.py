# encoding: utf-8

import gvsig

class Rule(object):
  def __init__(self, factory):
    self.__factory = factory
    self.__actions = list()

  def execute(self, report, feature):
    pass
    
  def getName(self):
    return self.__factory.getName()
    
  def getFactory(self):
    return self.__factory
    
  def getActions(self):
    return self.__actions
    
  def getAction(self, name):
    for action in self.__actions:
      if action.getName() == name:
        return action
    return None


class RuleFactory(object):
  def __init__(self, id):
    self.__id = id
    
  def getName(self):
    return self.__id

  def create(self, **args):
    rule = Rule(self, **args)
    return rule
    
  def isSelectedByDefault(self):
    return True
        
def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
