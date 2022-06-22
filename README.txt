Quick and simple picture file compressor and decompressor (for .png and .jpg)

USAGE:
1.
To use, throw and .png images into the same folder as the rest of the .py and .bat files and use "Compress Image.bat"
This will simply create an image with the same filename but with "_Compressed_" added to its name. The image is just a half-resolution picture of the original with one pixel representing the average of four from the original.

(As that last step actually gets rid of a lot of data, it took a long time to find a decompressor that would actually work reasonably well)

2.
Then, when uncompressing the images, throw the "..._Compressed_.png" pictures into the primary file again and use the "Uncompress Image.bat" file.
This will create the regenerated images with the tag "(UnCompressed)" slapped on.
For almost all cases, you can ignore the "Sharpening Factor" input that appears. All this does is repeat the sharpening algorithm the amount of times given by the input. This can be good to have for images that had poor quality in the original image (i.e. highly pixelated example mentioned at bottom). The maxmium I could see being used is 3, although a factor of 2 does seem to do enough when needed.

Misc Notes:
- If your pictures aren't being recognized by the code, make sure the file name doesnt have "_" or ")" at the end. I claim these symbols for checking for filenames to compress and decompress.
- Sharpener.py is a simple algorithm used to sharpen the image. Reference the wikipedia page on "Unsharp Masking", specifically the digital method. This was a very simply algorithm that worked supringly well, but for higher quality images, the sharpening looks a bit cheap.

Misc Data Notes:
I tested a handful of images so here's some of the values and stuff
Format of:	(Original Size -> Compressed Size -> Uncompressed Size), R = ...
& R is compression ratio of (1 - 'Compressed Size' / 'Original Size'), so 0 to 1, with 1 as best

1. First Tests (only .png types recognized in code)
    i. 830x722 image: (494 KB -> 161 KB -> 508 KB)                                  R = 0.674
    ii. Same as prev but very blurry: (224 KB -> 102 KB -> 277 KB)                  R = 0.544
    iii. 60x60 color wheel: (4 KB -> 2 KB -> 5KB)                                   R = 0.500
    iv. 451x451 very sharp pic: (291 KB -> 80KB -> 261KB)                           R = 0.725
    v. 1439x749 monitor screenshot: (798 KB -> 205 KB -> 677KB)		            R = 0.743
    vi. 637x631 pic of a dog surrounded by bread: (1057 KB -> 199 KB -> 634 KB)	    R = 0.812
    vii. 728x405 orginally .jpg pic: (53 KB -> 107 KB -> 342 KB)                    R = -1.019*
    viii. 512x341 pixleated (originally a .jpg) pic (99 KB - > 99 KB - > 334 KB)    R = 0*
    ix. 1444x904 monitor screenshot: (716 KB -> 188 KB -> 686 KB)		    R = 0.737
    
    - The screenshots proved to be good limitations for the current code. The images are quite sharp (as computer monitor graphics are) so some smaller             text is slightly hard to read. Applying some anti aliasing to these images would probably be the best simple solution.

    * These images were originally .jpg but I hardconverted them to .png by changing their name. As shown in 2. it is much better to be able to use the             original filetype:

2. New results (with .png and .jpg as recognized filetypes)
    i. 728x450 image retested: (53 KB -> 12 KB - > 31KB)                    R = 0.774 (better!)
    ii. 512x341 pixleated image: (99 KB -> 14 KB -> 40 KB)                  R = 0.859**

    **I very much like this value, but addmitedly, the uncompressed image did not look very good due to the highly pixleated nature of the original                 image. It's still much better than the test in 1.viii. however!
