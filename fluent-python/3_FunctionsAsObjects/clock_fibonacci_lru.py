#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

from clock_decorator import clock

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@functools.lru_cache()
@clock
def fibonacci2(n): # Second function need to renew cached values
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)

if __name__=='__main__':
    print('---------------------------------------------------------------------------')
    print(fibonacci(6))
    print('---------------------------------------------------------------------------')
    print(fibonacci2(30))
    print('---------------------------------------------------------------------------')

