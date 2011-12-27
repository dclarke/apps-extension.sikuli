from pprint import pprint

class AppDir:
  def __init__(self,app):
    self.app = app
    self.url = "https://apps.mozillalabs.com/appdir"
    self.applications = list()
    self.installedapps = list()

  def page_loaded(self):
    wait("DemoAPPSAcol.png")

  def InstallableApps(self):
    install_icons = list(findAll(system().images("Install.png")))
    for icon in install_icons:
      tempApp = AppObject()
      tempApp.topleft("Install Button",icon)
      self.applications.append(tempApp)
    self.applications = sorted(self.applications,key=attrgetter('y','x'))
    return self.applications

  def InstalledApps(self):
    installed_icons = None
    try: 
      installed_icons = list(findAll(system().images("Installed.png")))
    except FindFailed:
      installed_icons = list()   
    for icon in installed_icons:
      tempApp = AppObject()
      tempApp.topleft("Installed",icon)
      self.applications.append(tempApp)
    self.installedapps = sorted(self.applications,key=attrgetter('y','x'))
    return self.installedapps

  def isInstalled(self,appname):
     app.focus()
     try: 
       this.page_loaded()
     except FindFailed:
       app.gotourl(self.url())
       this.page_loaded()
     try: 
       appRegion = find(appname)
       appRegion.highlight(3)
       tempApp = AppObject()
       tempApp.topleft("App Name", appRegion)
       tempApp.find("Installed")
       return true
     except FindFailed:
       return false
