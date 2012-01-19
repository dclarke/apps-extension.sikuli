class TimeoutStartupError(Exception):
    """
    Thrown to indicate that firefox failed to startup within a time period.
    """
    pass


class Firefox:
    """
    This class encapsulates actions that occur on the Firefox browser.
    """

    def __init__(self):
        """
        Constructs a Firefox application instance and loads the application.
        """
        self._system = ConstructOSBox()
        self.start_browser()
        self.maximize()

    def start_browser(self):
        """ Starts up the browser if it hasn't already started and waits until it is loaded.
        
        Raises:
        TimeoutStartupError: If firefox fails to startup within ten seconds

        """
        self._location = self._system.firefoxLocation()
        self._firefox = App(self._system.FIREFOX_APP_NAME)
        
        # If firefox isn't loaded, start firefox
        if not self._firefox.window():
            App.open(self._location)
        
        is_started = False
        time_passed = 0
        
        # Wait until firefox has started for a period of time
        while(not is_started and time_passed < IMAGE_LOOKUP_TIMEOUT):
            if self._firefox.window():
                is_started = True
            wait(1)
        
        # If firefox has not started, throw an error
        if not is_started:
            raise TimeoutStartupError("Timeout on starting up firefox.")

    def focus(self):
        """
        Brings Firefox to the foreground by focusing on the firefox application.
        """
        self._firefox.focus()

    def go_to_url(self, url):
        """
        Instructs the browser to go to the specified URL.
        
        Arguments:
        url: The url to go to

        """
        if(self._system.mach == 'mac'):
            type("l", KEY_CMD)
        else:
            type('l', KEY_CTRL)

        paste(url)
        type(Key.ENTER)

    def maximize(self):
        """ Maximizes the application """
        self._system.maximizeapp(self._firefox)

    def reload(self):
        """ Reloads the current page """
        if(self._system.mach == 'mac'):
            type("r", KEY_CMD) # reload page
        else:
            type('r', KEY_CTRL)

    def gotodashboard(self):
        """ clicks on the dashboard icon in the bottom right of firefox. 
            this is only valid if the extension is installed 
        """
        if(exists(self._system.images("developer_preview_tab.png"))):
            click(self._system.images("developer_preview_tab.png"))
            return
 
        if(self._system.mach == 'mac'):
            type("t", KEY_CMD) # reload page
        else:
            type('t', KEY_CTRL)
        
        self.go_to_url('https://myapps.mozillalabs.com/')

    def switchappdirtab(self):
        """ switches to the apps.mozillalabs.com/appdir tab """
        if(exists(self._system.images("mozilla_appdir_tab.png"))):
            click(self._system.images("mozilla_appdir_tab.png"))
            self.reload()
            return
        if(self._system.mach == 'mac'):
            type("t", KEY_CMD) # reload page
        else:
            type('t', KEY_CTRL) 
        self.go_to_url('https://apps.mozillalabs.com/appdir')

