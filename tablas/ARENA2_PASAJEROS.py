# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator
from org.gvsig.tools.dynobject.DynField import RELATION_TYPE_COLLABORATION, RELATION_TYPE_AGGREGATE
from org.gvsig.tools.dataTypes import DataTypes

def add_attribute_LID_PASAJERO(ft):
  attr = ft.add("LID_PASAJERO",8)
  attr.setSize(30)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_PASAJERO')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(True)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Id_pasajero')
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

def add_attribute_LID_VEHICULO(ft):
  attr = ft.add("LID_VEHICULO",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_VEHICULO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Vehiculo')
  attr.setOrder(20)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'LID_VEHICULO')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s/%s %s %s %s %s',ID_ACCIDENTE,ID_VEHICULO,TIPO_VEHICULO,NACIONALIDAD,MARCA_NOMBRE,MODELO)")
  attr.getForeingKey().setClosedList(False)
  attr.getForeingKey().setTableName(u'ARENA2_VEHICULOS')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ID_VEHICULO(ft):
  attr = ft.add("ID_VEHICULO",8)
  attr.setSize(5)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_VEHICULO')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Codigo_vehiculo')
  attr.setOrder(30)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ID_PASAJERO(ft):
  attr = ft.add("ID_PASAJERO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_PASAJERO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Codigo_pasajero')
  attr.setOrder(40)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_FECHA_NACIMIENTO(ft):
  attr = ft.add("FECHA_NACIMIENTO",9)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'FECHA_NACIMIENTO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Fecha_nacimiento')
  attr.setOrder(50)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_SEXO(ft):
  attr = ft.add("SEXO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SEXO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Sexo')
  attr.setOrder(60)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_SEXO')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_PAIS_RESIDENCIA(ft):
  attr = ft.add("PAIS_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PAIS_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Pais_de_residencia')
  attr.setOrder(70)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_PROVINCIA_RESIDENCIA(ft):
  attr = ft.add("PROVINCIA_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PROVINCIA_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Provincia_de_residencia')
  attr.setOrder(80)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_MUNICIPIO_RESIDENCIA(ft):
  attr = ft.add("MUNICIPIO_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'MUNICIPIO_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Municipio_de_residencia')
  attr.setOrder(90)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ASISTENCIA_SANITARIA(ft):
  attr = ft.add("ASISTENCIA_SANITARIA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ASISTENCIA_SANITARIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Asistencia_sanitaria')
  attr.setOrder(100)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ASISTENCIA_SANITARIA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_POSICION_VEHI(ft):
  attr = ft.add("POSICION_VEHI",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'POSICION_VEHI')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Posicion_en_el_vehiculo')
  attr.setOrder(110)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_POSICION_VEHICULO')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NINYO_EN_BRAZO(ft):
  attr = ft.add("NINYO_EN_BRAZO",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NINYO_EN_BRAZO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Ninyo_en_brazo')
  attr.setOrder(120)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_CINTURON(ft):
  attr = ft.add("ACC_SEG_CINTURON",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_CINTURON')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Cinturon')
  attr.setOrder(130)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_CASCO(ft):
  attr = ft.add("ACC_SEG_CASCO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_CASCO')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(True)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Casco')
  attr.setOrder(140)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(RELATION_TYPE_COLLABORATION)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ACC_SEG_CASCO')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_SIS_RETEN_INFANTIL(ft):
  attr = ft.add("ACC_SEG_SIS_RETEN_INFANTIL",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_SIS_RETEN_INFANTIL')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Sistema_retencion_infantil')
  attr.setOrder(150)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_BRAZOS(ft):
  attr = ft.add("ACC_SEG_BRAZOS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_BRAZOS')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Brazos')
  attr.setOrder(160)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Accesorios_de_seguridad_opcionales')

def add_attribute_ACC_SEG_ESPALDA(ft):
  attr = ft.add("ACC_SEG_ESPALDA",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_ESPALDA')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Espalda')
  attr.setOrder(170)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_TORSO(ft):
  attr = ft.add("ACC_SEG_TORSO",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_TORSO')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Torso')
  attr.setOrder(180)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_MANOS(ft):
  attr = ft.add("ACC_SEG_MANOS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_MANOS')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Manos')
  attr.setOrder(190)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_PIERNAS(ft):
  attr = ft.add("ACC_SEG_PIERNAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PIERNAS')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Piernas')
  attr.setOrder(200)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_PIES(ft):
  attr = ft.add("ACC_SEG_PIES",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PIES')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Pies')
  attr.setOrder(210)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ACC_SEG_PRENDA_REF(ft):
  attr = ft.add("ACC_SEG_PRENDA_REF",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PRENDA_REF')
  attr.setGroup(u'_Accesorios_de_seguridad')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Prenda_reflectante')
  attr.setOrder(220)
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
  
def add_attributes_ARENA2_PASAJEROS(ft):
  add_attribute_LID_PASAJERO(ft)
  add_attribute_ID_ACCIDENTE(ft)
  add_attribute_LID_VEHICULO(ft)
  add_attribute_ID_VEHICULO(ft)
  add_attribute_ID_PASAJERO(ft)
  add_attribute_FECHA_NACIMIENTO(ft)
  add_attribute_SEXO(ft)
  add_attribute_PAIS_RESIDENCIA(ft)
  add_attribute_PROVINCIA_RESIDENCIA(ft)
  add_attribute_MUNICIPIO_RESIDENCIA(ft)
  add_attribute_ASISTENCIA_SANITARIA(ft)
  add_attribute_POSICION_VEHI(ft)
  add_attribute_NINYO_EN_BRAZO(ft)
  add_attribute_ACC_SEG_CINTURON(ft)
  add_attribute_ACC_SEG_CASCO(ft)
  add_attribute_ACC_SEG_SIS_RETEN_INFANTIL(ft)
  add_attribute_ACC_SEG_BRAZOS(ft)
  add_attribute_ACC_SEG_ESPALDA(ft)
  add_attribute_ACC_SEG_TORSO(ft)
  add_attribute_ACC_SEG_MANOS(ft)
  add_attribute_ACC_SEG_PIERNAS(ft)
  add_attribute_ACC_SEG_PIES(ft)
  add_attribute_ACC_SEG_PRENDA_REF(ft)
  add_attribute_EXTRA(ft)

def configurar_featuretype_ARENA2_PASAJEROS(ft):
  tags = ft.getTags()
  tags.set(u'dynform.width', 500)

  add_attributes_ARENA2_PASAJEROS(ft)

def crearTabla_ARENA2_PASAJEROS(connection):
  tableName = "ARENA2_PASAJEROS"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()
  configurar_featuretype_ARENA2_PASAJEROS(ft)

  server.add(tableName, params, False)

def main(*args):
    pass
