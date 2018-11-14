#!/use/bin/env python
# -*- coding: utf-8 -*-

from array import array
from random import random, seed
from datetime import datetime
from os import path
import pickle

seed(int(datetime.now().timestamp()))

binary_file = path.join(path.dirname(path.realpath(__file__)), 'f_arr.pickle')

f_arr = array('d', (random() for i in range(10**7)))
print(f_arr[-1])

with open(binary_file, 'wb') as fp_f_arr:
    pickle.dump(f_arr, fp_f_arr, protocol=pickle.HIGHEST_PROTOCOL)

f_arr2 = array('d')
with open(binary_file, 'rb') as fp_f_arr2:
    f_arr2 = pickle.load(fp_f_arr2)

print(f_arr2[-1])
print(f_arr[-1] == f_arr2[-1])
