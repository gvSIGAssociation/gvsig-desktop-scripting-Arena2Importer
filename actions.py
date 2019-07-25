# encoding: utf-8

import gvsig
from gvsig import getResource

from java.io import File
from org.gvsig.andami import PluginsLocator
from org.gvsig.app import ApplicationLocator
from org.gvsig.scripting.app.extension import ScriptingExtension
from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.swing.api import ToolsSwingLocator

from addons.Arena2Importer.Arena2ImportLocator import getArena2ImportManager

class Arena2ImporterExtension(ScriptingExtension):
  def __init__(self):
    pass

  def canQueryByAction(self):
    return False

  def isEnabled(self,action=None):
    return True

  def isVisible(self,action=None):
    return True
    
  def execute(self,actionCommand, *args):
    actionCommand = actionCommand.lower()
    if actionCommand == "arena2-importer-showimporter":
      self.importData()
    elif actionCommand == "arena2-importer-showtablecreator":
      self.createTables()
        
  def createTables(self):
    manager = getArena2ImportManager()
    dialog = manager.createTablestDialog()
    dialog.showWindow("ARENA2 Crear tablas de accidentes")

  def importData(self):
    manager = getArena2ImportManager()
    dialog = manager.createImportDialog()
    dialog.arena2filePicker.coerceAndSet(
      getResource(__file__,"..","Arena2Reader","datos", "test","TV_03_2019_01_Q1","victimas.xml")
    )
    dialog.showWindow("ARENA2 Importar accidentes")
    
def selfRegister():
  application = ApplicationLocator.getManager()

  #
  # Registramos las traducciones
  i18n = ToolsLocator.getI18nManager()
  i18n.addResourceFamily("text",File(getResource(__file__,"i18n")))

  #
  # Registramos los iconos en el tema de iconos
  iconTheme = ToolsSwingLocator.getIconThemeManager().getCurrent()
  icon = File(getResource(__file__,"images","arena2-importer-showimporter.png")).toURI().toURL()
  iconTheme.registerDefault("scripting.Arena2ImporterExtension", "action", "arena2-importer-showimporter", None, icon)
  icon = File(getResource(__file__,"images","arena2-importer-showtablecreator.png")).toURI().toURL()
  iconTheme.registerDefault("scripting.Arena2ImporterExtension", "action", "arena2-importer-showtablecreator", None, icon)

  #
  # Creamos la accion 
  actionManager = PluginsLocator.getActionInfoManager()
  extension = Arena2ImporterExtension()
  
  action = actionManager.createAction(
    extension, 
    "arena2-importer-showimporter", # Action name
    "ARENA2 importardor", # Text
    "arena2-importer-showimporter", # Action command
    "arena2-importer-showimporter", # Icon name
    None, # Accelerator
    650700600, # Position 
    "_Show_the_ARENA2_import_tool" # Tooltip
  )
  action = actionManager.registerAction(action)
  application.addMenu(action, "tools/ARENA2/Importador")
  
  action = actionManager.createAction(
    extension, 
    "arena2-importer-showtablecreator", # Action name
    "ARENA2 Creador de tablas", # Text
    "arena2-importer-showtablecreator", # Action command
    "arena2-importer-showtablecreator", # Icon name
    None, # Accelerator
    650700600, # Position 
    "_Show_the_ARENA2_tables_creator_tool" # Tooltip
  )
  action = actionManager.registerAction(action)
  application.addMenu(action, "tools/ARENA2/Crear tablas")
