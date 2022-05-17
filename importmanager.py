# encoding: utf-8

import gvsig

from collections import OrderedDict

from java.lang import IllegalArgumentException

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.util import Validator
from org.gvsig.tools.swing.api import ToolsSwingLocator
from org.gvsig.tools.dynobject import  DynObjectValueItem

class ReportAttribute(object):
  def __init__(self, name, javatype, size=None, label=None, isEditable=False, availableValues=None, celleditor=None):
    self.__name = name
    self.__javatype = javatype
    self.__size = size
    self.__label = label
    self.__isEditable = isEditable
    self.__celleditor = celleditor
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
    
  def getAvailableValues(self):
    #print "ReportAttribute(%r).getAvailableValues(1) %r" % (self.__name, self.__availableValues)
    if self.__availableValues == None:
      return None
    l = list()
    for code,label in self.__availableValues.iteritems():
      l.append(DynObjectValueItem(code,label))
    #print "ReportAttribute(%r).getAvailableValues(2) %r" % (self.__name, l)
    return l
      
class ImportManager(object):
  def __init__(self):
    self.__ruleFactories = list() 
    self.__ruleFixers = dict() 
    self.__transformFactories = list() # Factory
    self.__ruleErrorCodes = OrderedDict()
    self.__reportAttributes = OrderedDict()

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
    if len(messages)==0 :
      return None
    return messages
  
  def addRuleFactory(self, ruleFactory): 
    self.__ruleFactories.append(ruleFactory)

  def addRuleFixer(self, fixer):
    self.__ruleFixers[fixer.getId()] = fixer

  def addRuleErrorCode(self, errcode, description ):
    self.__ruleErrorCodes[errcode] = description

  def addReportAttribute(self, name, javatype, size=None, label=None, isEditable=False, availableValues=None, celleditor=None):
    desc = ReportAttribute(name, javatype, size=size, label=label, availableValues=availableValues, celleditor=celleditor, isEditable=isEditable)
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
      print "getTransforms: Create transform ", factory.getName()
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

  def createImportProcess(self, files, workspace, report, status=None, transforms=None, deleteChildrensAlways = True):
    from addons.Arena2Importer.importprocess import ImportProcess
    process = ImportProcess(self, files, workspace, report, status, transforms, deleteChildrensAlways = deleteChildrensAlways)
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
    
def main(*args):
  pass
  
