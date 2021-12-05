from Image_pre_process import img_pre_prs, craft_img
from DCT_Forward import DCT_block
from Quantazation import Lquant,Cquant
# from HuffmanCoding import read_block_coef_zig_zac, Huffman_encoding
# from Bin_encoding import encoding_bin

from re_Quantazation import re_Lquant,re_Cquant
from re_DCT import iDCT_block
from re_image_restore import restore

import os
import numpy as np

img_path = './Test_data/ngot.jpg'
print('Image Path: '+str(img_path))

blocks = img_pre_prs(img_path)
Y_blocks = blocks[0]
Cb_blocks = blocks[1]
Cr_blocks = blocks[2]

#DCT & Quant
#DCT forward all image & quantazation
for i in range(len(Y_blocks)):
    Y_blocks[i] = Y_blocks[i] - 128
    Y_blocks[i] = DCT_block(Y_blocks[i])
    Y_blocks[i] = Lquant(Y_blocks[i])


for i in range(len(Cb_blocks)):
    Cb_blocks[i] = Cb_blocks[i] - 128
    Cb_blocks[i] = DCT_block(Cb_blocks[i])
    Cb_blocks[i] = Cquant(Cb_blocks[i])

for i in range(len(Cr_blocks)):
    Cr_blocks[i] = Cr_blocks[i] - 128
    Cr_blocks[i] = DCT_block(Cr_blocks[i])
    Cr_blocks[i] = Cquant(Cr_blocks[i])

#reverse
re_Y = Y_blocks
re_Cb = Cb_blocks
re_Cr = Cr_blocks

for i in range(len(re_Y)):
    re_Y[i] = re_Lquant(re_Y[i])
    re_Y[i] = iDCT_block(re_Y[i])
    re_Y[i] = re_Y[i] + 128

for i in range(len(re_Cb)):
    re_Cb[i] = re_Cquant(re_Cb[i])
    re_Cb[i] = iDCT_block(re_Cb[i])
    re_Cb[i] = re_Cb[i] + 128

for i in range(len(re_Cr)):
    re_Cr[i] = re_Cquant(re_Cr[i])
    re_Cr[i] = iDCT_block(re_Cr[i])
    re_Cr[i] = re_Cr[i] + 128

re_img = restore(img_path, re_Y, re_Cb, re_Cr)
ori_img = craft_img(img_path)
#caculate MSE and PSNR
MSE_Y = 0
MSE_Cb = 0
MSE_Cr = 0

MN = re_img.shape[0]*re_img.shape[1]

for i in range(re_img.shape[0]):
    for j in range(re_img.shape[1]):
         MSE_Y += ((ori_img[i:j:0] - re_img[i:j:0])**2)/MN

for i in range(re_img.shape[0]):
    for j in range(re_img.shape[1]):
         MSE_Cb += ((ori_img[i:j:1] - re_img[i:j:1])**2)/MN

for i in range(re_img.shape[0]):
    for j in range(re_img.shape[1]):
         MSE_Y += ((ori_img[i:j:2] - re_img[i:j:2])**2)/MN

print('MSE Y channel: '+ str(MSE_Y))
print('MSE Cb channel: '+str(MSE_Cb))
print('MSE Cr channel: '+str(MSE_Cr))
