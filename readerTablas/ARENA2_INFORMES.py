# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator

def add_attribute_LID_INFORME(ft):
  attr = ft.add("LID_INFORME",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_INFORME')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(True)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Id_informe')
  attr.setOrder(0)
  attr.setPrecision(-1)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_COD_INFORME(ft):
  attr = ft.add("COD_INFORME",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'COD_INFORME')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Codigo_informe')
  attr.setOrder(10)
  attr.setPrecision(-1)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_FECHA_INI_EXPORT(ft):
  attr = ft.add("FECHA_INI_EXPORT",9)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'FECHA_INI_EXPORT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Fecha_inicio')
  attr.setOrder(20)
  attr.setPrecision(-1)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_FECHA_FIN_EXPORT(ft):
  attr = ft.add("FECHA_FIN_EXPORT",9)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'FECHA_FIN_EXPORT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Fecha_fin')
  attr.setOrder(30)
  attr.setPrecision(-1)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACCIDENTES(ft):
  attr = ft.add("ACCIDENTES",34)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACCIDENTES')
  attr.setGroup(u'_Accidentes')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(True)
  attr.setIsTime(False)
  attr.setLabel(u'ACCIDENTES')
  attr.setOrder(40)
  attr.setPrecision(-1)
  attr.setReadOnly(True)
  attr.setRelationType(0)
  attr.setFeatureAttributeEmulator(u'SELECT * FROM ARENA2_ACCIDENTES WHERE ARENA2_INFORMES.COD_INFORME = ARENA2_ACCIDENTES.COD_INFORME;')
  tags = attr.getTags()
  tags.set(u'dynform.label.empty', u'True')
  tags.set(u'dal.relatedfeatures.table', u'ARENA2_ACCIDENTES')
  tags.set(u'dal.relatedfeatures.columns', u'ID_ACCIDENTE/FECHA_ACCIDENTE/COD_PROVINCIA/COD_MUNICIPIO/COD_POBLACION')
  tags.set(u'dal.relatedfeatures.unique.field.name', u'ID_ACCIDENTE')

def add_attributes_ARENA2_INFORMES(ft):
  add_attribute_LID_INFORME(ft)
  add_attribute_COD_INFORME(ft)
  add_attribute_FECHA_INI_EXPORT(ft)
  add_attribute_FECHA_FIN_EXPORT(ft)
  add_attribute_ACCIDENTES(ft)


def configurar_featuretype_ARENA2_INFORMES(ft):

  add_attributes_ARENA2_INFORMES(ft)

def crearTabla_ARENA2_INFORMES(connection):
  tableName = "ARENA2_INFORMES"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()
  configurar_featuretype_ARENA2_INFORMES(ft)

  server.add(tableName, params, False)

def main(*args):
    pass
