# encoding: utf-8

import gvsig

from java.lang import IllegalArgumentException

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.util import Validator
from org.gvsig.tools.swing.api import ToolsSwingLocator


class ImportManager(object):
  def __init__(self):
    self.__ruleFactories = list() 
    self.__transformFactories = list() # Factory
    
  def addRuleFactory(self, ruleFactory): 
    self.__ruleFactories.append(ruleFactory)

  def getRuleFactories(self):
    return self.__ruleFactories

  def getRules(self):
    rules = list()
    for factory in self.__ruleFactories:
      print "getRules: Create rule ", factory.getName()
      rules.append(factory.create())
    print "getRules return: ", rules
    return rules

  def addTransformFactory(self, transform):
    self.__transformFactories.append(transform)
    
  def getTransformFactories(self):
    return self.__transformFactories
    
  def getTransforms(self):
    transforms = list()
    for factory in self.__transformFactories:
      print "getTransforms: Create transform ", factory.getName()
      transforms.append(factory.create())
    return transforms
    
  def createImportDialog(self): 
    from addons.Arena2Importer.importpanel import ImportPanel
    dialog = ImportPanel(self)
    return dialog
    
  def createImportProcess(self, input_store, workspace, report, status=None):
    from addons.Arena2Importer.importprocess import ImportProcess
    process = ImportProcess(self, input_store, workspace, report, status)
    return process

  def createValidatorProcess(self, input_store, report, status=None):
    from addons.Arena2Importer.importprocess import ValidatorProcess
    process = ValidatorProcess(self, input_store, report, status)
    return process

  def createTablestDialog(self):
    from addons.Arena2Importer.createtablespanel import CreateTablesDialog
    dialog = CreateTablesDialog(self)
    return dialog
    
  def createTablesProcess(self, connection, status, **args):
    from addons.Arena2Importer.createtablesprocess import CreateTablesProcess
    process = CreateTablesProcess(self, connection, status, **args)
    return process

  def createStatus(self, title="ARENA2", observer=None):
    taskManager = ToolsLocator.getTaskStatusManager()
    status = taskManager.createDefaultSimpleTaskStatus(title)
    if observer!=None:
      status.addObserver(observer)
    return status

  def createReport(self):
    from addons.Arena2Importer.integrity.report import Report
    report = Report(self)
    return report
    

