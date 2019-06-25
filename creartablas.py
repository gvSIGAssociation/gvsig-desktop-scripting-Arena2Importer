# encoding: utf-8

import gvsig

from java.lang import Runnable
from java.lang import Thread

from org.gvsig.fmap.dal import DALLocator

from addons.Arena2Importer.tablas.accidentes import crearTablaAccidentes
from addons.Arena2Importer.tablas.conductores import crearTablaConductores
from addons.Arena2Importer.tablas.croquis import crearTablaCroquis
from addons.Arena2Importer.tablas.informes import crearTablaInformes
from addons.Arena2Importer.tablas.pasajeros import crearTablaPasajeros
from addons.Arena2Importer.tablas.peatones import crearTablaPeatones
from addons.Arena2Importer.tablas.vehiculos import crearTablaVehiculos

from addons.Arena2Reader import diccionarios

class CrearTablasProceso(Runnable):
  def __init__(self, 
    connection,
    status,
    callback,
    crearTablasBase=True,
    crearTablasDiccionarios=True,
    crearTablasDeRegistro=True,
    cargarDiccionarios=True
    ):
    self.connection = connection
    self.status = status
    self.crearTablasBase=crearTablasBase
    self.crearTablasDiccionarios=crearTablasDiccionarios
    self.crearTablasDeRegistro=crearTablasDeRegistro
    self.cargarDiccionarios=cargarDiccionarios
    self.callback=callback

  def run(self):
    Thread.sleep(5000)
    
    dataManager = DALLocator.getDataManager()

    if self.crearTablasBase:
      self.status.message("Creando tabla de accidentes")
      crearTablaAccidentes(self.connection)

      self.status.message("Creando tabla de conductores")
      crearTablaConductores(self.connection)
      
      self.status.message("Creando tabla de croquis")
      crearTablaCroquis(self.connection)
      
      self.status.message("Creando tabla de informes")
      crearTablaInformes(self.connection)
      
      self.status.message("Creando tabla de pasajeros")
      crearTablaPasajeros(self.connection)
      
      self.status.message("Creando tabla de peatones")
      crearTablaPeatones(self.connection)
      
      self.status.message("Creando tabla de vehiculos")
      crearTablaVehiculos(self.connection)

    if self.crearTablasDeRegistro:
      pass

    if self.crearTablasDiccionarios:
      for name in diccionarios.getNames():
        parameters = diccionarios.getParameters(name)
        
      pass

    if self.cargarDiccionarios:
      pass
      
    self.status.message("Creacion completada")
    self.callback.processCompleted()

    





def main(*args):
    print "hola mundo"
    pass
