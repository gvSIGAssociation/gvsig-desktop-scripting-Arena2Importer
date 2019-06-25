# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator

def crearTablaPeatones(connection):
  tableName = "ARENA2_PEATONES"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getExplorerName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()

  attr = ft.add("LID_PEATON",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_PEATON')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'LID_PEATON')
  attr.setMandatory(False)
  attr.setOrder(0)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Accidente')
  attr.setMandatory(False)
  attr.setOrder(10)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)
  attr.getForeingKey().setCodeName(None)
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(None)
  attr.getForeingKey().setSelectable(False)
  attr.getForeingKey().setTableName(None)

  attr = ft.add("ID_PEATON",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ID_PEATON')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Cod. peaton')
  attr.setMandatory(False)
  attr.setOrder(20)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Fecha nacimiento')
  attr.setMandatory(False)
  attr.setOrder(30)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(u'Date')

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Sexo')
  attr.setMandatory(False)
  attr.setOrder(40)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)
  attr.getForeingKey().setCodeName(None)
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(None)
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Pais de residencia')
  attr.setMandatory(False)
  attr.setOrder(50)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Provincia de residencia')
  attr.setMandatory(False)
  attr.setOrder(60)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Municipio de residencia')
  attr.setMandatory(False)
  attr.setOrder(70)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

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
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Asistencia sanitaria')
  attr.setMandatory(False)
  attr.setOrder(80)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)
  attr.getForeingKey().setCodeName(None)
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(None)
  attr.getForeingKey().setSelectable(True)
  attr.getForeingKey().setTableName(None)

  attr = ft.add("INFLU_ALCOHOL",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_ALCOHOL')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'INFLU_ALCOHOL')
  attr.setMandatory(False)
  attr.setOrder(90)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("PRUEBA_ALCOHOLEMIA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRUEBA_ALCOHOLEMIA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'PRUEBA_ALCOHOLEMIA')
  attr.setMandatory(False)
  attr.setOrder(100)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("TASA_ALCOHOLEMIA1",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TASA_ALCOHOLEMIA1')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'TASA_ALCOHOLEMIA1')
  attr.setMandatory(False)
  attr.setOrder(110)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("TASA_ALCOHOLEMIA2",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TASA_ALCOHOLEMIA2')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'TASA_ALCOHOLEMIA2')
  attr.setMandatory(False)
  attr.setOrder(120)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("PRUEBA_ALC_SANGRE",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRUEBA_ALC_SANGRE')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'PRUEBA_ALC_SANGRE')
  attr.setMandatory(False)
  attr.setOrder(130)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("SIGNOS_INFLU_ALCOHOL",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SIGNOS_INFLU_ALCOHOL')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'SIGNOS_INFLU_ALCOHOL')
  attr.setMandatory(False)
  attr.setOrder(140)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("INFLU_DROGAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_DROGAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'INFLU_DROGAS')
  attr.setMandatory(False)
  attr.setOrder(150)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("PRUEBA_DROGAS",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(u'DAL.SelectableForeingKey')
  attr.setDescription(u'PRUEBA_DROGAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'Prueba drogas')
  attr.setMandatory(False)
  attr.setOrder(160)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("AMP",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'AMP')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'AMP')
  attr.setMandatory(False)
  attr.setOrder(170)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_AMP",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_AMP')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_AMP')
  attr.setMandatory(False)
  attr.setOrder(180)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("BDZ",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'BDZ')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'BDZ')
  attr.setMandatory(False)
  attr.setOrder(190)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_BDZ",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_BDZ')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_BDZ')
  attr.setMandatory(False)
  attr.setOrder(200)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("COC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'COC')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'COC')
  attr.setMandatory(False)
  attr.setOrder(210)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_COC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_COC')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_COC')
  attr.setMandatory(False)
  attr.setOrder(220)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("THC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'THC')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'THC')
  attr.setMandatory(False)
  attr.setOrder(230)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_THC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_THC')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_THC')
  attr.setMandatory(False)
  attr.setOrder(240)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("METH",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'METH')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'METH')
  attr.setMandatory(False)
  attr.setOrder(250)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_METH",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_METH')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_METH')
  attr.setMandatory(False)
  attr.setOrder(260)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("OPI",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'OPI')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'OPI')
  attr.setMandatory(False)
  attr.setOrder(270)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_OPI",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_OPI')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_OPI')
  attr.setMandatory(False)
  attr.setOrder(280)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("OTRAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'OTRAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'OTRAS')
  attr.setMandatory(False)
  attr.setOrder(290)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("CONFIRMADO_OTRAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_OTRAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'CONFIRMADO_OTRAS')
  attr.setMandatory(False)
  attr.setOrder(300)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("SIGNOS_INFLU_DROGAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SIGNOS_INFLU_DROGAS')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'SIGNOS_INFLU_DROGAS')
  attr.setMandatory(False)
  attr.setOrder(310)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("MOTIVO_DESPLAZAMIENTO",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'MOTIVO_DESPLAZAMIENTO')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'MOTIVO_DESPLAZAMIENTO')
  attr.setMandatory(False)
  attr.setOrder(320)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("ACCION_PEA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'ACCION_PEA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'ACCION_PEA')
  attr.setMandatory(False)
  attr.setOrder(330)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("INFLU_PRES_INFRAC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_PRES_INFRAC')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'INFLU_PRES_INFRAC')
  attr.setMandatory(False)
  attr.setOrder(340)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("PRES_INFRAC_PEA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRES_INFRAC_PEA')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'PRES_INFRAC_PEA')
  attr.setMandatory(False)
  attr.setOrder(350)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("POSIBLE_RESPONSABLE",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'POSIBLE_RESPONSABLE')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'POSIBLE_RESPONSABLE')
  attr.setMandatory(False)
  attr.setOrder(360)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("INFLU_FACT_ATENCION",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_FACT_ATENCION')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'INFLU_FACT_ATENCION')
  attr.setMandatory(False)
  attr.setOrder(370)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("FACTORES_ATENCION",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'FACTORES_ATENCION')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'FACTORES_ATENCION')
  attr.setMandatory(False)
  attr.setOrder(380)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("INFLU_PRES_ERROR",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_PRES_ERROR')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'INFLU_PRES_ERROR')
  attr.setMandatory(False)
  attr.setOrder(390)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)

  attr = ft.add("PRESUNTOS_ERRORES",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRESUNTOS_ERRORES')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setPersistent(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'PRESUNTOS_ERRORES')
  attr.setMandatory(False)
  attr.setOrder(400)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.setSubtype(None)
  
  server.add(tableName, params, False)

def main(*args):
    pass