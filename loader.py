'''loader.py is used to load all the libraries / tests into the 
   main context for processing.
'''
import glob 

def execdir(path, separator, directory):
    '''execdir recurses a directory and calls execfile on each python file'''
    pythonfiles = path + directory + separator + "*.py"
    listing = glob.glob(pythonfiles)
    for infile in listing:
        execfile(infile, GLOBDICT)

GLOBDICT = globals()

def importfiles(path, separator):
    '''importfiles takes a path and a separator'''
    execdir(path, separator, 'lib')
    execdir(path, separator, 'tests')
