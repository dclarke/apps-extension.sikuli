"""
File: myapps_page.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

class MyAppsPage:
    """ MyApps class creates a page object model """
    URL = "https://myapps.mozillalabs.com/"

    def __init__(self, app):
        """ initialize the myapp object """
        self.system = ConstructOSBox()

    def page_loaded(self):
        """Reloads the dashboard """
        wait(self.system.images("clicktolaunch.png"), 10)

    def delete(self, appimage):
        """ delete an app from the myapps page """
        self.go()
        self.page_loaded()
        found = find(appimage)
        uninstall_visible = 0 
        hover(found)
        mouseDown(Button.LEFT)
        wait(2)
        mouseUp() 
        click(self.system.images("uninstall_ok.png"))

    def go(self):
        """ launches the dashboard, through the icon in the bottom right of firefox """
        click(self.system.images("dashboard_launcher.png"))
