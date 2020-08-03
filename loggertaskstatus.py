# encoding: utf-8

import gvsig

from org.gvsig.tools.task import SimpleTaskStatus
from org.gvsig.app import ApplicationLocator
from java.lang import System

class LoggerTaskStatus(SimpleTaskStatus):
  def __init__(self, title):
    self.__title = title
    self.__message = None
    self.__curvalue  = 0
    self.__max = 0
    self.__min = 0
    self.__state = "init"
    application = ApplicationLocator.getApplicationManager()
    arguments = application.getArguments()
    self.__consolelogger = arguments.get("consolelogger",True)

  def __print(self):
    s = self.getLabel()
    self.logger(s)
    
  def logger(self, msg, mode=gvsig.LOGGER_INFO):
    gvsig.logger(msg)
    if not self.__consolelogger:
      print msg
  
  def getTitle(self):
    return self.__title
    
  def getCode(self):
    return None

  def getCompleted(self):
    return -1

  def getLabel(self):
    label = "[%03d/%03d][%s] %s/%s" % (
        self.__curvalue,
        self.__max,
        self.__state,
        self.__title,
        self.__message
      )
    return label
    
  def getMessage(self):
    return self.__message

  def isCancelled(self):
    return self.__state == "cancelled"

  def isAborted(self):
    return self.__state == "aborted"
    
  def isRunning(self):
    return self.__state == "running"
    
  def getLastModification(self):
    return None
    
  def getManager(self):
    return None
    
  def isIndeterminate(self):
    return self.__min == self.__max
    
  def isCancellable(self):
    return False

  def setTitle(self, title):
    self.__title = title
    self.__print()
  
  def message(self, message):
    self.__message = message
    self.__print()
    
  def setRangeOfValues(self, min, max):
    self.__min = min
    self.__max = max
    if self.__state == "init":
      self.__state = "running"
    self.__print()
    
  def setCurValue(self, value):
    self.__curvalue = value
    self.__state = "running"
    #self.__print()
    
  def incrementCurrentValue(self):
    self.__curvalue += 1
    self.__state = "running"
   # self.__print()
    
  def terminate(self):
    self.__state = "terminate"
    self.__print()

  def cancel(self):
    self.__state = "cancelled"
    self.__print()

  def abort(self):
    self.__state = "aborted"
    self.__print()

  def remove(self):
    return None

  def add(self):
    return None

  def setCancellable(self, cancellable):
    pass
    
  def setAutoremove(self, autoremove):
    pass

  def getAutoRemove(self):
    return True

  def setIndeterminate(self):
    return True

  def push(self):
    return None

  def pop(self):
    return None

  def restart(self):
    return None
    
def main(*args):
  status = LoggerTaskStatus("ARENA2")
  for n in range(10):
    status.logger("Test")
  pass
