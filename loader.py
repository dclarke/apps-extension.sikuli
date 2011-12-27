import glob
def execdir(path):
  listing = glob.glob(path + "/*.py")
  for infile in listing:
     print infile
     execfile(infile,globdict)

globdict= globals()

execdir(Path + 'lib')
execdir(Path + 'tests')


