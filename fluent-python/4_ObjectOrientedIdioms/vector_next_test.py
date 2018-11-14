#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vector_next import Vector

v1 = Vector([3.1, 4,2])
v2 = Vector((3, 4, 5))
v3 = Vector(range(10))

print('-' * 100)

print(repr(v1))
print(repr(v2))
print(repr(v3))

# for i in Vector(range(10)):
#     print(i)

print('-' * 100)

print(len(v1))
print(len(v2))
print(len(v3))

print(repr(v3[2]))
print(repr(v3[5]))

print(repr(v3[3:8]))
print(repr(v3[-1:]))

print('-' * 100)

print(v3.x)
print((v3.y, v3.z, v3.t))

print('-' * 100)

print(v3.x)
# v3.x = 10.0
print(v3)
print(repr(v3))
print(v3.x)

print('-' * 100)

# Before format implemented
# ----------------------------------------------------------------------------------------------------
# (3.1, 4.0, 2.0)
# (3.0, 4.0, 5.0)
# (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
# ----------------------------------------------------------------------------------------------------

print(format(v1, 'h'))
print(format(v2, 'h'))
print(format(v3, 'h'))
print(format(Vector([-1, -1, -1, -1]), 'h'))
print(format(Vector([2, 2, 2, 2]), '.3eh'))
print(format(Vector([0, 1, 0, 0]), '0.5fh'))

print('-' * 100)

v_xxx = Vector([1, 2, 3, 4])
print(format(v_xxx, 'h'))

print('-' * 100)
