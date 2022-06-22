import os
from Compressor import Smallen
from Expander import Bigen
from PIL import Image
import numpy as np
from Sharpen import *

# Get Files in current Directory
filelist = os.listdir()

# Get Image Filename
for i in range(len(filelist)):
    file = filelist[i]
    checkExtension = file[len(file)-5:len(file)]
    possibleExtensions = ["_.png", "_.PNG", "_.jpg", "_.JPG"]
    for e in range(len(possibleExtensions)):
        if checkExtension == possibleExtensions[e]:
            if file[len(file)-5] != ")":
                filename = file

                # Make Image Data Array
                with Image.open(str(filename)) as image:
                    pic = np.fromstring(image.tobytes(), dtype=np.uint8)
                    pic = pic.reshape((image.size[1], image.size[0], 3))

                # Unzip/Sharpen Image
                pic = Bigen(pic)
                try:
                    iterations = int(input("\nSharpening Factor (Default is 1): "))
                    iterations = max(iterations, 0)
                except:
                    iterations = 1
                for int in range(iterations):
                    pic = Sharpen(pic)

                # Naming Stuff
                shortFilename = filename[0:len(filename)-4]
                extension = filename[len(filename)-4:len(filename)]
                newFilename = f"{shortFilename}(UnCompressed){extension}"

                # Save File
                pic = Image.fromarray(pic)
                pic.save(newFilename)
                print(f"\nUncompressed Image Saved as: {newFilename}")
