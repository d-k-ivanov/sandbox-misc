#!/use/bin/env python
# -*- coding: utf-8 -*-

import array

print('---------------------------------------------------------------------------')

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv)

memv_oct = memv.cast('B')
print(type(memv_oct))
print(memv_oct)
print(memv_oct.tolist())
print(len(memv_oct))
print(memv_oct[5])
memv_oct[5] = 4
print(memv_oct.tolist())

print('---------------------------------------------------------------------------')

import time
for n in (100000, 200000, 300000, 400000):
    data = b'x' * n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes', n, time.time()-start)

for n in (1000000, 2000000, 3000000, 4000000):
    data = b'x' * n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)

print('---------------------------------------------------------------------------')
