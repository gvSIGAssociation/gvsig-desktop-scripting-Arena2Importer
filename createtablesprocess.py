# encoding: utf-8

import gvsig

from java.lang import Runnable
from java.lang import Thread
import java.lang.Exception 

from org.apache.commons.io import IOUtils

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.DatabaseWorkspaceManager import TABLE_RESOURCES, TABLE_REPOSITORY, TABLE_CONFIGURATION
from org.gvsig.fmap.dal.DatabaseWorkspaceManager import CONFIG_NAME_STORESREPOSITORYID, CONFIG_NAME_STORESREPOSITORYLABEL

from addons.Arena2Importer.tablas.ARENA2_ACCIDENTES import add_attributes_ARENA2_ACCIDENTES
from addons.Arena2Importer.tablas.ARENA2_CONDUCTORES import add_attributes_ARENA2_CONDUCTORES
from addons.Arena2Importer.tablas.ARENA2_CROQUIS import add_attributes_ARENA2_CROQUIS
from addons.Arena2Importer.tablas.ARENA2_INFORMES import add_attributes_ARENA2_INFORMES
from addons.Arena2Importer.tablas.ARENA2_PASAJEROS import add_attributes_ARENA2_PASAJEROS
from addons.Arena2Importer.tablas.ARENA2_PEATONES import add_attributes_ARENA2_PEATONES
from addons.Arena2Importer.tablas.ARENA2_VEHICULOS import add_attributes_ARENA2_VEHICULOS

from addons.Arena2Reader import diccionarios
from addons.Arena2Reader import recursos

class CreateTablesProcess(Runnable):
  def __init__(self, 
      importProcess,
      connection,
      status,
      createBaseTables=True,
      createDicTables=True,
      createLogTables=True,
      loadDics=True,
      createWorkspace=True
    ):
    self.importProcess = importProcess
    self.connection = connection
    if status == None:
      self.status = self.importManager.createStatus()
    else:
      self.status = status
    self.createBaseTables=createBaseTables
    self.createDicTables=createDicTables
    self.createLogTables=createLogTables
    self.loadDics=loadDics
    self.createWorkspace=createWorkspace

  def run(self):
    try:
      count = 0
      if self.createBaseTables:
        count += 7
      if self.createLogTables:
        count += 0
      if self.createDicTables:
        count += len(diccionarios.getNames())
      if self.loadDics:
        count += len(diccionarios.getNames())
      if self.createWorkspace:
        count += 7+len(diccionarios.getNames())
      
      self.status.setRangeOfValues(0,count)
      self.status.setCurValue(0)
      
      dataManager = DALLocator.getDataManager()
      workspace = dataManager.createDatabaseWorkspaceManager(self.connection)
      server = dataManager.openServerExplorer(
          self.connection.getExplorerName(),
          self.connection
      )
  
      if self.createWorkspace:
        self.status.message("Creando espacio de trabajo")
        workspace.create("ARENA2_DB","ARENA2 (db)")
        
      if self.createBaseTables:
        self.status.message("Creando ARENA2_ACCIDENTES")
        params = server.getAddParameters("ARENA2_ACCIDENTES")
        ft = params.getDefaultFeatureType()
        add_attributes_ARENA2_ACCIDENTES(ft)
        server.add("ARENA2_ACCIDENTES", params, False)
        self.status.incrementCurrentValue()
        for tableName, add_attributes in (
          ("ARENA2_CONDUCTORES",add_attributes_ARENA2_CONDUCTORES), 
          ("ARENA2_CROQUIS",add_attributes_ARENA2_CROQUIS), 
          ("ARENA2_INFORMES",add_attributes_ARENA2_INFORMES),
          ("ARENA2_PASAJEROS",add_attributes_ARENA2_PASAJEROS), 
          ("ARENA2_PEATONES",add_attributes_ARENA2_PEATONES), 
          ("ARENA2_VEHICULOS",add_attributes_ARENA2_VEHICULOS)
          ):
          self.status.message("Creando "+tableName)
          params = server.getAddParameters(tableName)
          ft = params.getDefaultFeatureType()
          add_attributes(ft)
          server.add(tableName, params, False)
          self.status.incrementCurrentValue()
  
      if self.createLogTables:
        pass
  
      if self.createDicTables:
        for tableName in diccionarios.getNames():
          self.status.message("Creando "+tableName)
          self.status.incrementCurrentValue()
          parameters = diccionarios.getParameters(tableName)
          addparams = server.getAddParameters(tableName)
          ft = addparams.getDefaultFeatureType()
          store = dataManager.openStore(parameters.getProviderName(),parameters)
          ft.copyFrom(store.getDefaultFeatureType())
          store.dispose()
          server.add(tableName, addparams, False)
  
  
      if self.loadDics:
        for tableName in diccionarios.getNames():
          self.status.message("Importando "+tableName)
          self.status.incrementCurrentValue()
          params_src = diccionarios.getParameters(tableName)
          params_dst = server.get(tableName)
          store_src = dataManager.openStore(params_src.getProviderName(),params_src)
          store_dst = dataManager.openStore(params_dst.getProviderName(),params_dst)
          store_src.copyTo(store_dst)
          store_src.dispose()
          store_dst.dispose()
  
      if self.createWorkspace:
        self.status.message("Actualizando espacio de trabajo")
        for tableName in ("ARENA2_ACCIDENTES",
          "ARENA2_CONDUCTORES", "ARENA2_CROQUIS", 
          "ARENA2_INFORMES","ARENA2_PASAJEROS", 
          "ARENA2_PEATONES", "ARENA2_VEHICULOS"):
          self.status.message("Actualizando espacio de trabajo ("+tableName+")")
          self.status.incrementCurrentValue()
          params = server.get(tableName)
          workspace.writeStoresRepositoryEntry(tableName, params)
          
          resourcesStorage_src = recursos.getResourcesStorage(tableName)
          resourcesStorage_dst = server.getResourcesStorage(params)
          #print "recursos de ",repr(tableName), repr(recursos.getResourceNames(tableName))
          for resourceName in recursos.getResourceNames(tableName):
            self.status.message("Actualizando espacio de trabajo (%s/%s)" % (tableName,resourceName))
            resource_src = resourcesStorage_src.getResource(resourceName)
            resource_dst = resourcesStorage_dst.getResource(resourceName)
            IOUtils.copy(
              resource_src.asInputStream(), 
              resource_dst.asOutputStream()
            )
            resource_src.close()
            resource_dst.close()
              
        for tableName in diccionarios.getNames():
          self.status.message("Actualizando espacio de trabajo ("+tableName+")")
          self.status.incrementCurrentValue()
          params = server.get(tableName)
          workspace.writeStoresRepositoryEntry(tableName, params)
            
        self.status.incrementCurrentValue()
        
      self.status.message("Creacion completada")
      self.status.terminate()

    except java.lang.Exception, ex:
      print "Error creating tables", str(ex)
      self.status.abort()
      ex.printStackTrace()
    except Exception, ex:
      print "Error creating tables", str(ex)
      self.status.abort()
    except:
      print "Error creating tables"
      self.status.abort()
    finally:
      pass

def main(*args):
    print "hola mundo"
    pass
