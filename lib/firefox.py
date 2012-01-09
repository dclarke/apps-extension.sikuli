class Firefox:
    ''' This class encapsulates actions that occur on the browser '''
    def __init__(self):
        self.system = System()
        print self.system

    def loadbrowser(self):
        ''' Load browser, attempts to load the firefox browser '''
        self.system = System()
        self.myApp = App("Firefox")
        self.location = system.firefoxLocation()
        App.open(self.location)
        wait(5)
        self.maximize()

    def focus(self):
        ''' Brings Firefox to the foreground '''
        self.myApp.focus()

    def gotourl(self,url):
        ''' instructs the browser to go to a url '''
        wait(2)
        if(self.system.mach == 'mac'):
            type("l", KEY_CMD) # switch to address field
            type(url + Key.ENTER)
        else:
            type('l', KEY_CTRL)
            type(url + Key.ENTER)

    def maximize(self):
        ''' Maximizes the application '''
        wait(2)
        self.system.maximizeapp(self.myApp)

    def reload(self):
        ''' Reloads the current page '''
        self.focus()
        if(self.system.mach == 'mac'):
            type("r", KEY_CMD) # reload page
        else:
            type('r', KEY_CTRL)

    def gotodashboard(self):
        ''' Goes to the Dasbhoard by typing the URL in the 
            URL bar
        '''
        self.focus()
        self.gotourl('myapps.mozilllalabs.com')

    def switchappdirtab(self):
        ''' switches to the apps.mozillalabs.com/appdir tab '''
        self.focus()
        click(self.system.images("appdirtab.png"))
        self.reload()
