#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        origin0 =  Vector2D(0,0)
        return EuclideanDistance2d(self, origin0)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)


def EuclideanDistance2d(v1: Vector2D, origin: Vector2D) -> float:
    a = (float(v1.x) - float(origin.x))
    b = (float(v1.y) - float(origin.y))
    d = a*a + b*b
    return d ** 0.5


if __name__ == '__main__':
    # exec(open("1_Prologue/vector2D.py").read())
    v1 = Vector2D(3, 4)
    v2 = Vector2D(9, 12)
    print('----------------------------------------------------------------------')
    print(v1)
    print(v2)
    print(abs(v1))
    print(abs(v2))
    print(v1 * 3)
    print(v2 * 8)
    print(abs(v1 * 3))
    print(abs(v2 * 8))
    print(v1 + v2)
    print('----------------------------------------------------------------------')
