from pprint import pprint

class AppDir:
  #An AppDir object is an object representation of https://apps.mozillalabs.com/appdir
  #The purpose of the object is to be able to dissect the page and determine what is installed
  def __init__(self,app):
    #AppDir constructor sets the page url, and takes an application object.  
    #Currently we just have a Firefox app object
    #But it allows for the AppDir to make calls into the firefox application to make sure
    #that the correct page is loaded, the browser is focused..etc.
    self.app = app
    self.url = "https://apps.mozillalabs.com/appdir"
    self.applications = list()
    self.installedapps = list()

  def page_loaded(self):
    #Waits for the main image on the page to load before returning
    wait(system().images("demoapps.png"))
    wait(system().images("appsvisible.png"))

  def installable_apps(self):
    self.applications = list()
    #Find all the apps that are not installed
    install_icons = list(findAll(system().images("Install.png")))
    for icon in install_icons:
      tempApp = AppObject()
      tempApp.topleft("Install Button",icon)
      self.applications.append(tempApp)
    self.applications = sorted(self.applications,key=attrgetter('y','x'))
    return self.applications

  def installed_apps(self):
    #Finds alls the apps that are currently installed
    installed_icons = None
    self.installedapps = list()
    try: 
      installed_icons = list(findAll(system().images("Installed.png")))
    except FindFailed:
      installed_icons = list()   
    for icon in installed_icons:
      icon.highlight(2)
      tempApp = AppObject()
      tempApp.topleft("Installed",icon)
      self.installedapps.append(tempApp)
    self.installedapps = sorted(self.installedapps,key=attrgetter('y','x'))
    return self.installedapps

  def is_installed(self,appname):
     #Checks to see if an app is installed
     app.focus()
     try: 
       this.page_loaded()
     except FindFailed:
       app.gotourl(self.url())
       this.page_loaded()
     try: 
       appRegion = find(appname)
       #appRegion.highlight(2)
       tempApp = AppObject()
       tempApp.topleft("App Name", appRegion)
       tempApp.find("Installed")
       return true
     except FindFailed:
       return false
