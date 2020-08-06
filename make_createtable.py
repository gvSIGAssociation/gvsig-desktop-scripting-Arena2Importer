# encoding: utf-8

import gvsig
from gvsig import getResource
from java.io import File
from java.lang import StringBuilder
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.expressionevaluator import FeatureAttributeEmulatorExpression 
from org.gvsig.fmap.dal.feature.impl import DALFile

def toSource(x):
  return repr(x)

def descriptor(builder, desc):
  builder.append("  attr = ft.add(\"").append(desc.getName()).append("\",").append(desc.getDataType().getType()).append(")\n")
  builder.append("  attr.setSize(").append(toSource(desc.getSize())).append(")\n")
  builder.append("  attr.setAllowIndexDuplicateds(").append(toSource(desc.isPrimaryKey())).append(")\n")
  builder.append("  attr.setAllowNull(").append(toSource(desc.allowNull())).append(")\n")
  builder.append("  attr.setDataProfileName(").append(toSource(desc.getDataProfileName())).append(")\n")
  builder.append("  attr.setDescription(").append(toSource(desc.getDescription())).append(")\n")
  if desc.getGeomType()!=None:
      builder.append("  attr.setGeometryType(").append(toSource(desc.getGeomType().getType())).append(", ").append(toSource(desc.getGeomType().getSubType())).append(")\n")
  
  builder.append("  attr.setGroup(").append(toSource(desc.getGroup())).append(")\n")
  builder.append("  attr.setHidden(").append(toSource(desc.isHidden())).append(")\n")
  builder.append("  attr.setIsAutomatic(").append(toSource(desc.isAutomatic())).append(")\n")
  builder.append("  attr.setIsIndexAscending(").append(toSource(desc.isIndexAscending())).append(")\n")
  builder.append("  attr.setIsIndexed(").append(toSource(desc.isIndexed())).append(")\n")
  builder.append("  attr.setIsPrimaryKey(").append(toSource(desc.isPrimaryKey())).append(")\n")
  #builder.append("  #attr.setPersistent(").append(toSource(desc.isPersistent())).append(")\n")
  builder.append("  attr.setIsReadOnly(").append(toSource(desc.isReadOnly())).append(")\n")
  builder.append("  attr.setIsTime(").append(toSource(desc.isTime())).append(")\n")
  builder.append("  attr.setLabel(").append(toSource(desc.getLabel())).append(")\n")
  #builder.append("  #attr.setMandatory(").append(toSource(desc.isMandatory())).append(")\n")
  builder.append("  attr.setOrder(").append(toSource(desc.getOder())).append(")\n")
  builder.append("  attr.setPrecision(").append(toSource(desc.getPrecision())).append(")\n")
  builder.append("  attr.setReadOnly(").append(toSource(desc.isReadOnly())).append(")\n")
  builder.append("  attr.setRelationType(").append(toSource(desc.getRelationType())).append(")\n")
  if desc.getSRS()!=None:
      builder.append("  attr.setSRS(").append(toSource(desc.getSRS().toString())).append(")\n")
  
  #builder.append("  #attr.setSubtype(").append(toSource(desc.getSubtype())).append(")\n")
  if desc.isForeingKey():
      fk = desc.getForeingKey()
      builder.append("  attr.getForeingKey().setCodeName(").append(toSource(fk.getCodeName())).append(")\n")
      builder.append("  attr.getForeingKey().setForeingKey(").append(toSource(fk.isForeingKey())).append(")\n")
      builder.append("  attr.getForeingKey().setLabelFormula(").append(toSource(fk.getLabelFormula())).append(")\n")
      builder.append("  attr.getForeingKey().setClosedList(").append(toSource(fk.isClosedList())).append(")\n")
      builder.append("  attr.getForeingKey().setTableName(").append(toSource(fk.getTableName())).append(")\n")
  
  emu = desc.getFeatureAttributeEmulator()
  if emu!=None and isinstance(emu,FeatureAttributeEmulatorExpression):
      builder.append("  attr.setFeatureAttributeEmulator(").append(toSource(emu.getExpression().getPhrase())).append(")\n")

  tags = desc.getTags()
  if tags!=None and not tags.isEmpty():
    builder.append("  tags = attr.getTags()\n")
    for name in tags:
        value = tags.get(name)
        builder.append("  tags.set(").append(toSource(name)).append(", ").append(toSource(value)).append(")\n")
              
  builder.append("\n")
  

def generateTable(pathname,tableName, ft):
  builder = StringBuilder()
  builder.append("""# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator

""")

  for attr in ft:
    builder.append("def add_attribute_%s(ft):\n" % attr.getName())
    descriptor(builder, attr)
    
  builder.append("def add_attributes_%s(ft):\n" % tableName)
  for attr in ft:
    builder.append("  add_attribute_%s(ft)\n" % attr.getName())
    
  builder.append("""

def configurar_featuretype_%s(ft):
""" % tableName )
  tags = ft.getTags()
  if tags!=None and not tags.isEmpty():
    builder.append("  tags = ft.getTags()\n")
    for name in ft.getTags():
        value = tags.get(name)
        builder.append("  tags.set(").append(toSource(name)).append(", ").append(toSource(value)).append(")\n")
              
  builder.append("""
  add_attributes_%s(ft)

def crearTabla_%s(connection):
  tableName = "%s"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()
  configurar_featuretype_%s(ft)
  
  server.add(tableName, params, False)

def main(*args):
    pass
""" % (tableName,tableName,tableName,tableName) )
  f = open(pathname,"w")
  f.write(builder.toString())
  f.close()

def create_arena2_tables():
  f = File("/home/jjdelcerro/datos/geodata/vector/ARENA2/TV_03_2019_01_Q1/victimas.xml")
  dataManager = DALLocator.getDataManager()
  print "Cargando ARENA2 file..."
  store = dataManager.openStore("ARENA2", "file", f)

  tableName = "ARENA2_ACCIDENTES"
  print "%s..." % tableName
  pathname = getResource(__file__,"tablas",tableName+".py")  
  generateTable(pathname, tableName, store.getDefaultFeatureType())

  for child in store.getChildren():
    tableName = child.getName()
    print "%s..." % tableName
    pathname = getResource(__file__,"tablas",tableName+".py")  
    generateTable(pathname, tableName, child.getDefaultFeatureType())

def create_ARENA2_AC_VE_CO_PA_PE_CR():
  tableName = "ARENA2_AC_VE_CO_PA_PE_CR"
  dataManager = DALLocator.getDataManager()
  store = dataManager.getStoresRepository().getStore(tableName)
  pathname = getResource(__file__,"tablas",tableName+".py")  
  generateTable(pathname, tableName, store.getDefaultFeatureType())

def create_DAL_ARENA2_AC_VE_CO_PA_PE_CR():
  from tablas.ARENA2_AC_VE_CO_PA_PE_CR import configurar_featuretype_ARENA2_AC_VE_CO_PA_PE_CR
  tableName = "ARENA2_AC_VE_CO_PA_PE_CR"
  dataManager = DALLocator.getDataManager()
  ft = dataManager.createFeatureType()
  configurar_featuretype_ARENA2_AC_VE_CO_PA_PE_CR(ft)
  dalfile = DALFile.getDALFile()
  dalfile.setFeatureType(ft)
  pathname = getResource(__file__,"../Arena2Reader/datos/recursos/",tableName+".dal")
  dalfile.write(File(pathname))
  
def main(*args):
  #create_arena2_tables()
  #create_ARENA2_AC_VE_CO_PA_PE_CR()
  create_DAL_ARENA2_AC_VE_CO_PA_PE_CR()