# encoding: utf-8

import gvsig
import os
from org.gvsig.tools import ToolsLocator
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.feature.impl import DALFile
from java.io import File
from org.gvsig.json import Json

def loadFeatureType(tableName, ft):
  pathname_json = gvsig.getResource(__file__,"../Arena2Importer/datos/",tableName+".featureType.json")
  f = open(pathname_json, "r")
  json_s = f.read()
  f.close()
  json = Json.createObject(json_s)
  ft.fromJson(json)

def createDalFile(tableName):
  dalFile = ToolsLocator.getFoldersManager().getTemporaryFile("Arena2Importer",tableName+".dal")
  if not dalFile.getParentFile().exists():
    os.makedirs(dalFile.getParent())
  ft = DALLocator.getDataManager().createFeatureType()
  loadFeatureType(tableName, ft)

  dalfile = DALFile.getDALFile()
  dalfile.setFeatureType(ft)
  dalfile.write(dalFile)
  print dalFile.getAbsolutePath()

def main(*args):

  for tableName in (
    "ARENA2_ACCIDENTES",
    "ARENA2_CONDUCTORES",
    "ARENA2_CROQUIS",
    "ARENA2_INFORMES",
    "ARENA2_PASAJEROS",
    "ARENA2_PEATONES",
    "ARENA2_VEHICULOS",
    "AFOROS_MEDIDAS",
    "ARENA2_AC_VE_CO_PA_PE_CR",
    ):
    createDalFile(tableName)
