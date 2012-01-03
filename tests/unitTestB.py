firefox = Firefox()
appdir = AppDir(firefox)
myapps = MyApps(firefox)

firefox.loadbrowser()
firefox.gotourl(appdir.url)

class UnitTestB(unittest.TestCase):
    def __init__(self,testName):
        unittest.TestCase.__init__(self,testName)
    def setUp(self):
        firefox.switchappdirtab()
        appdir.page_loaded()
        installed = appdir.installed_apps()
        popup("number of installed apps %d\n" %len(installed))
        iconimages = list()
        for app in installed:
           iconimages.append(app.iconimage())
        if len(iconimages) > 0:
          print "number of images to uninstall %d\n" %len(iconimages)
          firefox.gotodashboard()
          myapps.page_loaded()
          system().nativedirdeleteapps()       
          for icon in iconimages: 
             myapps.delete(icon)

        firefox.switchappdirtab()
        appdir.page_loaded()
        self.installable = appdir.installable_apps()
        self.installed = appdir.installed_apps()
    def testInstallA(self):
        self.installable[0].install_icon().click(system().images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.assertTrue(self.installable[0].installed())
    def testInstallB(self):
        firefox.focus()
        self.installable[0].install_icon().click(system().images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        img = self.installed[0].iconimage()
        system().nativediropen()
        print(img)
        find(img)
        assert exists(img)
        
