"""
File: myapps_page.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

class ApplicationNotFoundError(Exception):
    """
    Thrown to indicate that the application image specified was not found.
    """
    pass


class MyAppsPage:
    """
    Represents the My Applications Web Page at the below URL specified
    in the constant. Allows callers to delete applications.
    """
    URL = "https://myapps.mozillalabs.com/"
    CLICK_TO_LAUNCH_IMG = "clicktolaunch.png"
    UNINSTALL_OK_IMG = "uninstall_ok.png"

    def __init__(self):
        """
        Constructs a MyAppsPage object. 
        """
        self._system = ConstructOSBox()

    def page_loaded(self):
        """
        Waits for the MyAppsPage to be loaded.
        """
        wait(self._system.images(MyAppsPage.CLICK_TO_LAUNCH_IMG))

    def delete(self, appimage):
        """
        Deletes the specified application specified in the image.
        
        Arguments:
            appimage: The image of the application to delete

        Throws:
            ApplicationNotFoundError if the application image specified
            is not found
        """
        self.page_loaded()
        
        if(exists(appimage)):
            hover(find(appimage))
            mouseDown(Button.LEFT)
            wait(2)
            mouseUp() 
            click(self._system.images(MyAppsPage.UNINSTALL_OK_IMG))
        else:
            raise ApplicationNotFoundError(str(appimage) + " was not found.")
