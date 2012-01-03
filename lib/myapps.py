import time
class MyApps:
  def __init__(self,app):
    self.url = "https://myapps.mozillalabs.com/"
    self.applications = list()
    self.installedapps = list()
    self.app = app

  def page_loaded(self):
    wait(system().images("clicktolaunch.png"))
    self.app.reload()

  def focus(self):
    res = find(system().images("clicktolaunch.png"))
    click(res)

  def delete(self,appimage):
    self.focus()
    found = find(appimage)
    uninstall_visible = 0 
    hover(found)
    mouseDown(Button.LEFT)
    wait(2)
    mouseUp() 
    click(system().images("uninstall_ok.png"))

  def go(self):
    click(system().images("dashbaord_launcher.png"))
