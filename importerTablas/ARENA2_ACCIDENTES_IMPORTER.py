# encoding: utf-8

import gvsig
from org.gvsig.tools.dynobject.DynField import RELATION_TYPE_COLLABORATION, RELATION_TYPE_AGGREGATE
from org.gvsig.tools.dataTypes import DataTypes

def add_attribute_CARRETERA_DGT(ft):
  attr = ft.add("CARRETERA_DGT",8)
  attr.setSize(50)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CARRETERA_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Carretera_original_DGT')
  attr.setOrder(120)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'3')
  
def add_attribute_KM_DGT(ft):
  attr = ft.add("KM_DGT",7)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'KM_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Punto_kilometrico_DGT')
  attr.setOrder(130)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'4')



def add_attribute_TITULARIDAD_VIA_DGT(ft):
  attr = ft.add("TITULARIDAD_VIA_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TITULARIDAD_VIA_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Titularidad_de_la_via_original_DGT')
  attr.setOrder(150)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_TITULARIDAD_VIA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TIPO_VIA_DGT(ft):
  attr = ft.add("TIPO_VIA_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TIPO_VIA_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Tipo_de_via_original_DGT')
  attr.setOrder(100)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_TIPO_VIA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_COD_ESTACION_AFORO(ft):
  attr = ft.add("COD_ESTACION_AFORO",DataTypes.STRING)
  attr.setSize(40)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'COD_ESTACION_AFORO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Cod_Estacion_Aforo')
  attr.setOrder(0)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  
def add_attribute_COD_AFORO(ft):
  attr = ft.add("COD_AFORO",8)
  attr.setSize(40)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'COD_AFORO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Codigo_aforo')
  attr.setOrder(10)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'COD_AFORO')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s',COD_AFORO)")
  attr.getForeingKey().setClosedList(False)
  attr.getForeingKey().setTableName(u'AFOROS_MEDIDAS')
  #tags = attr.getTags()
  #tags.set(u'dynform.readonly', u'True')
  
def add_attribute_ACTUALIZADO(ft):
  attr = ft.add("ACTUALIZADO",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACTUALIZADO')
  attr.setGroup(u'_Importacion')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Dato_actualizado')
  attr.setOrder(1810)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setDefaultValue(False)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TOTAL_VICTIMAS_DGT(ft):
  attr = ft.add("TOTAL_VICTIMAS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_VICTIMAS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_victimas_DGT')
  attr.setOrder(270)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TOTAL_MUERTOS_DGT(ft):
  attr = ft.add("TOTAL_MUERTOS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_MUERTOS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_muertos_DGT')
  attr.setOrder(280)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'10')

def add_attribute_TOTAL_GRAVES_DGT(ft):
  attr = ft.add("TOTAL_GRAVES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_GRAVES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_graves_DGT')
  attr.setOrder(290)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'11')

def add_attribute_TOTAL_LEVES_DGT(ft):
  attr = ft.add("TOTAL_LEVES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_LEVES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_Leves_DGT')
  attr.setOrder(300)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'12')

def add_attribute_TOTAL_ILESOS_DGT(ft):
  attr = ft.add("TOTAL_ILESOS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_ILESOS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_ilesos_DGT')
  attr.setOrder(310)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TOTAL_VEHICULOS_DGT(ft):
  attr = ft.add("TOTAL_VEHICULOS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_VEHICULOS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_vehiculos_implicados_DGT')
  attr.setOrder(320)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dal.search.attribute.priority', u'13')

def add_attribute_TOTAL_CONDUCTORES_DGT(ft):
  attr = ft.add("TOTAL_CONDUCTORES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_CONDUCTORES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_conductores_implicados_DGT')
  attr.setOrder(330)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TOTAL_PASAJEROS_DGT(ft):
  attr = ft.add("TOTAL_PASAJEROS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_PASAJEROS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_pasajeros_implicados_DGT')
  attr.setOrder(340)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TOTAL_PEATONES_DGT(ft):
  attr = ft.add("TOTAL_PEATONES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TOTAL_PEATONES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Total_peatones_implicados_DGT')
  attr.setOrder(350)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_TURISMOS_DGT(ft):
  attr = ft.add("NUM_TURISMOS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_TURISMOS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_turismos_implicados_DGT')
  attr.setOrder(360)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_FURGONETAS_DGT(ft):
  attr = ft.add("NUM_FURGONETAS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_FURGONETAS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_furgonetas_implicadas_DGT')
  attr.setOrder(370)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_CAMIONES_DGT(ft):
  attr = ft.add("NUM_CAMIONES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_CAMIONES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_camiones_implicados_DGT')
  attr.setOrder(380)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_AUTOBUSES_DGT(ft):
  attr = ft.add("NUM_AUTOBUSES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_AUTOBUSES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_autobuses_implicados_DGT')
  attr.setOrder(390)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_CICLOMOTORES_DGT(ft):
  attr = ft.add("NUM_CICLOMOTORES_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_CICLOMOTORES_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_ciclomotores_implicados_DGT')
  attr.setOrder(400)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_MOTOCICLETAS_DGT(ft):
  attr = ft.add("NUM_MOTOCICLETAS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_MOTOCICLETAS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_motocicletas_implicadas_DGT')
  attr.setOrder(410)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_BICICLETAS_DGT(ft):
  attr = ft.add("NUM_BICICLETAS_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_BICICLETAS_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_bicicletas_implicadas_DGT')
  attr.setOrder(420)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NUM_OTROS_VEHI_DGT(ft):
  attr = ft.add("NUM_OTROS_VEHI_DGT",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NUM_OTROS_VEHI_DGT')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Num_otros_vehiculos_implicados_DGT')
  attr.setOrder(430)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

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
  
def add_import_attr_ARENA2_ACCIDENTES(ft):
  add_attribute_COD_AFORO(ft)
  add_attribute_COD_ESTACION_AFORO(ft)
  add_attribute_TIPO_VIA_DGT(ft)
  add_attribute_CARRETERA_DGT(ft)
  add_attribute_KM_DGT(ft)
  add_attribute_TITULARIDAD_VIA_DGT(ft)
  add_attribute_TOTAL_VICTIMAS_DGT(ft)
  add_attribute_TOTAL_MUERTOS_DGT(ft)
  add_attribute_TOTAL_GRAVES_DGT(ft)
  add_attribute_TOTAL_LEVES_DGT(ft)
  add_attribute_TOTAL_ILESOS_DGT(ft)
  add_attribute_TOTAL_VEHICULOS_DGT(ft)
  add_attribute_TOTAL_CONDUCTORES_DGT(ft)
  add_attribute_TOTAL_PASAJEROS_DGT(ft)
  add_attribute_TOTAL_PEATONES_DGT(ft)
  add_attribute_NUM_TURISMOS_DGT(ft)
  add_attribute_NUM_FURGONETAS_DGT(ft)
  add_attribute_NUM_CAMIONES_DGT(ft)
  add_attribute_NUM_AUTOBUSES_DGT(ft)
  add_attribute_NUM_CICLOMOTORES_DGT(ft)
  add_attribute_NUM_MOTOCICLETAS_DGT(ft)
  add_attribute_NUM_BICICLETAS_DGT(ft)
  add_attribute_NUM_OTROS_VEHI_DGT(ft)
  
  add_attribute_ACTUALIZADO(ft)
  add_attribute_EXTRA(ft)

def main(*args):
  import gvsig
  ft = gvsig.createFeatureType()
  add_import_attr_ARENA2_ACCIDENTES(ft)
  print ft