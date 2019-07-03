# encoding: utf-8

import gvsig

from java.lang import Runnable
from java.lang import Thread

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

class CrearTablasProceso(Runnable):
  def __init__(self, 
    connection,
    status,
    callback,
    crearTablasBase=True,
    crearTablasDiccionarios=True,
    crearTablasDeRegistro=True,
    cargarDiccionarios=True,
    crearEspacioDeTrabajo=True
    ):
    self.connection = connection
    self.status = status
    self.crearTablasBase=crearTablasBase
    self.crearTablasDiccionarios=crearTablasDiccionarios
    self.crearTablasDeRegistro=crearTablasDeRegistro
    self.cargarDiccionarios=cargarDiccionarios
    self.crearEspacioDeTrabajo=crearEspacioDeTrabajo
    self.callback=callback

  def run(self):
    count = 0
    if self.crearTablasBase:
      count += 7
    if self.crearTablasDeRegistro:
      count += 0
    if self.crearTablasDiccionarios:
      count += len(diccionarios.getNames())
    if self.cargarDiccionarios:
      count += len(diccionarios.getNames())
    if self.crearEspacioDeTrabajo:
      count += 1
    
    self.status.setRangeOfValues(0,count)
    self.status.setCurValue(0)
    
    dataManager = DALLocator.getDataManager()
    workspace = dataManager.createDatabaseWorkspaceManager(self.connection)
    server = dataManager.openServerExplorer(
        self.connection.getExplorerName(),
        self.connection
    )

    if self.crearEspacioDeTrabajo:
      if not workspace.existsTable(TABLE_RESOURCES):
        workspace.createTable(TABLE_RESOURCES)
      
    if self.crearTablasBase:
      self.status.message("Creando ARENA2_ACCIDENTES")
      params = server.getAddParameters("ARENA2_ACCIDENTES")
      ft = params.getDefaultFeatureType()
      add_attributes_ARENA2_ACCIDENTES(ft)
      server.add("ARENA2_ACCIDENTES", params, False)
      # Añadir copia del tipo via 
      # Añadir MAPA geometria
      self.status.incrementCurrentValue()
      for tableName in (
        "ARENA2_CONDUCTORES", "ARENA2_CROQUIS", 
        "ARENA2_INFORMES","ARENA2_PASAJEROS", 
        "ARENA2_PEATONES", "ARENA2_VEHICULOS"):
        self.status.message("Creando "+tableName)
        params = server.getAddParameters(tableName)
        ft = params.getDefaultFeatureType()
        add_attributes_ARENA2_ACCIDENTES(ft)
        server.add(tableName, params, False)
        self.status.incrementCurrentValue()

    if self.crearTablasDeRegistro:
      pass

    if self.crearTablasDiccionarios:
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


    if self.cargarDiccionarios:
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

    if self.crearEspacioDeTrabajo:
      self.status.message("Creando espacio de trabajo")
      if not workspace.existsTable(TABLE_CONFIGURATION):
        workspace.createTable(TABLE_CONFIGURATION)
      if not workspace.existsTable(TABLE_REPOSITORY):
        workspace.createTable(TABLE_REPOSITORY)
      workspace.set(CONFIG_NAME_STORESREPOSITORYID,"ARENA2_DB")
      workspace.set(CONFIG_NAME_STORESREPOSITORYLABEL,"ARENA2 (db)")
      for tableName in ("ARENA2_ACCIDENTES",
        "ARENA2_CONDUCTORES", "ARENA2_CROQUIS", 
        "ARENA2_INFORMES","ARENA2_PASAJEROS", 
        "ARENA2_PEATONES", "ARENA2_VEHICULOS"):
        self.status.message("Creando espacio de trabajo ("+tableName+")")
        self.status.incrementCurrentValue()
        params = server.get(tableName)
        workspace.storesRepositoryWriteEntry(tableName, params)
      for tableName in diccionarios.getNames():
        self.status.message("Creando espacio de trabajo ("+tableName+")")
        self.status.incrementCurrentValue()
        params = server.get(tableName)
        workspace.storesRepositoryWriteEntry(tableName, params)

      self.status.incrementCurrentValue()
      
      
    self.status.message("Creacion completada")
    self.callback.processCompleted()

    





def main(*args):
    print "hola mundo"
    pass
