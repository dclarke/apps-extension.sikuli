class Firefox:
    """ This class encapsulates actions that occur on the browser """
    def __init__(self):
        self.system = System()
        self.loadbrowser()

    def loadbrowser(self):
        """ Load browser, attempts to load the firefox browser """
        self.location = self.system.firefoxLocation()
        self.myApp = App("Mozilla Firefox")
        
        if not self.myApp.window():
            App.open(self.location)
        
        for i in range(10):
            if self.myApp.window(): break
            wait(1)
        
        #self.maximize()

    def focus(self):
        """ Brings Firefox to the foreground """
        self.myApp.focus()

    def gotourl(self,url):
        """ instructs the browser to go to a url """
        wait(2)
        # switch to address field
        if(self.system.mach == 'mac'):
            type("l", KEY_CMD)
        else:
            type('l', KEY_CTRL)
        paste(url)
        type(Key.ENTER)

    def maximize(self):
        """ Maximizes the application """
        self.focus()
        wait(2)
        self.system.maximizeapp(self.myApp)

    def reload(self):
        """ Reloads the current page """
        self.focus()
        if(self.system.mach == 'mac'):
            type("r", KEY_CMD) # reload page
        else:
            type('r', KEY_CTRL)

    def gotodashboard(self):
        """ clicks on the dashboard icon in the bottom right of firefox. 
            this is only valid if the extension is installed 
        """
        self.focus()
        if(exists(self.system.images("developer_preview_tab.png"))):
            click(self.system.images("developer_preview_tab.png"))
            return
 
        if(self.system.mach == 'mac'):
            type("t", KEY_CMD) # reload page
        else:
            type('t', KEY_CTRL)  
        self.gotourl('myapps.mozillalabs.com')

    def switchappdirtab(self):
        """ switches to the apps.mozillalabs.com/appdir tab """
        self.focus()
        if(exists(self.system.images("mozilla_appdir_tab.png"))):
            click(self.system.images("mozilla_appdir_tab.png"))
            self.reload()
            return
        if(self.system.mach == 'mac'):
            type("t", KEY_CMD) # reload page
        else:
            type('t', KEY_CTRL) 
        self.gotourl('https://apps.mozillalabs.com/appdir')

