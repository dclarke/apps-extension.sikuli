from pprint import pprint

class AppObject:
  def __init__(self):
    self.x = 0
    self.y = 0
   
  def __repr__(self):
    return 
  def topleft(self,name,region):
    if name == "Install Button":
          self.x = region.getX() - 110
          self.y = region.getY() - 70
    elif name == "App Name":
          self.x = region.getX() - 110 
          self.y = region.getY() - 50
    elif name == "Installed":
          self.x = region.getX() - 110
          self.y = region.getY() - 77
    else:
         self.x = 0
         self.y = 0 
         return False
    return True

  def name(self,expected):
    try:
      return nameregion().find(expected).text()
    except FindFailed:
      return None

  def install_icon(self):
    print "install icon"
    print self.x
    print self.y
    return Region(self.x + 110,
                  self.y + 70, 
                  100, 30)

  def nameregion(self):
    return Region(self.x + 110,
                  self.y + 50,
                  170, 25)

  def iconregion(self):
    return Region(self.x, self.y,
                  100, 100)
  
  def iconimage(self):
    foo = self.iconregion()
    foo.highlight(2) 
    return capture(foo)
   
  def installed(self):
    try:
      Region(self.x + 105, self.y + 77, 80, 25).find("installed!")
      return True
    except FindFailed:
      return False       
