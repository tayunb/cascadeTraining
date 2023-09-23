import os
import cv2

files = os.listdir('pos_top')

with open('info.dat', 'w') as f:
    for file in files:
        img = cv2.imread('pos_top/'+file)

        width = img.shape[1]
        height = img.shape[0]

        f.write('pos_top/'+file+' 1 0 0 '+str(width)+' '+str(height)+'\n')
    