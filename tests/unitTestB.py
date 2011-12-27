firefox = Firefox()
appdir = AppDir(firefox)
myapps = MyApps()
class UnitTestB(unittest.TestCase):
    def __init__(self,testName):
        unittest.TestCase.__init__(self,testName)
    def setUp(self):
        firefox.loadbrowser()
        installed = appdir.installed_apps()
        iconimages = list()
        for app in installed:
           iconimages.append(app.iconimage())

        firefox.gotodashboard()
        myapps.page_loaded()
        system().nativedirdeleteapps()       
        for icon in iconimages: 
           myapps.delete(img)

        firefox.gotourl(appdir.url)
        
        self.installable = appdir.installable_apps()
        self.installed = appdir.installed_apps()
        
    def testInstallA(self):
        print(len(self.installable))
        self.installable[0].install_icon().click(system().images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.assertTrue(self.installable[0].installed())
    def testInstallB(self):
        firefox.focus()
        img = self.installed[0].iconimage()
        system().nativediropen()
        print(img)
        find(img)
        assert exists(img)
        
