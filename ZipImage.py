import os
from Compressor import Smallen
from Expander import Bigen
from PIL import Image
import numpy as np

# Get Files in current Directory
filelist = os.listdir()

# Get Image Filename
for i in range(len(filelist)):
    file = filelist[i]
    checkExtension = file[len(file)-4:len(file)]
    possibleExtensions = [".png", ".PNG", ".jpg", ".JPG"]
    for e in range(len(possibleExtensions)):
        if checkExtension == possibleExtensions[e]:
            if file[len(file)-5] != "_" and file[len(file)-5] != ")":
                filename = file

                # Make Image Data Array
                with Image.open(str(filename)) as image:
                    pic = np.fromstring(image.tobytes(), dtype=np.uint8)
                    pic = pic.reshape((image.size[1], image.size[0], 3))

                # Zip/Compress Image
                pic = Smallen(pic)

                shortFilename = filename[0:len(filename)-4]
                extension = filename[len(filename)-4:len(filename)]
                newFilename = f"{shortFilename}_Compressed_{extension}"

                pic = Image.fromarray(pic)
                pic.save(newFilename)
                print(f"\nCompressed Image Saved as: {newFilename}")
