#!/use/bin/env python
# -*- coding: utf-8 -*-

from array import array
from random import random, seed, uniform
from datetime import datetime

seed(int(datetime.now().timestamp()))

f_arr = array('d', (uniform(0.0, 1.0) for i in range(10**7)))
print('{:.32f}'.format(f_arr[0]))
print('{:.32f}'.format(f_arr[-1]))

f_arr = array(f_arr.typecode, sorted(f_arr))
print('{:.32f}'.format(f_arr[0]))
print('{:.32f}'.format(f_arr[-1]))
