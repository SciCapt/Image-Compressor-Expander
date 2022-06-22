import numpy as np
from PIL import Image

def Bigen(im_arr):

    'Imageis Expandous!'

    ## Image Data
    colors = 3

    ## Get Picture Dimensions
    y_dim = len(im_arr)
    row_arr = im_arr[0]
    x_dim = len(row_arr)
    # print(f"\nDimensions: {x_dim}, {y_dim}")

    ## Make Larger Array
    exp_x_dim = x_dim*2
    exp_y_dim = y_dim*2
    # print(f"Expanded Dimensions: {exp_x_dim}, {exp_y_dim}")
    exp_im_arr = np.zeros((exp_y_dim, exp_x_dim, colors), dtype=np.uint8)
    exp_im_arr[:, :, :] = 0

    time = 1*10**-5 * x_dim * y_dim
    # print(f"Estimated Time to Complete: {(4*time)} Seconds")

    ## Phase I Image Expansion (netting image)
    for y in range (0, exp_y_dim-1, 2):
        for x in range (0, exp_x_dim-1, 2):
            for z in range (colors):
                exp_im_arr[y, x, z] = im_arr[y//2, x//2, z]

    ## Phase II Image Expansion (row 0, 2, 4, ... net coloring)
    for y in range (0, exp_y_dim-1, 2):
        for x in range (1, exp_x_dim-1, 2):
            row = exp_im_arr[y]
            pixL = row[x-1]
            pixR = row[x+1]
            for z in range (colors):
                avg_color = (int(pixL[z]) + int(pixR[z]))/2
                exp_im_arr[y,x,z] = avg_color

    ## Phase III Image Expansion (row 1, 3, 5, ... net coloring)
    for y in range (1, exp_y_dim-1, 2):
        for x in range (0, exp_x_dim-1, 1):
            rowU = exp_im_arr[y-1]
            rowD = exp_im_arr[y+1]
            pixU = rowU[x]
            pixD = rowD[x]
            for z in range (colors):
                avg_clr = (int(pixU[z]) + int(pixD[z]))/2
                exp_im_arr[y,x,z] = avg_clr

    return exp_im_arr
