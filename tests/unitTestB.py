class UnitTestB(unittest.TestCase):

    def setUp(self):
        self.firefox = Firefox()
        self.firefox.switchappdirtab()
        
        self.appdir = AppDir(self.firefox)
        self.appdir.page_loaded()
        self.myapps = MyApps(self.firefox)

        self.installable = self.appdir.installable_apps()
        self.installed = self.appdir.installed_apps()
        self.system = ConstructBox()

    def tearDown(self):
        self.firefox.switchappdirtab()
        installed = self.appdir.installed_apps()
        iconimages = []
        for app in installed:
           iconimages.append(app.iconimage())
        
        if len(iconimages) > 0:
          self.firefox.gotodashboard()
          self.myapps.page_loaded()
          self.system.nativedirdeleteapps()
          for icon in iconimages: 
              self.myapps.delete(icon)

    def testInstallAppDir(self):
        self.installable[0].installregion().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.firefox.reload()
        self.assertTrue(self.installable[0].installed())
   
    def disabled_testInstallB(self):
        self.installable = appdir.installable_apps()
        self.installable[0].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.installed = appdir.installed_apps()
        img = self.installed[0].iconimage()
        img = desktopsize(img)
        print img
        system.nativediropen()
        wait(1)
        find(img).highlight(2)
        assert exists(img)
    
    def disabled_testInstallC(self):
        firefox.focus()
        self.installable[3].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        self.installable[4].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
        self.installed = appdir.installed_apps()
        img3 = desktopsize(self.installed[0].iconimage())
        img4 = desktopsize(self.installed[1].iconimage())
        system.nativediropen()
        assert exists(img3)    
        assert exists(img4) 
