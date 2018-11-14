#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vector2d_redux import Vector2D

import copy

v1 = Vector2D(3, 4)
v3 = Vector2D(32, 2)
v4 = Vector2D(3.1, 4.2)

print('-' * 100)

print(v1.x, v1.y)

x, y = v1
print(x, y)

print(v1)
print(repr(v1))

v1_clone = eval(repr(v1))
# v1_clone = copy.copy(v1)
print(v1_clone)
print(v1 == v1_clone)

octets = bytes(v1)
print(octets)

print(abs(v1))
print(abs(v1*12))

print(bool(v1), bool(Vector2D(0, 0)))

print('-' * 100)

# vec_3_4 = bytes(b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@')
vec_9_12 = bytes(b'd\x00\x00\x00\x00\x00\x00"@\x00\x00\x00\x00\x00\x00(@')
print(vec_9_12)
v2 = Vector2D.frombytes(vec_9_12)
print(v2)

print('-' * 100)

print(bytes([9]))
print(bytes([12]))
print((9).to_bytes(8, byteorder='big'))
print((12).to_bytes(8, byteorder='big'))
print(bytes((9, 12)))
print(bytes(Vector2D(9, 12)))

print('-' * 100)

print(format(v1))
print(format(v1, '.3f'))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

print(format(v1, '.10fp'))
print(format(v2, '.10fp'))
print(format(v3, '.10fp'))

print('-' * 100)

vp1 = Vector2D(3, 0)
vp2 = Vector2D(3, 4)
vp3 = Vector2D(-3, 11)
vp4 = Vector2D(-3, -11)
vp5 = Vector2D(0, 11)
vp6 = Vector2D(0, -11)
vp7 = Vector2D(0, 0)

print(format(vp1, '.10fp'))
print(format(vp2, '.10fp'))
print(format(vp3, '.10fp'))
print(format(vp4, '.10fp'))
print(format(vp5, '.10fp'))
print(format(vp6, '.10fp'))
print(format(vp7, '.10fp'))

print('-' * 100)

print(hash(v1))
print(hash(v2))
print(hash(v3))
print(hash(v4))
print(set([v1]))

print(hash(vp1))
print(hash(vp2))
print(hash(vp3))
print(hash(vp4))
print(hash(vp5))
print(hash(vp6))
print(hash(vp7))

print('-' * 100)

print(v1.__dict__)
print(v2.__dict__)
print(v3.__dict__)
print(v4.__dict__)
print(vp1.__dict__)
print(vp2.__dict__)
print(vp3.__dict__)
print(vp4.__dict__)
print(vp5.__dict__)
print(vp6.__dict__)
print(vp7.__dict__)

print('-' * 100)

dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))
v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))

from vector2d_short import Vector2D_short
sv1 = Vector2D_short(1/11, 1/27)
print(sv1)
print(repr(sv1))
print(bytes(sv1))
print(len(bytes(sv1)))

print('-' * 100)

