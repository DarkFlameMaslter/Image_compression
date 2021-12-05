import os
import struct
# os.system('mkdir Final.txt')
curr = os.getcwd()
path = os.path.join(curr,'Final.txt')
# print(path)
# f = open(path,'w')
# f.write('test_string')
# f = open(path, 'w')


def writing(final_seq, path = path):
    with open(path, "wb") as f:
        for j in range(len(final_seq)):
            bits = final_seq[j]
            for k in range(len(bits)):
                int_value = int(bits[k], base=2)
                bin_array = struct.pack('b', int_value)
                f.write(bin_array)
