"""
File: image_resize.py

Author: David Clarke
Contributor(s): Jason Smith

Date: 1/18/2012
"""

def desktopsize(filename):
    from org.mozilla.sikuli.utils import ImageResize                                    
    ImageResize(filename)   
    return filename
