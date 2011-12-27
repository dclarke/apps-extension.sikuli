import os
import subprocess
import platform

def system(): 
  system = java.lang.System.getProperty( "os.name" )
  print system
  if system.find('Mac') >= 0:
    return macbox()
  elif system.find('Windows') >= 0:
    return winbox()
  elif system.find('Linux') >= 0:
    return linbox()
  else:
    return None


class box():
  def __init__(self):
    self.mach = "unknown"

  def images(self,filename):
    directory = 'images/' + self.mach + '/'
    print directory
    if (os.path.isfile(Path + directory + filename)):
      return directory+filename
    else:
      return Path + 'images/' +filename

class macbox(box):
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "mac"
  def nativediropen(self):
    subprocess.call(["open", self.home])
  def nativedirdeleteapps(self):
    subprocess.call(["rm", "-rf", self.home])
      
class winbox(box):
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "windows"

class linuxbox(box):
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "linux"
