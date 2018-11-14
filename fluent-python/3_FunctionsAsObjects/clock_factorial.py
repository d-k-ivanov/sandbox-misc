#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from clock_decorator import clock

@clock
def snooze(sec):
    time.sleep(sec)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

def factorial2(n):
    return 1 if n < 2 else n * factorial2(n-1)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123):')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6):')
    print('6! = ', factorial(6))
    print('*' * 40, 'Calling factorial2(6):')
    factorial2 = clock(factorial2)
    print('6! = ', factorial2(6))
    print('*' * 40, 'Calling factorial2(6):')
    factorial_clocked = clock(factorial2)
    print('6! = ', factorial_clocked(6))



