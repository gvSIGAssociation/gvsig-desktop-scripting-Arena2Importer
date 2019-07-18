# encoding: utf-8

import gvsig

from org.gvsig.fmap.dal import DALLocator

def add_attribute_LID_PEATON(ft):
  attr = ft.add("LID_PEATON",8)
  attr.setSize(20)
  attr.setAllowIndexDuplicateds(True)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'LID_PEATON')
  attr.setGroup(None)
  attr.setHidden(True)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(True)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Id_peaton')
  attr.setOrder(0)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Accidente')
  attr.setOrder(10)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID_ACCIDENTE')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%s',ID_ACCIDENTE)")
  attr.getForeingKey().setClosedList(False)
  attr.getForeingKey().setTableName(u'ARENA2_ACCIDENTES')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_ID_PEATON(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Codigo_peaton')
  attr.setOrder(20)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_POSIBLE_RESPONSABLE(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Posible_responsable')
  attr.setOrder(30)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Fecha_nacimiento')
  attr.setOrder(40)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Datos_personales')

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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Sexo')
  attr.setOrder(50)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_SEXO')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_NACIONALIDAD(ft):
  attr = ft.add("NACIONALIDAD",8)
  attr.setSize(100)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'NACIONALIDAD')
  attr.setGroup(None)
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Nacionalidad')
  attr.setOrder(60)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Asistencia_sanitaria')
  attr.setOrder(100)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ASISTENCIA_SANITARIA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_INFLU_FACT_ATENCION(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Influyen_factores_atencion')
  attr.setOrder(110)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Posibles_errores')

def add_attribute_FACTORES_ATENCION(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Factores_afectan_atencion')
  attr.setOrder(120)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_FACTORES_ATENCION_PEA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_INFLU_PRES_ERROR(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Influyen_presuntos_errores')
  attr.setOrder(130)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_PRESUNTOS_ERRORES(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Presuntos_errores')
  attr.setOrder(140)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ERRORES_PEA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_INFLU_PRES_INFRAC(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Influyen_presunta_infraccion')
  attr.setOrder(150)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_PRES_INFRAC_PEA(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Presunta_infraccion')
  attr.setOrder(160)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_INFRACCIONES_PEATON')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_MOTIVO_DESPLAZAMIENTO(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Motivo_desplazamiento')
  attr.setOrder(170)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_MOTIVO_DESPLAZA_PEA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Desplazamiento')

def add_attribute_ACCION_PEA(ft):
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
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Accion_del_peaton')
  attr.setOrder(180)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_ACCION_PEA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_INFLU_ALCOHOL(ft):
  attr = ft.add("INFLU_ALCOHOL",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_ALCOHOL')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Influye_el_alcohol')
  attr.setOrder(190)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Prueba_de_alcohol')

def add_attribute_PRUEBA_ALCOHOLEMIA(ft):
  attr = ft.add("PRUEBA_ALCOHOLEMIA",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRUEBA_ALCOHOLEMIA')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Prueba_en_aire')
  attr.setOrder(200)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_PRUEBA_ALCOHOLEMIA')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TASA_ALCOHOLEMIA1(ft):
  attr = ft.add("TASA_ALCOHOLEMIA1",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TASA_ALCOHOLEMIA1')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Tasa_1_en_aire_mg_l')
  attr.setOrder(210)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_TASA_ALCOHOLEMIA2(ft):
  attr = ft.add("TASA_ALCOHOLEMIA2",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'TASA_ALCOHOLEMIA2')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Tasa_2_en_aire_mg_l')
  attr.setOrder(220)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_PRUEBA_ALC_SANGRE(ft):
  attr = ft.add("PRUEBA_ALC_SANGRE",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRUEBA_ALC_SANGRE')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Prueba_en_sangre')
  attr.setOrder(230)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_SIGNOS_INFLU_ALCOHOL(ft):
  attr = ft.add("SIGNOS_INFLU_ALCOHOL",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SIGNOS_INFLU_ALCOHOL')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Signos_de_influencia_del_alcohol')
  attr.setOrder(240)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_INFLU_DROGAS(ft):
  attr = ft.add("INFLU_DROGAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'INFLU_DROGAS')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Influyen_las_drogas')
  attr.setOrder(250)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')
  tags.set(u'dynform.separator', u'_Prueba_de_drogas')

def add_attribute_PRUEBA_DROGAS(ft):
  attr = ft.add("PRUEBA_DROGAS",4)
  attr.setSize(10)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'PRUEBA_DROGAS')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Prueba_de_drogas')
  attr.setOrder(260)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  attr.getForeingKey().setCodeName(u'ID')
  attr.getForeingKey().setForeingKey(True)
  attr.getForeingKey().setLabelFormula(u"FORMAT('%02d - %s',ID,DESCRIPCION)")
  attr.getForeingKey().setClosedList(True)
  attr.getForeingKey().setTableName(u'ARENA2_DIC_PRUEBA_DROGAS')
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_AMP(ft):
  attr = ft.add("AMP",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'AMP')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_anfetaminas')
  attr.setOrder(270)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_AMP(ft):
  attr = ft.add("CONFIRMADO_AMP",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_AMP')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_anfetaminas')
  attr.setOrder(280)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_BDZ(ft):
  attr = ft.add("BDZ",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'BDZ')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_benzodiacepinas')
  attr.setOrder(290)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_BDZ(ft):
  attr = ft.add("CONFIRMADO_BDZ",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_BDZ')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_benzodiacepinas')
  attr.setOrder(300)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_COC(ft):
  attr = ft.add("COC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'COC')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_cocaina')
  attr.setOrder(310)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_COC(ft):
  attr = ft.add("CONFIRMADO_COC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_COC')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_cocaina')
  attr.setOrder(320)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_THC(ft):
  attr = ft.add("THC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'THC')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_cannabis_y_derivados')
  attr.setOrder(330)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_THC(ft):
  attr = ft.add("CONFIRMADO_THC",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_THC')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_cannabis_y_derivados')
  attr.setOrder(340)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_METH(ft):
  attr = ft.add("METH",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'METH')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_metanfetaminas')
  attr.setOrder(350)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_METH(ft):
  attr = ft.add("CONFIRMADO_METH",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_METH')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_metanfetaminas')
  attr.setOrder(360)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_OPI(ft):
  attr = ft.add("OPI",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'OPI')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_opiaceos')
  attr.setOrder(370)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_OPI(ft):
  attr = ft.add("CONFIRMADO_OPI",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_OPI')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_opiaceos')
  attr.setOrder(380)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_OTRAS(ft):
  attr = ft.add("OTRAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'OTRAS')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Positivo_benzodiacepinas')
  attr.setOrder(390)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_CONFIRMADO_OTRAS(ft):
  attr = ft.add("CONFIRMADO_OTRAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'CONFIRMADO_OTRAS')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Confirmado_otra_sustancias')
  attr.setOrder(400)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attribute_SIGNOS_INFLU_DROGAS(ft):
  attr = ft.add("SIGNOS_INFLU_DROGAS",1)
  attr.setSize(0)
  attr.setAllowIndexDuplicateds(False)
  attr.setAllowNull(True)
  attr.setDataProfileName(None)
  attr.setDescription(u'SIGNOS_INFLU_DROGAS')
  attr.setGroup(u'_Pruebas')
  attr.setHidden(False)
  attr.setIsAutomatic(False)
  attr.setIsIndexAscending(True)
  attr.setIsIndexed(False)
  attr.setIsPrimaryKey(False)
  attr.setIsReadOnly(False)
  attr.setIsTime(False)
  attr.setLabel(u'_Signos_de_influencia_de_drogas')
  attr.setOrder(410)
  attr.setPrecision(0)
  attr.setReadOnly(False)
  attr.setRelationType(0)
  tags = attr.getTags()
  tags.set(u'dynform.readonly', u'True')

def add_attributes_ARENA2_PEATONES(ft):
  add_attribute_LID_PEATON(ft)
  add_attribute_ID_ACCIDENTE(ft)
  add_attribute_ID_PEATON(ft)
  add_attribute_POSIBLE_RESPONSABLE(ft)
  add_attribute_FECHA_NACIMIENTO(ft)
  add_attribute_SEXO(ft)
  add_attribute_NACIONALIDAD(ft)
  add_attribute_PAIS_RESIDENCIA(ft)
  add_attribute_PROVINCIA_RESIDENCIA(ft)
  add_attribute_MUNICIPIO_RESIDENCIA(ft)
  add_attribute_ASISTENCIA_SANITARIA(ft)
  add_attribute_INFLU_FACT_ATENCION(ft)
  add_attribute_FACTORES_ATENCION(ft)
  add_attribute_INFLU_PRES_ERROR(ft)
  add_attribute_PRESUNTOS_ERRORES(ft)
  add_attribute_INFLU_PRES_INFRAC(ft)
  add_attribute_PRES_INFRAC_PEA(ft)
  add_attribute_MOTIVO_DESPLAZAMIENTO(ft)
  add_attribute_ACCION_PEA(ft)
  add_attribute_INFLU_ALCOHOL(ft)
  add_attribute_PRUEBA_ALCOHOLEMIA(ft)
  add_attribute_TASA_ALCOHOLEMIA1(ft)
  add_attribute_TASA_ALCOHOLEMIA2(ft)
  add_attribute_PRUEBA_ALC_SANGRE(ft)
  add_attribute_SIGNOS_INFLU_ALCOHOL(ft)
  add_attribute_INFLU_DROGAS(ft)
  add_attribute_PRUEBA_DROGAS(ft)
  add_attribute_AMP(ft)
  add_attribute_CONFIRMADO_AMP(ft)
  add_attribute_BDZ(ft)
  add_attribute_CONFIRMADO_BDZ(ft)
  add_attribute_COC(ft)
  add_attribute_CONFIRMADO_COC(ft)
  add_attribute_THC(ft)
  add_attribute_CONFIRMADO_THC(ft)
  add_attribute_METH(ft)
  add_attribute_CONFIRMADO_METH(ft)
  add_attribute_OPI(ft)
  add_attribute_CONFIRMADO_OPI(ft)
  add_attribute_OTRAS(ft)
  add_attribute_CONFIRMADO_OTRAS(ft)
  add_attribute_SIGNOS_INFLU_DROGAS(ft)


def configurar_featuretype_ARENA2_PEATONES(ft):
  tags = ft.getTags()
  tags.set(u'dynform.width', 500)

  add_attributes_ARENA2_PEATONES(ft)

def crearTabla_ARENA2_PEATONES(connection):
  tableName = "ARENA2_PEATONES"
  dataManager = DALLocator.getDataManager()
  server = dataManager.openServerExplorer(
      connection.getProviderName(),
      connection
  )
  params = server.getAddParameters(tableName)
  ft = params.getDefaultFeatureType()
  configurar_featuretype_ARENA2_PEATONES(ft)
  
  server.add(tableName, params, False)

def main(*args):
    pass
