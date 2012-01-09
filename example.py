""" Main python script used to load all the test cases, and run the test suite"""

import unittest


mmd = Settings.MoveMouseDelay
Settings.MouseMoveDelay = 2

MYOS = Env.getOS()

SEPARATOR = '/'
if MYOS == OS.WINDOWS:
    SEPARATOR = '\\'

# get the directory containing your running .sikuli

PATH = getBundlePath() + SEPARATOR

if not PATH in sys.path: sys.path.append(PATH)


execfile(PATH + 'loader.py')  

importfiles(PATH, SEPARATOR)

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTestB) # see comment
unittest.TextTestRunner(verbosity=2).run(SUITE)

Settings.MoveMouseDelay = mmd # reset to original value
    

