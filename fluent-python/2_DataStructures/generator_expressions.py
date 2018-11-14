#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array

string_of_symbols = 'Generator Expressions $¢£¥€¤'
print('-------------------- Tuple in memory Generator ----------------------------')
print(tuple(ord(s) for s in string_of_symbols))

print('---------------------------------------------------------------------------')
print(array.array('I',(ord(s) for s in string_of_symbols)))

print('-------------------- In Memory Cartesian Products -------------------------')
colors = ['black', 'white', 'green']
sizes = ['XS','S','M','L','XL','XXL','XXXL']
for tshirt in ('%s, %s' % (c, s) for c in colors
                                 for s in sizes):
    print(tshirt)
print('---------------------------------------------------------------------------')

