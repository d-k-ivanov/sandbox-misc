#!/use/bin/env python
# -*- coding: utf-8 -*-

from unicodedata import name
import datetime
import random

random.seed(int(datetime.datetime.now().timestamp()))

print('-' * 160)
set0 = { chr(i) for i in range(32, 1024) if 'SIGN' in name(chr(i), '')}
print(set0)

print('-' * 160)
set1 = { chr(i) for i in range(32, 1024)}
print(set1)

print('-' * 160)
set2 = { random.randrange(0, 512) for i in range(1024)}
print(set2)

print('-' * 160)
set3 = { random.uniform(0.0, 1.0) for i in range(1024)}
print(set3)

print('-' * 160)
