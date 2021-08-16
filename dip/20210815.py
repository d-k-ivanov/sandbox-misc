#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyStack:
    def __init__(self):
        self.stack = []


    def push(self, val):
        self.stack.append(val)


    def pop(self):
        self.stack.pop()


    def max(self):
        return max(self.stack)

    def __str__(self):
        return self.stack.__str__()


s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2

from random import randrange
for i in range(10):
    s.push(randrange(1000))

print(s)
print(s.max())
