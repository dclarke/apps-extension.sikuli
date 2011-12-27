from operator import itemgetter, attrgetter
from pprint import pprint

# works on all platforms
import os
import unittest

mmd = Settings.MoveMouseDelay
Settings.MouseMoveDelay = 2

# get the directory containing your running .sikuli
Path = os.path.dirname(getBundlePath()) + '/example.sikuli/'
testPath = os.path.dirname(getBundlePath()) + '/example.sikuli/tests'
if not Path in sys.path: sys.path.append(libPath)
if not testPath in sys.path: sys.path.append(testPath)

execfile(Path + '/loader.py')    

firefox = Firefox()


#applications = list()
#suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestB) # see comment
#unittest.TextTestRunner(verbosity=2).run(suite)

Settings.MoveMouseDelay = mmd # reset to original value

