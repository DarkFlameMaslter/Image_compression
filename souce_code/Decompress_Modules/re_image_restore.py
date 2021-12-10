import math as m
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

def restore(path,Y,Cb,Cr):
    img = cv.imread(path)
    new_img = np.zeros(img.shape, dtype = 'int')

    height_index = (img.shape[0]//8)-1
    weight_index = (img.shape[1]//8)-1
    #restore Y channel
    count = 0
    for i in range(weight_index):
        for j in range(height_index):
            new_img[j*8:(j+1)*8,i*8:(i+1)*8,0] = Y[count]
            count += 1

    # restore Cb channel
    count = 0
    for i in range(weight_index):
        for j in range(height_index):
            new_img[j*8:(j+1)*8,i*8:(i+1)*8,1] = Cb[count]
            count += 1

    # restore Cr channel
    count = 0
    for i in range(weight_index):
        for j in range(height_index):
            new_img[j*8:(j+1)*8,i*8:(i+1)*8,2] = Cr[count]
            count += 1

    plt.imshow(new_img, cmap = 'gray')
    plt.show()

    return new_img
