
class Firefox:
    ''' This class encapsulates actions that occur on the browser '''
    def __init__(self):
        self.os = "MacOSX" 
        self.system = System()
        print self.system

    def loadbrowser(self):
        ''' Load browser, attempts to load the firefox browser '''
        self.myApp = App("Firefox")
        if not self.myApp.window(): # no window(0) - Firefox not open
            App.open("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
            wait(2)
        self.focus()
        self.maximize()

    def focus(self):
        ''' Brings Firefox to the foreground '''
        self.myApp.focus()

    def gotourl(self,url):
        ''' instructs the browser to go to a url '''
        wait(1)
        type("l", KEY_CMD) # switch to address field
        type(url +  Key.ENTER)

    def maximize(self):
        ''' Maximizes the application '''
        self.focus()
        wait(1)
        self.system.maximizeapp(self.myApp)

    def reload(self):
        ''' Reloads the current page '''
        self.focus()
        type("r", KEY_CMD) # reload page

    def gotodashboard(self):
        ''' clicks on the dashboard icon in the bottom right of firefox. 
            this is only valid if the extension is installed 
        '''
        self.focus()
        click(self.system.images("dashboard_launcher.png"))

    def switchappdirtab(self):
        ''' switches to the apps.mozillalabs.com/appdir tab '''
        self.focus()
        click(self.system.images("appdirtab.png"))
        self.reload()
