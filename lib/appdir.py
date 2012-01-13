from pprint import pprint
from operator import itemgetter, attrgetter

class AppDir:
    """ An AppDir object is an object representation of https://apps.mozillalabs.com/appdir
        The purpose of the object is to be able to dissect the page and determine what is installed
    """
    def __init__(self, app):
        """ AppDir constructor sets the page url, and takes an application object.  
            It allows for the AppDir to make calls into the firefox application to make sure 
            that the correct page is loaded, the browser is focused..etc.
        """
        self.app = app
        self.url = "https://apps.mozillalabs.com/appdir"
        self.system = ConstructBox()
        self.applications = []
        self.installedapps = []

    def page_loaded(self):
        """ Waits for the main image on the page to load before returning"""
        wait(self.system.images("demoapps.png"))
        wait(self.system.images("appsvisible.png"))

    def installable_apps(self):
        """ Find all the apps that are not installed"""
        self.applications = list()
        install_icons = list(findAll(self.system.images("Install.png")))
        for icon in install_icons:
            tempApp = AppObject()
            tempApp.topleft("Install Button",icon)
            self.applications.append(tempApp)
        self.applications = sorted(self.applications,key=attrgetter('y','x'))
        return self.applications

    def installed_apps(self):
        """Finds alls the apps that are currently installed"""
        installed_icons = None
        self.installedapps = list()
        try: 
            installed_icons = list(findAll(self.system.images("Installed.png")))
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
        """Checks to see if an app is installed"""
        app.focus()
        try: 
            this.page_loaded()
        except FindFailed:
            app.gotourl(self.url())
            this.page_loaded()
        try: 
            appRegion = find(appname)
            tempApp = AppObject()
            tempApp.topleft("App Name", appRegion)
            return tempApp.installed()
        except FindFailed:
            return false
