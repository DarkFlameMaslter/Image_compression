import math as m
import numpy as np

LQM = np.asarray([[16 ,11 ,10 ,16 ,24 ,40 ,51 ,61],
       [12 ,12 ,14 ,19 ,26 ,58 ,60 ,55],
       [14 ,13 ,16 ,24 ,40 ,57 ,69 ,56],
       [14 ,17 ,22 ,29 ,51 ,87 ,80 ,62],
       [18 ,22 ,37 ,56 ,68 ,109 ,103 ,77],
       [24 ,35 ,55 ,64 ,81 ,104 ,113 ,92],
       [49 ,64 ,78 ,87 ,103 ,121 ,120 ,101],
       [72 ,92 ,95 ,98 ,112 ,100 ,103 ,99]])

CQM = np.asarray(
    [
    [17,18,24,47,99,99,99,99],
    [18,21,26,66,99,99,99,99],
    [24,26,56,99,99,99,99,99],
    [47,66,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99]
    ]
)

def re_Lquant(block, QM = LQM):
    N = block.shape[0]
    output = np.zeros(block.shape, dtype = 'int16')
    for i in range(N):
        for j in range(N):
            output[i,j] = block[i,j]*QM[i,j]
    return output

def re_Cquant(block, QM = CQM):
    N = block.shape[0]
    output = np.zeros(block.shape, dtype = 'int16')
    for i in range(N):
        for j in range(N):
            output[i,j] = block[i,j]*QM[i,j]
    return output
