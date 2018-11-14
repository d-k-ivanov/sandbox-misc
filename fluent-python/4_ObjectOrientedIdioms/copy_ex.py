#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('-' * 100)

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
print('Bus1: ' + str(bus1.passengers))
print('Bus2: ' + str(bus2.passengers))
print('Bus3: ' + str(bus3.passengers))
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
bus1.drop('Bill')
print('Bus1: ' + str(bus1.passengers))
print('Bus2: ' + str(bus2.passengers))
print('Bus3: ' + str(bus3.passengers))

print('-' * 100)

a = [10, 20]
b = [a, 30]
print(id(a), a)
print(id(b), b)
a.append(b)
print(id(a), a)
c = copy.deepcopy(a)
d = copy.copy(a)
e = a
print(id(c), c)
print(id(d), d)
print(id(e), e)

print('-' * 100)

for item in a:
    print('{0:15} -> {1}'.format(str(id(item)), item))

print('-' * 100)

for item in b:
    print('{0:15} -> {1}'.format(str(id(item)), item))

print('-' * 100)

for item in c:
    print('{0:15} -> {1}'.format(str(id(item)), item))

print('-' * 100)

for item in d:
    print('{0:15} -> {1}'.format(str(id(item)), item))

print('-' * 100)

for item in e:
    print('{0:15} -> {1}'.format(str(id(item)), item))

print('-' * 100)
