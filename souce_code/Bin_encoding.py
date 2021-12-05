import math as m
import numpy as np

DC_Coe_bin_encoder = {
0:'00',
1:'010',
2:'011',
3:'100',
4:'101',
5:'110',
6:'1110',
7:'11110',
8:'111110',
9:'1111110',
10:'111111110',
11:'1111111110'
}

def encoding_bin(seq):
    bin_seq = ''
    #encodingDC
    DC_coe = seq[0]
    bin_seq += str(DC_Coe_bin_encoder[DC_coe[0]])
    temp_bin = str((bin(abs(int(DC_coe[1])))))
    # print('test DC bin encoding: ')
    # print('DC = '+str(DC_coe[1]))
    # print('cat : '+str(DC_coe[0]) +' bin : '+ str(DC_Coe_bin_encoder[DC_coe[0]]))
    # print('bin = '+str(bin(abs(int(DC_coe[1])))))
    # print('temp bin = '+ bin_seq)
    if DC_coe[1]>0:
        bin_seq += temp_bin[2:]
    else:
        for i in range(2,len(temp_bin)):
            if(temp_bin[i] == '1'):
                bin_seq += '0'
            else:
                bin_seq += '1'
    # print('bin_seq: '+bin_seq)
    #encoding AC
    # print('AC encoding: ')
    for i in range(1,len(seq[1:])):
        AC_coe = seq[i]
        if AC_coe == 'ZRL':
            bin_seq += '11110000'
        elif AC_coe == 'EOB':
            bin_seq += '00000000'
        else:
            rrrr = AC_coe[0]
            coe = AC_coe[1]
            ssss = m.floor(m.log2(abs(coe)))+1
            bin_seq += str(DC_Coe_bin_encoder[rrrr])
            bin_seq += str(DC_Coe_bin_encoder[ssss])
            temp_bin = str((bin(abs(int(coe)))))
            if coe>0:
                bin_seq += temp_bin[2:]
            else:
                for i in range(2,len(temp_bin)):
                    if(temp_bin[i] == '1'):
                        bin_seq += '0'
                    else:
                        bin_seq += '1'
            # print('check point:')
            # print(seq[i])
            # print(bin_seq)
    print('check point: ')
    print(seq)
    print(bin_seq)

    return bin_seq
