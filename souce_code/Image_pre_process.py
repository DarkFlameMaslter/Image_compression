import math as m
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

def get_Y_Cb_Cr_img(path):
    img = cv.imread(path)
    # img_ = Image.open(path)
    plt.imshow(img, cmap = 'gray')
    plt.show()
    img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
    return img

def dividing_blocks(img):
    # print('image shape: '+ str(img.shape))
    height_index = (img.shape[0]//8)-1
    weight_index = (img.shape[1]//8)-1
    total_blocks = []
    blocks = []
    for n in range(3):
        for i in range(weight_index):
            for j in range(height_index):
                blocks.append(img[j*8:(j+1)*8,i*8:(i+1)*8,n])
        total_blocks.append(blocks)
        blocks = []
    return total_blocks

def img_pre_prs(path):
    img = get_Y_Cb_Cr_img(path)
    print('image shape = '+ str(img.shape))
    print('image size = ' + str(img.size))
    blocks = dividing_blocks(img)
    print('number of blocks: '+str(len(blocks[0]))+ ' per 3 color channel')
    return blocks

def craft_img(path):
    img = cv.imread(path)
    img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
    new_img = np.zeros(img.shape, dtype = 'int')
    height_index = (img.shape[0]//8)
    weight_index = (img.shape[1]//8)

    for n in range(3):
        new_img[:height_index*8, :weight_index*8,n] = img[:height_index*8, :weight_index*8,n]
#test
# path = './Test_data/Miko.jpeg'
# img_pre_prs(path)




#test zone
