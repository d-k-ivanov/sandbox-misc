#!/use/bin/env python
# -*- coding: utf-8 -*-

from array import array
from random import random, seed
from datetime import datetime
from os import path

seed(int(datetime.now().timestamp()))

binary_file = path.join(path.dirname(path.realpath(__file__)), 'f_arr.bin')

f_arr = array('d', (random() for i in range(10**7)))
print(f_arr[-1])

fp_f_arr = open(binary_file, 'wb')
f_arr.tofile(fp_f_arr)
fp_f_arr.close()

f_arr2 = array('d')
with open(binary_file, 'rb') as fp_f_arr2:
    f_arr2.fromfile(fp_f_arr2, 10**7)
#fp_f_arr2.close()
print(f_arr2[-1])
print(f_arr[-1] == f_arr2[-1])
