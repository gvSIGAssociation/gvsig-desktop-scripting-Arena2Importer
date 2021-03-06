# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.tools.dynobject.DynField import RELATION_TYPE_COLLABORATION, RELATION_TYPE_AGGREGATE
from org.gvsig.tools.dataTypes import DataTypes

def add_attribute_LID_CROQUIS(ft):
  attr = ft.add("LID_CROQUIS",8)
  attr.setSize(30)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_CROQUIS')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(True)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Id_croquis')
  attr.setOrder(0)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ID_ACCIDENTE(ft):
  attr = ft.add("ID_ACCIDENTE",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_ACCIDENTE')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Accidente')
  attr.setOrder(10)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID_ACCIDENTE')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s',ID_ACCIDENTE)")
  attr.getForeingKey().setClosedList(False)
  attr.getForeingKey().setTableName(u'ARENA2_ACCIDENTES')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ID_CROQUIS(ft):
  attr = ft.add("ID_CROQUIS",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_CROQUIS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Codigo_croquis')
  attr.setOrder(20)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_IMAGEN(ft):
  attr = ft.add("IMAGEN",DataTypes.BYTEARRAY)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(u'Image')
  attr.setDescription(u'IMAGEN')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Imagen')
  attr.setOrder(30)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.height', u'300')
  
def add_attribute_EXTRA(ft):
  attr = ft.add("EXTRA", DataTypes.STRING)
  attr.setSize(10000)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'Extra')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Extra')
  attr.setOrder(2000)
  attr.setPrecision(-1)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  
def add_attributes_ARENA2_CROQUIS(ft):
  add_attribute_LID_CROQUIS(ft)
  add_attribute_ID_ACCIDENTE(ft)
  add_attribute_ID_CROQUIS(ft)
  add_attribute_IMAGEN(ft)
  add_attribute_EXTRA(ft)


def configurar_featuretype_ARENA2_CROQUIS(ft):
  tags = ft.getTags()
  tags.set(u'dynform.width', 500)

  add_attributes_ARENA2_CROQUIS(ft)

def crearTabla_ARENA2_CROQUIS(connection):
  tableName = "ARENA2_CROQUIS"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()
  configurar_featuretype_ARENA2_CROQUIS(ft)

  server.add(tableName, params, False)

def main(*args):
    pass
