firefox = Firefox()
appdir = AppDir(firefox)
myapps = MyApps(firefox)
system = System()

firefox.loadbrowser()
firefox.gotourl(appdir.url)

class UnitTestB(unittest.TestCase):
    def __init__(self,testName):
        unittest.TestCase.__init__(self,testName)
    def setUp(self):
        firefox.switchappdirtab()
        appdir.page_loaded()
        installed = appdir.installed_apps()
        iconimages = list()
        for app in installed:
           iconimages.append(app.iconimage())
        if len(iconimages) > 0:
          firefox.gotodashboard()
          myapps.page_loaded()
          system.nativedirdeleteapps()       
          for icon in iconimages: 
             myapps.delete(icon)

        firefox.switchappdirtab()
        appdir.page_loaded()
        self.installable = appdir.installable_apps()
        self.installed = appdir.installed_apps()
    def testInstallA(self):
        self.installable[0].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.assertTrue(self.installable[0].installed())
    def testInstallB(self):
        firefox.focus()
        self.installable[0].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.installed = appdir.installed_apps()
        img = self.installed[0].iconimage()
        system.nativediropen()
        find(img)
        assert exists(img)
        
