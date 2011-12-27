import time
class MyApps:
  def __init__(self,app):
    self.app = app
    self.url = "https://myapps.mozillalabs.com/"
    self.applications = list()
    self.installedapps = list()

  def page_loaded(self):
    wait(system().images("clicktolaunch.png"))

  def delete(self,appimage):
		found = find(appimage)
    found.mouseDown(Button.LEFT)
    time.sleep(2)
    found.mouseUp(Button.LEFT)
	  click(system().images("uninstall_ok"))

  def go(self):
    click(system().images("dashbaord_launcher.png"))
