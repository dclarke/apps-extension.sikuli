from pprint import pprint

class Firefox:
  # Firefox Class deals with opening the browser, and parts of the Windowing system 
  # around the web page.  The idea is for this might be to try and merge this with selenium
  # so you can both programmatically read a page, and visually

  def __init__(self):
    self.os = "MacOSX" 

  def loadbrowser(self):
    self.myApp = App("Firefox")
    if not self.myApp.window(): # no window(0) - Firefox not open
      App.open("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
      wait(5)
     self.focus()
     self.maximize()

  def focus(self):
    self.myApp.focus()

  def gotourl(self,url):
    wait(1)
    type("l", KEY_CMD) # switch to address field
    type("https://apps.mozillalabs.com/appdir" +  Key.ENTER)

  def maximize(self):
    self.focus()
    click(system().images("maximize_firefox.png"))

  def reload(self):
    self.focus()
    type("r", KEY_CMD) # reload page

  def gotodashboard(self):
    self.focus()
    click(system().images("dashboard_launcher.png"))
