#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import operator
import numpy as np

print('-' * 100)

print(2 * 3 * 4 * 5)
print(functools.reduce(lambda a,b: a*b, range(1, 6)))

print('-' * 100)

n = 0
for i in range(1, 6):
    n ^= i
print (n)

print(functools.reduce(lambda a, b: a^b, range(6)))
print(functools.reduce(operator.xor, range(6)))

print('-' * 100)

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
print('functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list]):')
print(functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list]))
print('functools.reduce(lambda a, b: a + b[1], my_list, 0):')
print(functools.reduce(lambda a, b: a + b[1], my_list, 0))
my_array = np.array(my_list)
print('np.sum(my_array[:, 1]):')
print(np.sum(my_array[:, 1]))
print('functools.reduce(operator.add, [sub[1] for sub in my_list], 0):')
print(functools.reduce(operator.add, [sub[1] for sub in my_list], 0))
t = 0
for sub in my_list:
    t += sub[1]
print('t=0\nfor sub in my_list:\n\tt += sub[1]')
print(t)
print('sum([sub[1] for sub in my_list]):')
print(sum([sub[1] for sub in my_list]))
print('sum(sub[1] for sub in my_list):')
print(sum(sub[1] for sub in my_list))

print('-' * 100)
