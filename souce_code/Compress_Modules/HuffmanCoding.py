import math as m
import numpy as np

def read_block_coef_zig_zac(block):
    sequence =[]
    sequence.append(block[0,0])
    sequence.append(block[0,1])
    sequence.append(block[1,0])
    sequence.append(block[2,0])
    sequence.append(block[1,1])
    sequence.append(block[0,2])
    sequence.append(block[0,3])
    sequence.append(block[1,2])
    sequence.append(block[2,1])
    sequence.append(block[3,0])
    sequence.append(block[4,0])
    sequence.append(block[3,1])
    sequence.append(block[2,2])
    sequence.append(block[1,3])
    sequence.append(block[0,4])
    sequence.append(block[0,5])
    sequence.append(block[1,4])
    sequence.append(block[2,3])
    sequence.append(block[3,2])
    sequence.append(block[4,1])
    sequence.append(block[5,0])
    sequence.append(block[6,0])
    sequence.append(block[5,1])
    sequence.append(block[4,2])
    sequence.append(block[3,3])
    sequence.append(block[2,4])
    sequence.append(block[1,5])
    sequence.append(block[0,6])
    sequence.append(block[0,7])
    sequence.append(block[1,6])
    sequence.append(block[2,5])
    sequence.append(block[3,4])
    sequence.append(block[4,3])
    sequence.append(block[5,2])
    sequence.append(block[6,1])
    sequence.append(block[7,0])
    sequence.append(block[7,1])
    sequence.append(block[6,2])
    sequence.append(block[5,3])
    sequence.append(block[4,4])
    sequence.append(block[3,5])
    sequence.append(block[2,6])
    sequence.append(block[1,7])
    sequence.append(block[2,7])
    sequence.append(block[3,6])
    sequence.append(block[4,5])
    sequence.append(block[5,4])
    sequence.append(block[6,3])
    sequence.append(block[7,2])
    sequence.append(block[7,3])
    sequence.append(block[6,4])
    sequence.append(block[5,5])
    sequence.append(block[4,6])
    sequence.append(block[3,7])
    sequence.append(block[4,7])
    sequence.append(block[5,6])
    sequence.append(block[6,5])
    sequence.append(block[7,4])
    sequence.append(block[7,5])
    sequence.append(block[6,6])
    sequence.append(block[5,7])
    sequence.append(block[6,7])
    sequence.append(block[7,6])
    sequence.append(block[7,7])
    return sequence

"""
returned a list of coefficient with the very first is the
DC coefficient
now encoding to compress the image
"""

def DC_encoding(previous_DC, Coe_list):
    DC_Coe = previous_DC - Coe_list[0]
    cat = 0
    if(DC_Coe ==0):
        cat = 0
    else:
        cat = m.floor(m.log2(abs(DC_Coe)))+1
    return cat,DC_Coe

def AC_encoding(Coe_list, new_sequence):
    count = 0
    for i in range(1,len(Coe_list)):
        if(Coe_list[i]) == 0:
            count = count + 1
            if count == 16:
                new_sequence.append('ZRL')
                count = 0
        else:
            new_sequence.append([count,Coe_list[i]])
            count = 0
    new_sequence.append('EOB')


def Huffman_encoding(previous_seq, sequence):
    new_sequence = []
    # print('test123: '+str(previous_seq[0]) +' '+str(sequence[0]))
    temp = DC_encoding(previous_seq[0],sequence)
    # sequence[0] = temp[1]
    new_sequence.append([temp[0],temp[1]])
    AC_encoding(sequence, new_sequence)
    return new_sequence
