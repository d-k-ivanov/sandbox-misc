#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import locale
import pyuca
import sys

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

print('---------------------------------------------------------------------------')

locales = locale.locale_alias
for lang in locales.items():
    print(lang)
#print(locale.locale_alias)

print('---------------------------------------------------------------------------')

print(sorted(fruits))
#if os.name == 'nt':
if sys.platform == 'win32':
    locale.setlocale(locale.LC_COLLATE, 'portuguese_brazil')
#elif os.name == 'posix':
elif sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(sorted(fruits, key=locale.strxfrm))

print('---------------------------------------------------------------------------')

coll = pyuca.Collator()
print(sorted(fruits))
print(sorted(fruits, key=coll.sort_key))

print('---------------------------------------------------------------------------')
