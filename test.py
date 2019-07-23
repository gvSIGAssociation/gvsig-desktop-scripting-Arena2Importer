# encoding: utf-8

import gvsig

from gvsig import getResource
from org.gvsig.tools.util import LabeledValueImpl
from org.gvsig.tools.util import Validator

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager, selfRegister

TITULARIDADES = (
  LabeledValueImpl("01 - Estatal",1),
  LabeledValueImpl("02 - Autonomica",2),
  LabeledValueImpl("03 - Provincial, Cabildo/Consell",3),
  LabeledValueImpl("04 - Municipal",4),
  LabeledValueImpl("05 - Otra",5),
)

def testImport():
  manager = getArena2ImportManager()
  dialog = manager.createImportDialog()
  dialog.arena2filePicker.coerceAndSet(
    getResource(__file__,"..","Arena2Reader","datos", "test","TV_03_2019_01_Q1","victimas.xml")
  )
  dialog.showWindow("ARENA2 Importar accidentes")

class TestValidator(Validator):
  def __init__(self):
    self.__message = None
    self.__cause = None

  def isValid(self, value, *args):
    if value.get("CARRETERA") == "N-332":
      self.__message = "Carretera N-332"
      self.__cause = None
      return False
    return True

  def getMessage(self):
    return self.__message

  def getCause(self):
    return self.__cause

def testCreateTables():
  manager = getArena2ImportManager()
  dialog = manager.createTablestDialog()
  dialog.showWindow("ARENA2 Crear tablas de accidentes")

def main(*args):
  
  selfRegister()
  manager = getArena2ImportManager()
  manager.addValidator(TestValidator())
  manager.setValidOwnershipsOfRoads(TITULARIDADES)
  testImport()
  #testCreateTables()

