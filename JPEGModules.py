
import numpy as np
import math as m
import cv2 as cv

# get and convert img to YCbCr
def get_img(path):
    img = cv.imread(path)
    img_ = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
    return img_
img = get_img(path)
# block divider
def block_divider(img):
    height_index = img.shape[0]//8-1
    weight_index = img.shape[1]//8-1
    blocks = []
    for n in range(3)
        for i in range(weight_index):
            for j in range(height_index):
                blocks.append(blocks[i*8:(i+1)*8], j*8:(j+1)*8)
    return blocks
# DCT Forward
def DCT_Forward(block):
    N = block.shape[0]

    output = np.zeros(block.shape, dtype = 'double')
    for i in range(N):
        for j in range(N):
            #caculate FDCT
            Sum = 0

            for k in range(N):
                for l in range(N):
                    Sum = Sum + ( block[k,l]*math.cos( ((2*k)+1)*(i*math.pi)/16)*math.cos( ((2*l)+1)*(j*math.pi)/16))
            Cu = math.sqrt(1/2) if i == 0 else 1
            Cv = math.sqrt(1/2) if j == 0 else 1
            output[i,j]= (1/4)*Cu*Cv*Sum #output[i,j] be4 Quantazation
    return output

#quantazation matrix
QM = np.asarray([[16 ,11 ,10 ,16 ,24 ,40 ,51 ,61],
       [12 ,12 ,14 ,19 ,26 ,58 ,60 ,55],
       [14 ,13 ,16 ,24 ,40 ,57 ,69 ,56],
       [14 ,17 ,22 ,29 ,51 ,87 ,80 ,62],
       [18 ,22 ,37 ,56 ,68 ,109 ,103 ,77],
       [24 ,35 ,55 ,64 ,81 ,104 ,113 ,92],
       [49 ,64 ,78 ,87 ,103 ,121 ,120 ,101],
       [72 ,92 ,95 ,98 ,112 ,100 ,103 ,99]])
# Quantization
def quant(block, QM = QM):
    N = block.shape[0]
    output = np.zeros(block.shape, dtype = 'int16')
    for i in range(N):
        for j in range(N):
            output[i,j] = block[i,j]//QM[i,j]
    return output

# HuffMan encoding

#read blocks
def read_block(block)
