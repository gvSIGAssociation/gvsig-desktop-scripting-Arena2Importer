# encoding: utf-8

import gvsig

import sys
from gvsig import logger, LOGGER_WARN, LOGGER_ERROR

from collections import OrderedDict

from java.lang import IllegalArgumentException, Runnable
import java.lang.Exception
import java.lang.Throwable

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.util import Validator
from org.gvsig.tools.swing.api import ToolsSwingLocator
from org.gvsig.tools.dynobject import  DynObjectValueItem

class ReportAttribute(object):
  def __init__(self, name, javatype, size=None, label=None, isEditable=False, availableValues=None, cellEditor=None):
    self.__name = name
    self.__javatype = javatype
    self.__size = size
    self.__label = label
    self.__isEditable = isEditable
    self.__cellEditor = cellEditor
    self.__availableValues = availableValues
    #print "ReportAttribute(%r) %r" % (self.__name, self.__availableValues)

  def getLabel(self):
    if self.__label == None:
      return self.__name
    return self.__label

  def getName(self):
    return self.__name

  def getType(self):
    return self.__javatype

  def getTypeName(self):
    return self.__javatype.getSimpleName()

  def getSize(self):
    return self.__size

  def isEditable(self):
    return self.__isEditable
    
  def setEditable(self, editable):
    self.__isEditable=editable
    
  def getAvailableValues(self):
    #print "ReportAttribute(%r).getAvailableValues(1) %r" % (self.__name, self.__availableValues)
    if self.__availableValues == None:
      return None
    l = list()
    for code,label in self.__availableValues.iteritems():
      l.append(DynObjectValueItem(code,label))
    #print "ReportAttribute(%r).getAvailableValues(2) %r" % (self.__name, l)
    return l

  def setAvailableValues(self, availableValues):
    self.__availableValues = availableValues

  def getCellEditor(self):
    return self.__cellEditor
    
  def setCellEditor(self, cellEditor):
    self.__cellEditor = cellEditor
   
class ImportManager(object):
  def __init__(self):
    self.__ruleFactories = list() 
    self.__ruleFixers = dict() 
    self.__transformFactories = list() # Factory
    self.__ruleErrorCodes = OrderedDict()
    self.__reportAttributes = OrderedDict()
    self.__postProcessFactories = OrderedDict()

  def checkRequirements(self):
    messages = list()
    for factory in self.__ruleFactories:
      msg = factory.checkRequirements()
      if msg!=None:
        messages.append(msg)
    for factory in self.__transformFactories:
      msg = factory.checkRequirements()
      if msg!=None:
        messages.append(msg)
    for factory in self.getPostProcessFactories():
      msg = factory.checkRequirements()
      if msg!=None:
        messages.append(msg)
    if len(messages)==0:
      return None
    return messages
  
  def addRuleFactory(self, ruleFactory): 
    self.__ruleFactories.append(ruleFactory)

  def addRuleFixer(self, fixer):
    self.__ruleFixers[fixer.getId()] = fixer

  def addPostProcessFactory(self, postProcessFactory):
    self.__postProcessFactories[postProcessFactory.getName()] = postProcessFactory

  def getPostProcessFactories(self):
    return self.__postProcessFactories.values()

  def getPostProcessFactory(self, name):
    return self.__postProcessFactories.get(name,None)

  def addRuleErrorCode(self, errcode, description ):
    self.__ruleErrorCodes[errcode] = description

  def addReportAttribute(self, name, javatype, size=None, label=None, isEditable=False, availableValues=None, cellEditor=None):
    if self.__reportAttributes.has_key(name):
      desc = self.__reportAttributes[name]
      if desc.getAvailableValues() == None:
        desc.setAvailableValues(availableValues)
      if desc.getCellEditor() == None:
        desc.setCellEditor(cellEditor)
      if not desc.isEditable():
        desc.setEditable(isEditable)
    else:
      desc = ReportAttribute(name, javatype, size=size, label=label, availableValues=availableValues, cellEditor=cellEditor, isEditable=isEditable)
      self.__reportAttributes[name] = desc

  def getReportAttributes(self):
    return self.__reportAttributes.values()
    
  def getFixer(self, fixerID):
    return self.__ruleFixers.get(fixerID,None)

  def getRuleErrorCodes(self):
    return self.__ruleErrorCodes
  
  def getRuleFactories(self):
    return self.__ruleFactories

  def getRules(self, **args):
    rules = list()
    for factory in self.__ruleFactories:
      rule = factory.create(**args)
      rule.restart()
      rules.append(rule)
    return rules

  def addTransformFactory(self, transform):
    self.__transformFactories.append(transform)
    
  def getTransformFactories(self):
    return self.__transformFactories
    
  def getTransforms(self):
    transforms = list()
    for factory in self.__transformFactories:
      transform = factory.create()
      transform.restart()
      transforms.append(transform)
    return transforms
    
  def createImportDialog(self): 
    from addons.Arena2Importer.importpanel import ImportPanel
    dialog = ImportPanel(self)
    return dialog
    
  def createPostValidatorDialog(self): 
    from addons.Arena2Importer.validator.postvalidatorpanel import PostValidatorPanel
    dialog = PostValidatorPanel(self)
    return dialog

  def createImportProcess(self, files, workspace, report, status=None, transforms=None, deleteChildrensAlways = True, postprocess = None):
    from addons.Arena2Importer.importprocess import ImportProcess
    process = ImportProcess(self, files, workspace, report, status, transforms, deleteChildrensAlways = deleteChildrensAlways, postprocess = postprocess)
    return process
    

    
  def createValidatorProcess(self, files, report, workspace=None, status=None, rules=None):
    import addons.Arena2Importer.importprocess 
    #reload(addons.Arena2Importer.importprocess)
    process = addons.Arena2Importer.importprocess.ValidatorProcess(self, files, report, status=status, rules=rules, workspace=workspace)
    return process

  def createPostValidatorProcess(self, report, workspace=None, status=None, rules=None, expressionFilter=None):
    import addons.Arena2Importer.validator.postvalidatorprocess 
    #reload(addons.Arena2Importer.importprocess)
    process = addons.Arena2Importer.validator.postvalidatorprocess.PostValidatorProcess(self, report, status=status, rules=rules, workspace=workspace, expressionFilter=expressionFilter)
    return process
    
  def createPostUpdateProcess(self, workspace, report, status=None):
    import addons.Arena2Importer.validator.postvalidatorprocess
    process = addons.Arena2Importer.validator.postvalidatorprocess.PostUpdateProcess(self, workspace, report, status)
    return process
    
  def createPostTransformProcess(self, workspace, report, status=None, expressionFilter=None, transforms=None):
    import addons.Arena2Importer.validator.postvalidatorprocess
    process = addons.Arena2Importer.validator.postvalidatorprocess.PostTransformProcess(self, workspace, report, status, expressionFilter, transforms)
    return process
    
  def createTablestDialog(self):
    from addons.Arena2Importer.createtablespanel import CreateTablesDialog
    dialog = CreateTablesDialog(self)
    return dialog
    
  def createTablesProcess(self, connection, status, **args):
    from addons.Arena2Importer.createtablesprocess import CreateTablesProcess
    process = CreateTablesProcess(self, connection, status, **args)
    return process

  def createStatus(self, title="ARENA2", obsolete=None):
    taskManager = ToolsLocator.getTaskStatusManager()
    status = taskManager.createDefaultSimpleTaskStatus(title)
    return status

  def createReport(self):
    from addons.Arena2Importer.integrity.report import Report
    report = Report(self)
    return report

  def createPostProcessProcess(self, workspace, names, expressionFilter, status):
    return PostProcessProcess(self, workspace, names, expressionFilter, status)

class PostProcessProcess(Runnable):
  def __init__(self, importManager, workspace, names, expressionFilter, status):
    self.importManager = importManager
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.workspace = workspace
    self.names = names
    self.expressionFilter = expressionFilter
    self.__actions = list()

  def getName(self):
    return "postprocess"

  def getStatus(self):
    return self.status

  def add(self, action):
    self.__actions.append(action)
    
  def run(self):
    try:
      for factory in self.importManager.getPostProcessFactories():
        self.status.message(factory.getName())
        if factory.getName() in self.names:
          self.status.push()
          try:
            postProcess = factory.create(self.workspace, self.expressionFilter, self.status)
            postProcess.execute()
          finally:
            self.status.pop()
      self.status.terminate()
      for action in self.__actions:
        action(self)
    except java.lang.Exception, ex:
      logger("Error importando accidentes.", LOGGER_WARN, ex)
      self.status.message("Error importando accidentes. "+str(ex))
      self.status.abort()
    except:
      ex = sys.exc_info()[1]
      logger("Error importando accidentes. " + str(ex), gvsig.LOGGER_WARN, ex)
      self.status.message("Error importando accidentes. "+str(ex))
      self.status.abort()


def main(*args):
  pass
  
