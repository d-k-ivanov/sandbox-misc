#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from decimal import Decimal
from decimal import getcontext

@functools.lru_cache()
def fibonacci(n):
    getcontext().prec = 100
    if n < 2:
        return n
    return Decimal(fibonacci(n-2) + fibonacci(n-1))

def fibonacci_list(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def fibonacci3(n, computed = {0: 0, 1: 1}):
    getcontext().prec = 100
    if n not in computed:
        computed[n] = Decimal(fibonacci3(n-1, computed) + fibonacci3(n-2, computed))
    return computed[n]

def fibonacci4(n):
    getcontext().prec = 100
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return Decimal(a)

for i in range(1, 101):
   print('{:4} -> {:.220f}'.format(i, fibonacci(i+1)/fibonacci(i)))

print()

for i in range(1, 101):
   print('{:4} -> {:.100f}'.format(i, fibonacci3(i+1)/fibonacci3(i)))

print()

for i in range(1, 101):
   print('{:4} -> {:.200f}'.format(i, fibonacci3(i+1)/fibonacci3(i)))

print()

print(fibonacci_list(101))
