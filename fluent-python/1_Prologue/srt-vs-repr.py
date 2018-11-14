#!/usr/bin/env python
# -*- coding: utf-8 -*-

class class1:
    def __init__(self, val=0):
        self.val = val

    def __repr__(self):
        str = "class1({0})"
        return str.format(self.val)


class class2:
    def __init__(self, val=0):
        self.val = val

    def __str__(self):
        str = "Class 2: Value = {0}"
        return str.format(self.val)


if __name__ == '__main__':
    # exec(open("1_Prologue/vector2D.py").read())
    v1 = class1(50)
    v2 = class2(100)
    print('----------------------------------------------------------------------')
    print("Repr: " + repr(v1))
    print("Repr: " + repr(v2))
    print("Str: " + str(v1))
    print("Str: " + str(v2))
    print(v1)
    print(v2)
    print('----------------------------------------------------------------------')
