from Image_pre_process import img_pre_prs
from DCT_Forward import DCT_block
from
import os

currpath = os.getcwd()
img_path = os.path.join(currpath, "souce_code/souce_code/Test_data/Miko.jpeg")
print(img_path)
blocks = img_pre_prs(img_path)
print(blocks[0])
blocks = blocks[:4]


def DCT_All_image(blocks):
    for i in range(len(blocks)):
        blocks[i] = blocks[i]-128
        blocks[i] = DCT_block(blocks[i])

        print('complete DCT for block: '+str(i))
    return blocks

blocks = DCT_All_image(blocks)
print('DCT complete')
print(blocks[0])
