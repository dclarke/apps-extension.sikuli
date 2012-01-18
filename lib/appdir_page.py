"""
File: appdir.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

from pprint import pprint
from operator import itemgetter, attrgetter

class AppDirPage:
    """
    An AppDir object is an object representation of https://apps.mozillalabs.com/appdir.
    The purpose of the object is to be able to dissect the page and determine what is installed.
    """
    URL = "https://apps.mozillalabs.com/appdir"
    DEMO_APPS_IMG = "demoapps.png"
    APPS_VISIBLE_IMG = "appsvisible.png"
    INSTALL_IMG = "Install.png"
    INSTALLED_IMG = "Installed.png"

    def __init__(self):
        """ 
        AppDir constructor sets the page url, and takes an application object.  
        It allows for the AppDir to make calls into the firefox application to make sure 
        that the correct page is loaded, the browser is focused..etc.
        """
        self._system = ConstructOSBox()

    def page_loaded(self):
        """
        Waits for the main image on the page to load before returning.
        """
        wait(self._system.images(AppDirPage.DEMO_APPS_IMG), IMAGE_LOOKUP_TIMEOUT)
        wait(self._system.images(AppDirPage.APPS_VISIBLE_IMG), IMAGE_LOOKUP_TIMEOUT)

    def installable_apps(self):
        """
        Find all the apps that are not installed.
        """
        self._applications = list()

        install_icons = list(findAll(self._system.images(AppDirPage.INSTALL_IMG)))
        for icon in install_icons:
            tempApp = AppObject()
            tempApp.topleft("Install Button", icon)
            self._applications.append(tempApp)

        self._applications = sorted(self._applications, key=attrgetter('y', 'x'))
        return self._applications

    def installed_apps(self):
        """
        Finds all of the apps that are currently installed.
        
        Returns:
            The list of installed applications as application objects.
        
        XXX: Not all installed images are found consistently. Likely,
             we need to wait until the page is fully loaded before
             this method is executed.
        """
        installed_icons = None

        installed_icons = []
        installed_image = self._system.images(AppDirPage.INSTALLED_IMG)

        # If the installed image is found, get all of them
        if(exists(installed_image)):
            installed_icons = list(findAll(installed_image))  

        installed_apps = []

        # Creates an application object for each installed app found
        for icon in installed_icons:
            temp_app = AppObject()
            temp_app.topleft("Installed", icon)
            installed_apps.append(temp_app)

        return sorted(installed_apps, key=attrgetter('y', 'x'))

    # Disabled, as it is not be used and needs to be cleaned up
    """def is_installed(self, appname):
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
            return false"""
