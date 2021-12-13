import numpy as np
import math as m

def iDCT_block(block):
    N = block.shape[0]
    new_block = np.zeros(block.shape)

    for x in range(N):
        for y in range(N):
            temp = 0
            for v in range(N):
                for u in range(N):
                    a = m.cos((2*x +1)*u*m.pi / 16 )
                    b = m.cos((2*y +1)*v*m.pi / 16 )

                    Cv = m.sqrt(1/2) if v == 0 else 1
                    Cu = m.sqrt(1/2) if v == 0 else 1

                    temp = temp + Cu*Cv*a*b*block[v,u]
            new_block[x,y] = (1/4)*temp
    return new_block
