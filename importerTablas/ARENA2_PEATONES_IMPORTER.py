# encoding: utf-8

import gvsig
from org.gvsig.tools.dynobject.DynField import RELATION_TYPE_COLLABORATION, RELATION_TYPE_AGGREGATE
from org.gvsig.tools.dataTypes import DataTypes


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
  
def add_import_attr_ARENA2_PEATONES(ft):
  add_attribute_EXTRA(ft)

def main(*args):
  import gvsig
  ft = gvsig.createFeatureType()
  add_import_attr_ARENA2_PEATONES(ft)
  print ft