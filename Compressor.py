import numpy as np
from PIL import Image

def Smallen(im_arr):

    ## Image Data
    colors = 3

    ## Get Picture Dimensions
    y_dim = len(im_arr)
    row_arr = im_arr[0]
    x_dim = len(row_arr)
    # print(f"Dimensions: {x_dim}, {y_dim}")

    ## Make Averages
    avg_x_dim = x_dim//2
    avg_y_dim = y_dim//2
    # print(f"Avg. Dimensions: {avg_x_dim}, {avg_y_dim}")
    avg_im_arr = np.zeros((avg_y_dim, avg_x_dim, 3), dtype=np.uint8)
    avg_im_arr[:, :, :] = 100

    for y in range (0, y_dim-1, 2):
        for x in range (0, x_dim-1, 2):
            row = im_arr[y]
            rowD = im_arr[y+1]
            xypix = row[x]
            xyDpix = rowD[x]
            xUypix = row[x+1]
            xUyUpix = rowD[x+1]
            for clr in range (colors):
                clrresult = (int(xypix[clr]) + int(xyDpix[clr]) + int(xUypix[clr]) + int(xUyUpix[clr]))
                avg_im_arr[y//2, x//2, clr] = clrresult/4

    return avg_im_arr
