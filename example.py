
from operator import itemgetter, attrgetter
from pprint import pprint

# works on all platforms
import os
import unittest


mmd = Settings.MoveMouseDelay
Settings.MouseMoveDelay = 2

# get the directory containing your running .sikuli

Path = getBundlePath() + '/'
print Path
if not Path in sys.path: sys.path.append(Path)

execfile(Path + 'loader.py')  


#applications = list()
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestB) # see comment
unittest.TextTestRunner(verbosity=2).run(suite)

#Settings.MoveMouseDelay = mmd # reset to original value
    

