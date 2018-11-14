#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clock_decorator import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print('---------------------------------------------------------------------------')
    print(fibonacci(6))
    print('---------------------------------------------------------------------------')
    # print(fibonacci(30)) # It takes very long time to execute
    print('---------------------------------------------------------------------------')

