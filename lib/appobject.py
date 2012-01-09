from pprint import pprint

class AppObject:
    """ AppObject tries to encapsulate the visual representation for an app on apps.mozillalabs.com/appdir page
        It breaks down an app into a name, install_icon, nameregion, icon..etc
    """
    def __init__(self):
        """ Initialization, unknown coordinates, of the application object 
            x,y are considered the top left corner of the application object 
        """
        self.x = 0
        self.y = 0
   
    def __repr__(self):
        return 
 
    def topleft(self,name,region):
        """ Attempts to set x, and y coordinates of the application, based upon the region you are passing in. 
            If you have the "Install Button" then you can work backwards and find the top left for the application
            object. Once you have the top left, all the other positioning is known. 
        """
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
            return False
        return True

    def name(self,expected):
        """ You can only verify the expected name, sikuli doesn't return the OCR, you can only verify against 
            an expected value
        """
        try:
            return nameregion().find(expected).text()
        except FindFailed:
            return None

    def installregion(self):
        """ Returns a region that contains the install button for this app """ 
        return Region(self.x + 110,
                  self.y + 70, 
                  100, 30)

    def nameregion(self):
        """ Returns the region that contains the name of the app """
        return Region(self.x + 110,
                  self.y + 50,
                  170, 25)

    def iconregion(self):
        """ Returns the 100 x 100 region of the icon """
        return Region(self.x+10, self.y+10,
                  80, 80)
  
    def iconimage(self):
        """ Stores the region image in a file, and returns the location. 
            This technique is good when you want to compare images across multiple pages
        """
        foo = self.iconregion()
        return capture(foo)
   
    def installed(self):
        """ Finds if an app is installed by checking on apps.mozillalabs.com/appdir page. """
        try:
            Region(self.x + 105, self.y + 77, 80, 25).highlight(2)
            Region(self.x + 105, self.y + 77, 80, 25).find("installed!")
            return True
        except FindFailed:
            return False       
