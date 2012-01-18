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
        self._app = app
        self._url = "https://apps.mozillalabs.com/appdir"
        self._system = ConstructBox()
        self._applications = []
        self._installedapps = []

    def page_loaded(self):
        """ Waits for the main image on the page to load before returning"""
        wait(self._system.images("demoapps.png"), 10)
        wait(self._system.images("appsvisible.png"), 10)

    def installable_apps(self):
        """ Find all the apps that are not installed"""
        self._applications = list()
        
        install_icons = list(findAll(self._system.images("Install.png")))
        for icon in install_icons:
            tempApp = AppObject()
            tempApp.topleft("Install Button",icon)
            self._applications.append(tempApp)
        self._applications = sorted(self._applications,key=attrgetter('y','x'))
        return self._applications

    def installed_apps(self):
        """Finds alls the apps that are currently installed"""
        installed_icons = None
        self._installedapps = list()
        try:
            installed_image = 'Installed.png'
            # XXX: May not work for more than 3 applications
            installed_icons = list(findAll(self._system.images(installed_image)))   
        except FindFailed:
            installed_icons = list()   
        for icon in installed_icons:
            icon.highlight(2)
            tempApp = AppObject()
            tempApp.topleft("Installed",icon)
            self._installedapps.append(tempApp)
        self._installedapps = sorted(self._installedapps,key=attrgetter('y','x'))
        return self._installedapps

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
