import random
import kk

arr = kk.random_sequence(100)
file = open('inputfile.txt', 'w')

for i in arr:
    file.write(str(i) + '\n')

file.close()