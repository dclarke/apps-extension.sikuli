#firefox = Firefox()
#appdir = AppDir(firefox)
#myapps = MyApps(firefox)
#system = System()
#firefox.loadbrowser()

class UnitTestB(unittest.TestCase):

    def setUp(self):
        wait(1)
        firefox = Firefox()
        firefox.switchappdirtab()
        """firefox.focus()
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
        self.installed = appdir.installed_apps()"""
   
    def testSanity(self):
        pass
   
    def disabled_testInstallA(self):
        self.installable[0].installregion().click(system.images("Install.png"))
        click("images/install_accept.png")
        firefox.reload()
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
