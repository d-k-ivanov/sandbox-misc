#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implement a class for a stack that supports all the regular functions (push, pop)
# and an additional function of max() which returns the maximum element in the stack
# (return None if the stack is empty).
# Each method should run in constant time.

class MyStack:
    def __init__(self):
        self.stack = []


    def push(self, val):
        self.stack.append(val)


    def pop(self):
        self.stack.pop()


    def max(self):
        if len(self.stack):
            return max(self.stack)
        return None

    def __str__(self):
        return self.stack.__str__()


s = MyStack()
print(s.max())
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
