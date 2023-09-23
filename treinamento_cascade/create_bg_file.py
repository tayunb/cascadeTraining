import os

files = os.listdir('neg_top')
filename = 'bg.txt'

with open(filename, 'w') as f:
    for file in files:
        f.write('neg_top/'+file+'\n')
    