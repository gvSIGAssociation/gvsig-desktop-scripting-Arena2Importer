# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator

def add_attribute_LID_PASAJERO(ft):
  attr = ft.add("LID_PASAJERO",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_PASAJERO')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(True)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'LID_PASAJERO')
  #attr.setMandatory(True)
  attr.setOrder(0)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ID_ACCIDENTE(ft):
  attr = ft.add("ID_ACCIDENTE",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_ACCIDENTE')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Accidente')
  #attr.setMandatory(False)
  attr.setOrder(10)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'ID_ACCIDENTE')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s',ID_ACCIDENTE)")
  attr.getForeingKey().setSelectable(False)
  attr.getForeingKey().setTableName(u'ARENA2_ACCIDENTES')

def add_attribute_LID_VEHICULO(ft):
  attr = ft.add("LID_VEHICULO",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_VEHICULO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Vehiculo')
  #attr.setMandatory(False)
  attr.setOrder(20)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'LID_VEHICULO')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s/%s %s %s %s %s',ID_ACCIDENTE,ID_VEHICULO,TIPO_VEHICULO,NACIONALIDAD,MARCA_NOMBRE,MODELO)")
  attr.getForeingKey().setSelectable(False)
  attr.getForeingKey().setTableName(u'ARENA2_VEHICULOS')

def add_attribute_ID_VEHICULO(ft):
  attr = ft.add("ID_VEHICULO",8)
  attr.setSize(5)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_VEHICULO')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'ID_VEHICULO')
  #attr.setMandatory(False)
  attr.setOrder(30)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ID_PASAJERO(ft):
  attr = ft.add("ID_PASAJERO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_PASAJERO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Cod.pasajero')
  #attr.setMandatory(False)
  attr.setOrder(40)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_FECHA_NACIMIENTO(ft):
  attr = ft.add("FECHA_NACIMIENTO",9)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'FECHA_NACIMIENTO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Fecha nacimiento')
  #attr.setMandatory(False)
  attr.setOrder(50)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(u'Date')

def add_attribute_SEXO(ft):
  attr = ft.add("SEXO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SEXO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Sexo')
  #attr.setMandatory(False)
  attr.setOrder(60)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_SEXO')

def add_attribute_PAIS_RESIDENCIA(ft):
  attr = ft.add("PAIS_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PAIS_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Pais de residencia')
  #attr.setMandatory(False)
  attr.setOrder(70)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_PROVINCIA_RESIDENCIA(ft):
  attr = ft.add("PROVINCIA_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PROVINCIA_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Provincia de residencia')
  #attr.setMandatory(False)
  attr.setOrder(80)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_MUNICIPIO_RESIDENCIA(ft):
  attr = ft.add("MUNICIPIO_RESIDENCIA",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'MUNICIPIO_RESIDENCIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Municipio de residencia')
  #attr.setMandatory(False)
  attr.setOrder(90)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ASISTENCIA_SANITARIA(ft):
  attr = ft.add("ASISTENCIA_SANITARIA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ASISTENCIA_SANITARIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Asistencia sanitaria')
  #attr.setMandatory(False)
  attr.setOrder(100)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ASISTENCIA_SANITARIA')

def add_attribute_ACC_SEG_CINTURON(ft):
  attr = ft.add("ACC_SEG_CINTURON",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_CINTURON')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Cinturon')
  #attr.setMandatory(False)
  attr.setOrder(110)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_CASCO(ft):
  attr = ft.add("ACC_SEG_CASCO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_CASCO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Casco')
  #attr.setMandatory(False)
  attr.setOrder(120)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ACC_SEG_CASCO')

def add_attribute_ACC_SEG_BRAZOS(ft):
  attr = ft.add("ACC_SEG_BRAZOS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_BRAZOS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Brazos')
  #attr.setMandatory(False)
  attr.setOrder(130)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_ESPALDA(ft):
  attr = ft.add("ACC_SEG_ESPALDA",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_ESPALDA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Espalda')
  #attr.setMandatory(False)
  attr.setOrder(140)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_TORSO(ft):
  attr = ft.add("ACC_SEG_TORSO",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_TORSO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Torso')
  #attr.setMandatory(False)
  attr.setOrder(150)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_MANOS(ft):
  attr = ft.add("ACC_SEG_MANOS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_MANOS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Manos')
  #attr.setMandatory(False)
  attr.setOrder(160)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_PIERNAS(ft):
  attr = ft.add("ACC_SEG_PIERNAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PIERNAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Piernas')
  #attr.setMandatory(False)
  attr.setOrder(170)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_PIES(ft):
  attr = ft.add("ACC_SEG_PIES",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PIES')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Pies')
  #attr.setMandatory(False)
  attr.setOrder(180)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_ACC_SEG_PRENDA_REF(ft):
  attr = ft.add("ACC_SEG_PRENDA_REF",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACC_SEG_PRENDA_REF')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'ACC_SEG_PRENDA_REF')
  #attr.setMandatory(False)
  attr.setOrder(190)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

def add_attribute_POSICION_VEHI(ft):
  attr = ft.add("POSICION_VEHI",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'POSICION_VEHI')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Posicion en el vehiculo')
  #attr.setMandatory(False)
  attr.setOrder(200)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_POSICION_VEHICULO')

def add_attribute_NINYO_EN_BRAZO(ft):
  attr = ft.add("NINYO_EN_BRAZO",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NINYO_EN_BRAZO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  #attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Ni\xf1o en brazo')
  #attr.setMandatory(False)
  attr.setOrder(210)
  attr.setPrecision(0)
  #attr.setReadOnly(False)
  attr.setRelationType(0)
  #attr.setSubtype(None)

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
  add_attribute_ACC_SEG_CINTURON(ft)
  add_attribute_ACC_SEG_CASCO(ft)
  add_attribute_ACC_SEG_BRAZOS(ft)
  add_attribute_ACC_SEG_ESPALDA(ft)
  add_attribute_ACC_SEG_TORSO(ft)
  add_attribute_ACC_SEG_MANOS(ft)
  add_attribute_ACC_SEG_PIERNAS(ft)
  add_attribute_ACC_SEG_PIES(ft)
  add_attribute_ACC_SEG_PRENDA_REF(ft)
  add_attribute_POSICION_VEHI(ft)
  add_attribute_NINYO_EN_BRAZO(ft)


def crearTabla_ARENA2_PASAJEROS(connection):
  tableName = "ARENA2_PASAJEROS"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()

  add_attributes_ARENA2_PASAJEROS(ft)
  
  server.add(tableName, params, False)

def main(*args):
    pass
