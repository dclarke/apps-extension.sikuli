import os
import subprocess
import platform

# @author David Clarke
# @version .1

def system(): 
  # A call to the system() function anywhere should return an object 
  # that is tailored to return operating system dependent data 
  # 
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
  # A MacBox object will contain functions that are mac specific
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "mac"
  def nativediropen(self):
    #nativediropen: will open the directory where the native application is installed
    #this can be used in conjunction with the vision processing inside sikuli to verify 
    #an application was installed
    subprocess.call(["open", self.home])
  def nativedirdeleteapps(self):
    #nativedirdeleteapps will delete all the apps in the binary installed application

    subprocess.call(["rm", "-rf", self.home])
      
class winbox(box):
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "windows"
  
  def images(self,filename):
    #images is custom for windows because their slashes are always the wrong way
    #essence is to return all the images
    directory = 'images\' + self.mach + '\'
    print directory
    if (os.path.isfile(Path + directory + filename)):
      return directory+filename
    else:
      return Path + 'images\' +filename
  def nativediropen(self):
    #unimplemented in windows
    return 0     
  def nativedirdeleteapps(self):
    #unimplemented in windows
    return 0

class linuxbox(box):
    #linuxbox is currently untested, but will need to be filled in when appropriate 
  def __init__(self):
    self.home = os.path.expanduser("~") + "/Applications/"
    self.mach = "linux"
