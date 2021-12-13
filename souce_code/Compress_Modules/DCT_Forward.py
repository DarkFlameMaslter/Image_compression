import numpy as np
import math as m

def DCT_block(block):
    N = block.shape[0]
    new_block = np.zeros(block.shape)
    # print('test: ' + str(block.shape))
    for v in range(N):
        for u in range(N):
            temp = 0
            for x in range(N):
                for y in range(N):
                    a = m.cos((2*x +1)*u*m.pi / 16 )
                    b = m.cos((2*y +1)*v*m.pi / 16 )
                    temp = temp + (block[x,y]*a*b)
            Cv = m.sqrt(1/2) if v == 0 else 1
            Cu = m.sqrt(1/2) if v == 0 else 1
            new_block[v,u] = temp*Cv*Cu*(1/4)
    return new_block




#Test_data
