import _picam
import StringIO
from PIL import Image

def takePhoto():
    s = _picam.takePhoto()
    ss = StringIO.StringIO(s)
    i = Image.open(ss)
    return i     

def takePhotoWithDetails(width, height, quality):
    s = _picam.takePhotoWithDetails(width, height, quality)
    ss = StringIO.StringIO(s)
    i = Image.open(ss)
    return i  