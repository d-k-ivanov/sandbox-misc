#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dis

print('---------------------------- Average OOP ----------------------------------')

class Averager():

    def __init__(self):
        self.series1 = []

    def __call__(self, new_value1):
        self.series1.append(new_value1)
        total1 = sum(self.series1)
        return total1/len(self.series1)

avg1 = Averager()
print(avg1(10))
print(avg1(11))
print(avg1(12))

print('---------------------------------------------------------------------------')

#print(dis.dis(Averager))

print('---------------------------- Average functional ---------------------------')

def make_averager2():
    series2 = []

    def averager_inner2(new_value2):
        series2.append(new_value2)
        total2 = sum(series2)
        return total2/len(series2)

    return averager_inner2

avg2 = make_averager2()
print(avg2(10))
print(avg2(11))
print(avg2(12))

print('---------------------------------------------------------------------------')

# print(dis.dis(avg2))
print(avg2.__code__.co_varnames)
print(avg2.__code__.co_freevars)
print(avg2.__closure__)
print(avg2.__closure__[0].cell_contents)

print('---------------------------------------------------------------------------')

def make_averager3():
    count3 = 0
    total3 = 0

    def averager_inner3(new_value3):
        nonlocal count3, total3
        count3 += 1
        total3 += new_value3
        return total3 / count3

    return averager_inner3

avg3 = make_averager3()
print(avg3(10))
print(avg3(11))
print(avg3(12))

print(avg3.__code__.co_varnames)
print(avg3.__code__.co_freevars)
print(avg3.__closure__)
print(avg3.__closure__[0].cell_contents)
print(avg3.__closure__[1].cell_contents)

print('---------------------------------------------------------------------------')
