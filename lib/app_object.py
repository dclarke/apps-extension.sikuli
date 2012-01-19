"""
File: app_page.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

from pprint import pprint

class AppObject:
    """
    AppObject encapsulates the visual representation for an app on the
    https://apps.mozillalabs.com/appdir page. It breaks down an app into
    a name, install_icon, nameregion, icon..etc
    """

    def __init__(self):
        """
        Initialization, unknown coordinates, of the application object 
        x,y are considered the top left corner of the application object 
        """
        self.x = 0
        self.y = 0
 
    def topleft(self, name, region):
        """
        Attempts to set x, and y coordinates of the application, based upon
        the region you are passing in. If you have the "Install Button"
        then you can work backwards and find the top left for the application
        object. Once you have the top left, all the other positioning is known.
        
        Arguments:
            name: The name of the region name being looked for
            region: The region to analyze to find the app
        
        Returns:
            True if the application was found in the region, False otherwise
        """
        regionFound = True
        
        # TODO: This needs to be refactored - Shouldn't be making dependencies
        #       on specific buttons to find and using hardcoded constants without
        #       definition.
        if name == "Install Button":
            self.x = region.getX() - 110
            self.y = region.getY() - 70
        elif name == "App Name":
            self.x = region.getX() - 110 
            self.y = region.getY() - 50
        elif name == "Installed":
            self.x = region.getX() - 110
            self.y = region.getY() - 77
        else:
            self.x = 0
            self.y = 0 
            regionFound = False

        return regionFound

    def name(self, expected):
        """
        You can only verify the expected name, sikuli doesn't return the OCR,
        you can only verify against an expected value.
        
        TODO: What does this method actually do?
        """
        region = nameregion()
        name = None
        
        if(region.exists(expected)):
            name = region.find(expected).text()
            
        return name

    def installregion(self):
        """
        Returns a region that contains the install button for this app.
        
        TODO: Avoid hardcoding this, needs to be refactored
        """ 
        return Region(self.x + 110, self.y + 70, 100, 30)

    def nameregion(self):
        """
        Returns the region that contains the name of the app.
        
        TODO: Avoid hardcoding this, needs to be refactored
        """
        return Region(self.x + 110, self.y + 50, 170, 25)

    def iconregion(self):
        """
        Returns the 100 x 100 region of the icon.

        TODO: Avoid hardcoding this, needs to be refactored
        """
        return Region(self.x + 10, self.y + 10, 80, 80)
  
    def iconimage(self):
        """
        Stores the region image in a file, and returns the location. 
        This technique is good when you want to compare images across
        multiple pages.
        """
        return capture(self.iconregion())
   
    def installed(self):
        """
        Finds if an app is installed by checking on apps.mozillalabs.com/appdir
        page.
        """
        try:
            Region(self.x + 105, self.y + 77, 80, 25).highlight(2)
            Region(self.x + 105, self.y + 77, 80, 25).find("installed!")
            return True
        except FindFailed:
            return False       
