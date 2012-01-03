from pprint import pprint

class Firefox:
  def __init__(self):
    self.os = "MacOSX" 

  def loadbrowser(self):
    self.myApp = App("Firefox")
    if not self.myApp.window(): # no window(0) - Firefox not open
      App.open("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
      wait(2)
    self.maximize()

  def focus(self):
    self.myApp.focus()

  def gotourl(self,url):
    wait(1)
    type("l", KEY_CMD) # switch to address field
    type("https://apps.mozillalabs.com/appdir" +  Key.ENTER)

  def maximize(self):
    self.focus()
    wait(2)
    system().maximize_firefox(self.myApp)

  def reload(self):
    self.focus()
    type("r", KEY_CMD) # reload page

  def gotodashboard(self):
    self.focus()
    click(system().images("dashboard_launcher.png"))

  def switchappdirtab(self):
    self.focus()
    click(system().images("appdirtab.png"))
    self.reload()
