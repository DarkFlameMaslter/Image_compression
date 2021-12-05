from Image_pre_process import img_pre_prs
from DCT_Forward import DCT_block
from Quantazation import quant
from HuffmanCoding import read_block_coef_zig_zac, Huffman_encoding
from Bin_encoding import encoding_bin
from To_file import writing

import os
import numpy as np
# currpath = os.getcwd()
# img_path = os.path.join(currpath, "souce_code/souce_code/Test_data/Miko.jpeg")
img_path = './Test_data/Miko.jpeg'
print(img_path)
blocks = img_pre_prs(img_path)
print(blocks[0])


def forward_All_image(blocks):
    for i in range(len(blocks)):
        blocks[i] = blocks[i]-128
        blocks[i] = DCT_block(blocks[i])
        blocks[i] = Yquant(blocks[i])
        print('complete quanta for block: '+str(i))
    return blocks

blocks = forward_All_image(blocks)
print('Quanta complete')
print(blocks)

sequence = []
for i in range(len(blocks)):
    sequence.append(read_block_coef_zig_zac(blocks[i]))
print('test sequence: length '+str(len(sequence)))
print(sequence)

temp_block = np.zeros((8,8))
temp_sequence = read_block_coef_zig_zac(temp_block)

new_sequence = []
new_sequence.append(Huffman_encoding(temp_sequence, sequence[0]))

for i in range(1,len(sequence)):
    new_sequence.append(Huffman_encoding(sequence[i-1], sequence[i]))
print('new sequence created:length '+str(len(sequence)))
print(new_sequence)

print('Seq bin encoding: ')
bin_seq = []
for i in range(len(new_sequence)):
    bin_seq.append(encoding_bin(new_sequence[i]))

print('final_seq: ')
print(bin_seq)
writing(bin_seq)
