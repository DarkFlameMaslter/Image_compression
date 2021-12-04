import math as m
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

def get_Y_Cb_Cr_img(path):
    img = cv.imread(path)
    img_ = Image.open(path)
    plt.imshow(img_)
    plt.show()
    img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
    return img

def dividing_blocks(img):
    # print('image shape: '+ str(img.shape))
    height_index = (img.shape[0]//8)-1
    weight_index = (img.shape[1]//8)-1
    blocks = []
    for n in range(3):
        for i in range(weight_index):
            for j in range(height_index):
                blocks.append(img[j*8:(j+1)*8,i*8:(i+1)*8,n])

    return blocks

def img_pre_prs(path):
    img = get_Y_Cb_Cr_img(path)
    print('image shape = '+ str(img.shape))
    print('image size = ' + str(img.size))
    blocks = dividing_blocks(img)
    print('number of blocks: '+str(len(blocks)))
    return blocks
#test
# path = './Test_data/Miko.jpeg'
# img_pre_prs(path)




#test zone
