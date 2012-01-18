"""
Author: David Clarke
Contributors: David Clarke, Mohamed Dabbagh, Jason Smith
"""

import subprocess
import os 

class OSBox(object):
    """ Base class representation for all machines """
    FIREFOX_APP_NAME = None

    def __init__(self):
        self.mach = "unknown"

    def images(self, filename):
        """ Find an image stored in images/(mac/win/linux) or images directory"""
        directory = 'images' + SEPARATOR + self.mach + SEPARATOR
        if (os.path.isfile(PATH + directory + filename)):
            return PATH + directory + filename
        else:
            return PATH + 'images' + SEPARATOR + filename

class MacOSBox(OSBox):
    """ A MacOSBox object will contain functions that are mac specific """
    FIREFOX_APP_NAME = 'Firefox'
    
    def __init__(self):
        super(MacOSBox, self).__init__()
        self.home = os.path.expanduser("~") + "/Applications/"
        self.mach = "mac"

    def nativediropen(self):
        """nativediropen: will open the directory where the native application is installed
         this can be used in conjunction with the vision processing inside sikuli to verify 
         an application was installed
        """
        subprocess.call(["open", self.home])

    def nativedirdeleteapps(self):
        """ delete all the apps that are installed, this api needs to nativedirdelete(self, app) 
        nativedirdeleteapps will delete all the apps in the binary installed application """
        subprocess.call(["rm", "-rf", self.home])

    def images(self, filename): 
        return super(MacOSBox, self).images(filename)

    def firefoxLocation(self):
        if(os.path.isdir('/Applications/Firefox.app/Contents/MacOS')):
            return '/Applications/Firefox.app/Contents/MacOS/firefox-bin'
        else:
            # XXX: Need to return proper error
            return 0

    def maximizeapp(self, app):
        """ maximize the application that you pass in """
        app.focus()
        print self.images("maximize_firefox.png")
        mTL = find(self.images("maximize_firefox.png"))
        dragDrop(mTL.getCenter().offset(50,0), Location(100,30))
        mLL = find(self.images("bottom_right.png"))
        reg = Screen(0).getBounds()
        dragDrop(mLL, Location(reg.width,reg.height-100))

class WinError(Exception):
    """
    Error to indicate a windows-specific issue, such as finding windows-specific icons.
    """
    pass

class WinOSBox(OSBox):
    """ A windows OSBox will contain functions that are windows specific """

    MAXIMIZE_BUTTON = "maximize_firefox_icon.png"
    MINIMIZE_BUTTON = "minimize_icon.png"
    FIREFOX_APP_NAME = 'Mozilla Firefox'

    def __init__(self):
        super(WinOSBox, self).__init__()
        self.home = os.getenv('APPDATA')
        self.mach = "windows"
  
    def images(self,filename):
        """ images is custom for windows because their slashes are always the wrong way
            essence is to return all the images"""
        return super(WinOSBox, self).images(filename)
  
    def nativediropen(self):
        """ Opening APPDATA in windows"""
        raise NotImplementedError

    def nativedirdeleteapps(self):
        """unimplemented in windows"""
        raise NotImplementedError
	
    def firefoxLocation(self):
        if(os.path.isdir('C:\\Program Files (x86)\\Mozilla Firefox\\')):
            return 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
        elif(os.path.isdir('C:\\Program Files\\Mozilla Firefox\\')):
            return 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        else:
		    raise WinError, "Could not find firefox.exe on Windows"

    def maximizeapp(self, app):
        """
        Maximizes the specified application utilizing the windows maximize icon if it exists.
        
        Arguments:
            app: The application to maximize
        """
        # XXX: Need to maximize against the particular app region
        maxButton = self.images(WinOSBox.MAXIMIZE_BUTTON)
        minButton = self.images(WinOSBox.MINIMIZE_BUTTON)
        
        if(exists(maxButton)):
            click(maxButton)
        elif(not exists(minButton)):
            raise WinError, "Could not find windows maximize or minimize button on application"

class LinOSBox(OSBox):
    """ linuxOSBox is currently untested, but will need to be filled in when appropriate """
    def __init__(self):
        super(LinOSBox, self).__init__()
        self.home = os.path.expanduser("~") + "/Applications/"
        self.mach = "linux"

    def firefoxLocation(self):
        if(os.path.isfile('/usr/bin/firefox')):
            return '/usr/bin/firefox'

    def maximizeapp(self, app):
        app.focus()
        maxButton = self.images("maximize_firefox_icon.png")
        if(exists(maxButton)):
            click(maxButton)


class UnsuppportedOSError(Exception):
    """
    Thrown to indicate that the OS running is not supported.
    """
    pass


class ConstructOSBox(object):
    """ 
    A call to the System class anywhere should return an object
    that is tailored to return operating system dependent data
    """
    
    OS_BOXES = {
        'Linux': LinOSBox,
        'Windows': WinOSBox,
        'Mac': MacOSBox
    }

    def __new__(cls):
        name = str(MYOS).capitalize()
        
        if name in ConstructOSBox.OS_BOXES:
            return ConstructOSBox.OS_BOXES[name]()
        else:
            raise UnsupportedOSError("Operating system not supported for this test framework")
