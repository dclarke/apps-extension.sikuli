"""
File: basic_install_test.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

class BasicInstallTest(unittest.TestCase):
    """Sanity tests to verify web and native installation of applications."""

    def setUp(self):
        """
        Sets up a firefox instance and other required dependencies,
        loads the application directory page, and determines
        the existing installable and installed applications.
        """
        self.firefox = Firefox()
        self.firefox.switchappdirtab()

        self.appdir = AppDirPage()
        self.appdir.page_loaded()
        self.myapps = MyAppsPage(self.firefox)

        self.installable = self.appdir.installable_apps()
        self.installed = self.appdir.installed_apps()
        self.system = ConstructOSBox()

    def tearDown(self):
        """
        Finds all existing installed applications and uninstalls
        them from the web and on the native desktop.
        """
        self.firefox.switchappdirtab()
        installed = self.appdir.installed_apps()
        iconimages = []
        
        for app in installed:
           iconimages.append(app.iconimage())
        
        # If there are installed apps, uninstall from web/native
        if iconimages:
          self.firefox.gotodashboard()
          self.myapps.page_loaded()
          for icon in iconimages: 
              self.myapps.delete(icon)
          self.system.nativedirdeleteapps()

    def test_install_appdir_shows_installed(self):
        """
        Installs the first application on the application directory
        page, reloads it, and verifies the application is still installed.
        """
        self.installable[0].install_region().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.firefox.reload()
        self.assertTrue(self.installable[0].installed())
   
    def test_single_native_install(self):
        """
        Installs the first application on the application directory
        page, reloads it, and checks if the native desktop has it
        installed.
        """
        self.installable[0].install_region().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))

        self.firefox.reload()
        self.installed = self.appdir.installed_apps()

        img = desktopsize(self.installed[0].iconimage())
        self.system.nativediropen()
        wait(1)
        self.assertTrue(exists(img))

    def test_two_native_app_installs(self):
        """
        Installs two applications on the application directory page,
        reloads it, and checks if the native desktop has both
        applications installed.
        """
        self.installable[3].install_region().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))
        self.installable[4].install_region().click(self.system.images("Install.png"))
        click(self.system.images("install_accept.png"))

        self.firefox.reload()
        self.appdir.page_loaded()
        self.installed = self.appdir.installed_apps()

        img3 = desktopsize(self.installed[0].iconimage())
        img4 = desktopsize(self.installed[1].iconimage())
        self.system.nativediropen()
        self.assertTrue(exists(img3) and exists(img4))
