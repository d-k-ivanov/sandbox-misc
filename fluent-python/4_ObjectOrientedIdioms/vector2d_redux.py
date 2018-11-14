#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array
import math

class Vector2D:
    # __slots__ = ('__x', '__y')
    typecode = 'd'
    pi = 3.14159265359

    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            # r - dictance from reference point to vertor point (hypotenuse)
            r = abs(self)
            # Θ - angle from a reference direction
            t = self.angle()
            coords = (r, t)
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array.array(self.typecode, self)))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        # print(typecode)
        # print(str(octets))
        memv = memoryview(octets[1:]).cast(typecode)
        # print(memv[0], memv[1])
        # return cls(memv[0], memv[1])
        return cls(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # return math.hypot(self.x, self)
        # return (self.x*self.x + self.y*self.y) ** 0.5
        origin0 =  Vector2D(0,0)
        return self.EuclideanDistance2d(self, origin0)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    @staticmethod
    def EuclideanDistance2d(v1, origin) -> float:
        a = v1.x - origin.x
        b = v1.y - origin.y
        d = a*a + b*b
        return d ** 0.5

    @staticmethod
    def _atan(n:float) -> float:
        return math.atan(n)

    def angle(self):
        x = self.x
        y = self.y
        if x > 0:
            return self._atan(y/x)
        elif x < 0 and y >= 0:
            return self._atan(y/x) + self.pi
        elif x < 0 and y < 0:
            return self._atan(y/x) - self.pi
        elif x == 0 and y > 0:
            return self.pi/2
        elif x == 0 and y < 0:
            return -(self.pi/2)
        else:
            return 0.0
        # return math.atan2(self.y, self.x)
