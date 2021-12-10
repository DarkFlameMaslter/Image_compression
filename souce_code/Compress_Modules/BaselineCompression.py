from Image_pre_process import img_pre_prs as preprocess
from DCT_Forward import DCT_block
from Quantazation import Lquant, Cquant
from HuffmanCoding import read_block_coef_zig_zac, Huffman_encoding
from Bin_encoding import encoding_bin

import os
import numpy as np

img_path = ''
print(img_path)

blocks = preprocess(img_path) #return 3 list of blocks of 3 color channel

#dividing channel:
Y = blocks[0]
Cb = blocks[1]
Cr = blocks[2]

#forward Y channel of image
for i in range(len(Y)):
    block = Y[i]
    for j in range(len(block)):
        for 
