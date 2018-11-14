#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref
import time

print('-' * 100)

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)

print('-' * 100)

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
#time.sleep(5)
print(wref() is None)

# >>> import weakref
# >>> a_set = {0, 1}
# >>> wref = weakref.ref(a_set)
# >>> wref
# <weakref at 0x000002D49A8BD728; to 'set' at 0x000002D49AC254A8>
# >>> wref()
# {0, 1}
# >>> a_set = {2, 3, 4}
# >>> wref()
# {0, 1}
# >>> wref() is None
# False
# >>> wref() is None
# True

print('-' * 100)

class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese

print(str(sorted(stock.keys())))
del catalog
print(str(sorted(stock.keys())))
del cheese
print(str(sorted(stock.keys())))

print('-' * 100)

class MyList(list):
    """list subclass whose instances may be weakly referenced"""

a_list = MyList(range(10))
wref_to_a_list = weakref.ref(a_list)
print(wref_to_a_list)

print('-' * 100)

t1 = (1, 2, 3)
t2 = tuple(t1)
print('{}: {}'.format(id(t1), 't1'))
print('{}: {}'.format(id(t2), 't2'))
print('{}: {}'.format('t2 is t1', t2 is t1))
t3 = t1[:]
print('{}: {}'.format(id(t1), 't1'))
print('{}: {}'.format(id(t2), 't2'))
print('{}: {}'.format(id(t3), 't3'))
print('{}: {}'.format('t3 is t1', t3 is t1))
print('{}: {}'.format('t3 is t2', t3 is t2))

print('-' * 100)

t11 = (1,2,3)
t22 = (1,2,3)
print('{}: {}'.format('t22 is t11', t22 is t11))
s11 = 'ABC'
s22 = 'ABC'
print('{}: {}'.format('s22 is s11', s22 is s11))
s33 = 'why do pangolins dream of quiche'
s44 = 'why do pangolins dream of quiche'
print('{}: {}'.format('s44 is s33', s44 is s33))
i11 = '123'
i22 = '123'
print('{}: {}'.format('i11 is i22', i11 is i22))
i33 = '283'
i44 = '283'
print('{}: {}'.format('i33 is i44', i33 is i44))

print('-' * 100)
