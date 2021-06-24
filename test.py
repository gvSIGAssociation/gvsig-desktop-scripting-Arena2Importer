# encoding: utf-8

import gvsig

from gvsig import getResource
from org.gvsig.tools.util import LabeledValueImpl
from org.gvsig.tools.util import Validator

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager, selfRegister

#from addons.AccidentRate import geocode 

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

def testCreateTables():
  manager = getArena2ImportManager()
  dialog = manager.createTablestDialog()
  dialog.showWindow("ARENA2 Crear tablas de accidentes")


def testDeleteChildrenSQL():
    
    from org.gvsig.fmap.dal import DALLocator
    dataManager = DALLocator.getDataManager()
    pool = dataManager.getDataServerExplorerPool()
    #explorerParams = pool.get("carreteras_gva")#.getExplorerParameters()
    #if explorerParams==None:

    ws = dataManager.getDatabaseWorkspace("ARENA2_DB")
    server = ws.getServerExplorer()
    params = server.getOpenParameters()
    tableName = "ARENA2_CROQUIS"
    accidentId = "201903090000013"
    builder = server.createSQLBuilder()
    delete = builder.delete()
    delete.table().database(params.getDBName()).schema(params.getSchema()).name(tableName)
    delete.where().and(delete.where().eq(
            builder.column("ID_ACCIDENTE"),
            builder.expression().constant(accidentId)
    ))
    sql = delete.toString()
    print builder, type(builder)
    print sql
      
def main(*args):
  #testCreateTables()()
  
  #selfRegister()
  #geocode.selfRegister()
  
  #manager = getArena2ImportManager()
  #print manager.checkRequirements()
  #manager.addValidator(TestValidator())
  #manager.setValidOwnershipsOfRoads(TITULARIDADES)
  #testImport()
  #testCreateTables()
  testDeleteChildrenSQL()

