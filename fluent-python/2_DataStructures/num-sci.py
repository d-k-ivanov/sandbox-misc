#!/use/bin/env python
# -*- coding: utf-8 -*-

from os import path
from array import array
from random import random, seed, uniform
from datetime import datetime
from time import perf_counter as pc

import numpy

print('---------------------------------------------------------------------------')

a = numpy.arange(12)
print(a)
print(type(a))
print()

a.shape = 3, 4
print(a)
print()
print(a[2])
print(a[2, 1])
print(a[:, 1])

print()
print(a.transpose())

print('---------------------------------------------------------------------------')

floats_file = path.join(path.dirname(path.realpath(__file__)), 'floats-10M-lines.txt')
numpy_file = path.join(path.dirname(path.realpath(__file__)), 'floats-10M-lines.npy')

if not path.isfile(floats_file):
    print(floats_file + ' not found. Generating...')
    seed(int(datetime.now().timestamp()))
    f_arr = array('d', (uniform(0.0, 999999.0) for i in range(10**7)))
    with open(floats_file, 'w') as fp_floats_file:
        for f in f_arr:
            fp_floats_file.write("%s\n" % f)

floats = numpy.loadtxt(floats_file)
print(floats[-3:])
floats *= .5
print(floats[-3:])
print()

t0 = pc()
floats /= 3
print(pc() - t0)
print()

numpy.save(numpy_file, floats)

floats2 = numpy.load(numpy_file, 'r+')
floats2 *= 6
print(floats2[-3:])

print('---------------------------------------------------------------------------')

