#!/usr/bin/env python
# -*- coding: utf-8 -*-

def decorator(func):
    def inner_func():
        print('Running inner function')
    return inner_func

@decorator
def target():
    print('running target()')


print('---------------------------------------------------------------------------')

target()

print('---------------------------------------------------------------------------')

import registration

print('---------------------------------------------------------------------------')
