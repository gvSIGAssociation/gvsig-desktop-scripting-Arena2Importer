# encoding: utf-8

import gvsig


from addons.Arena2Importer import Arena2ImportLocator 
from addons.Arena2Importer import actions 

def main(*args):
  Arena2ImportLocator.selfRegister()
  actions.selfRegister()
  
