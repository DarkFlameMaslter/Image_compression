from Image_pre_process import img_pre_prs
from DCT_Forward import DCT_block
from Quantazation import Lquant,Cquant
from HuffmanCoding import read_block_coef_zig_zac, Huffman_encoding
from Bin_encoding import encoding_bin

import os
import numpy as np

#get the image and convert to Y_Cb_Cr

img_path = './Test_data/ngot.jpg'
print('Image Path: '+str(img_path))

blocks = img_pre_prs(img_path)
Y_blocks = blocks[0]
Cb_blocks = blocks[1]
Cr_blocks = blocks[2]

print('begin DCT: ')
print('sample blocks:')
print(Y_blocks[0])
print('Centering Blocks:')
temp = Y_blocks[0] - 128
print(temp)
print('DCT block: ')
temp = DCT_block(temp)
print('quantazation: ')
temp = Lquant(temp)
print(temp)
# #DCT forward all image & quantazation
# for i in range(len(Y_blocks)):
#     Y_blocks[i] = Y_blocks[i] - 128
#     Y_blocks[i] = DCT_block(Y_blocks[i])
#     Y_blocks[i] = Lquant(Y_blocks[i])
"""
in case you want to turn your computer and micro-processor become a camp-fire, then take your chance

for i in range(len(Cb_blocks)):
    Cb_blocks[i] = Cb_blocks[i] - 128
    Cb_blocks[i] = DCT_block(Cb_blocks[i])
    Cb_blocks[i] = Cquant(Cb_blocks[i])

for i in range(len(Cr_blocks)):
    Cr_blocks[i] = Cr_blocks[i] - 128
    Cr_blocks[i] = DCT_block(Cr_blocks[i])
    Cr_blocks[i] = Cquant(Cr_blocks[i])
"""
#turn blocks to a chain of chains
sequence = []
# for i in range(len(Y_blocks)):
#     sequence.append(read_block_coef_zig_zac(Y_blocks[i]))
sequence.append(read_block_coef_zig_zac(temp))
print("scan complete!")
print("number of sequences: "+str(len(sequence)))
print("test sequence: ")
print(sequence[0])

#convert ordinary sequence to a chain of Huffman coded
new_sequence = []
temp_block = np.zeros((8,8))
temp_sequence = read_block_coef_zig_zac(temp_block)
# for i in range(len(Y_blocks)):
#     new_sequence.append(Huffman_encoding(Y_blocks[i]))
new_sequence.append(Huffman_encoding(temp_sequence, sequence[0]))
print('encoded!')
print('test encoded sequence:')
print(new_sequence[0])

print('binary encoding:')
bin_seq = []
bin_seq.append(encoding_bin(new_sequence[0]))
print(bin_seq)
