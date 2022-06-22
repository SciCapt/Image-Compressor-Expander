from PIL import Image
import numpy as np
from Expander import *
from Compressor import *

def Sharpen(pic):

    # Array size
    ydim = len(pic)
    xdim = len(pic[0])

    # Blurred image copy
    blur = Smallen(pic)
    blur = Bigen(blur)

    # Subtraction data
    for j in range(ydim):
        for i in range(xdim):
            for c in range(3):
                newpix = 2*int(pic[j,i,c]) - int(blur[j,i,c])
                newpix = max(0, min(newpix, 255))
                pic[j,i,c] = np.uint8(newpix)

    return pic
