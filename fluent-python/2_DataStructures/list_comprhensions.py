#!/usr/bin/env python
# -*- coding: utf-8 -*-

string_of_symbols = 'List Comprehensions $¢£¥€¤'

print('-------------------- List Append with For ----------------------------')
codes1 = []
for s in string_of_symbols:
    codes1.append(ord(s))
print(codes1)

print('-------------------- List Comprehention ------------------------------')

codes2 = [ord(s) for s in string_of_symbols]
print(codes2)

print('----------------------------------------------------------------------')

x = 'Shiny string one'
dummy = [x for x in 'ABCDEFJHIJK']
print(x)
print(dummy)

print('----------------------------------------------------------------------')

beyond_ascii_table1 =  [ord(s) for s in string_of_symbols if ord(s) > 127]
print(beyond_ascii_table1)

print('----------------------------------------------------------------------')

beyond_ascii_table2 = list(filter(lambda c: c > 127, map(ord, string_of_symbols)))
print(beyond_ascii_table2)

print('-------------------- Cartesian Products ------------------------------')
colors = ['black', 'white', 'green']
sizes = ['XS','S','M','L','XL','XXL','XXXL']
tshirts1 = [(color, size) for color in colors
                          for size in sizes]
print(tshirts1)
print('----------------------------------------------------------------------')
tshirts2 = [(color, size) for size in sizes for color in colors]
print(tshirts2)

print('----------------------------------------------------------------------')
