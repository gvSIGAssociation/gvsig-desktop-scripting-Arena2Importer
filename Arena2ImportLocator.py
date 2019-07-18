# encoding: utf-8

import gvsig

from org.gvsig.app import ApplicationLocator

from addons.Arena2Importer.dynobjectadapter import createDynObjectAdapter
from addons.Arena2Importer.importmanager import ImportManager

def getArena2ImportManager():
  application = ApplicationLocator.getApplicationManager()
  adapter = application.getProperty("ARENA2.importManager")
  if adapter == None:
    manager = ImportManager()
    adapter = createDynObjectAdapter(manager)
    application.setProperty("ARENA2.importManager",adapter)
  else:
    manager = adapter._get()
  return manager

getManager = getArena2ImportManager
  
    
def selfRegister():
  application = ApplicationLocator.getApplicationManager()
  manager = ImportManager()
  adapter = createDynObjectAdapter(manager)
  application.setProperty("ARENA2.importManager",adapter)
  

def main(*args):
  selfRegister()
