class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.firefox = Firefox()
        self.firefox.switchappdirtab()

        self.appdir = AppDirPage()
        self.appdir.page_loaded()
        self.myapps = MyAppsPage(self.firefox)

        self.installable = self.appdir.installable_apps()
        self.installed = self.appdir.installed_apps()
        self.system = ConstructOSBox()

    def tearDown(self):
        self.firefox.switchappdirtab()
        installed = self.appdir.installed_apps()
        iconimages = []
        for app in installed:
           iconimages.append(app.iconimage())
        
        if len(iconimages) > 0:
          self.firefox.gotodashboard()
          self.myapps.page_loaded()
          for icon in iconimages: 
              self.myapps.delete(icon)
          self.system.nativedirdeleteapps()

    def testInstallAppDir(self):
        self.installable[0].installregion().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.firefox.reload()
        self.assertTrue(self.installable[0].installed())
   
    def testSingleNativeInstall(self):
        self.installable = self.appdir.installable_apps()
        self.installable[0].installregion().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.firefox.reload()
        self.installed = self.appdir.installed_apps()
        img = self.installed[0].iconimage()
        img = desktopsize(img)
        self.system.nativediropen()
        wait(1)
        find(img).highlight(2)
        self.assertTrue(exists(img))

    def testTwoNativeAppInstalls(self):
        self.installable[3].installregion().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.installable[4].installregion().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.firefox.reload()
        self.installed = self.appdir.installed_apps()
        img3 = desktopsize(self.installed[0].iconimage())
        img4 = desktopsize(self.installed[1].iconimage())
        self.system.nativediropen()
        self.assertTrue(exists(img3) and exists(img4))
