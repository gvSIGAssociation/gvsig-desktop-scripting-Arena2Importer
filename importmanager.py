# encoding: utf-8

import gvsig

from java.lang import IllegalArgumentException

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.util import Validator
from org.gvsig.tools.swing.api import ToolsSwingLocator

class CompoundValidator(Validator):
  def __init__(self):
    self.__validators = list() # List<org.gvsig.tools.util.Validator>
    self.__message = None
    self.__cause = None

  def add(self, validator): 
    if not isinstance(validator, Validator):
      raise IllegalArgumentException("Required a Validator instance ("+ str(validator.__class__)+")")
    self.__validators.append(validator)

  def getValidators(self):
    return tuple(self.__validators)

  def isValid(self, value, *args):
    for validator in self.__validators:
      if not validator.isValid(value, *args):
        self.__message = validator.getMessage()
        self.__cause = validator.getCause()
        return False
    self.__message = None
    self.__cause = None
    return True

  def getMessage(self):
    return self.__message

  def getCause(self):
    return self.__cause

class ImportManager(object):
  def __init__(self):
    self.__validator = CompoundValidator()

  def addValidator(self, validator): 
    self.__validator.add(validator)

  def getValidators(self):
    return self.__validator.getValidators()

  def getValidator(self):
    return self.__validator

  def setValidOwnershipsOfRoads(self, ownerships):
    # List<LabeledValue<Integer>>
    self.__ownerships = ownerships

  def getValidOwnershipOfRoads(self):
    if self.__ownerships == None:
      return tuple()
    return self.__ownerships
    
  def createImportDialog(self): 
    from addons.Arena2Importer.importpanel import ImportPanel
    dialog = ImportPanel(self)
    return dialog
    
  def createImportProcess(self, input_store, status=None, report=None):
    from addons.Arena2Importer.importprocess import ImportProcess
    process = ImportProcess(self, input_store, status, report)
    return process

  def createValidatorProcess(self, input_store, status=None):
    from addons.Arena2Importer.importprocess import ValidatorProcess
    process = ValidatorProcess(self, input_store, status)
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

"""
from addons.Arena2Importer.importprocess import ImportProcess, ValidatorProcess
from addons.Arena2Importer.importpanel import ImportPanel
from addons.Arena2Importer.createtablesprocess import CreateTablesProcess
from addons.Arena2Importer.createtablespanel import CreateTablesDialog
"""

