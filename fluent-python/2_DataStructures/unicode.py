#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('---------------------------------------------------------------------------')

s = 'café'
print(len(s))
b = s.encode('utf_8')
print(b)
print(len(b))
print(b.decode('utf_8'))

cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

print('---------------------------------------------------------------------------')

import array
# nums = array.array('h', [-2, -1, 0, 1, 2])
nums = array.array('q', [-2, -1, 0, 1, 2])
nums_b = bytes(nums)
print(nums_b)

print('---------------------------------------------------------------------------')

import os
import struct

png_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.png')
# print(png_file)
with open(png_file, 'rb') as fp_png_file:
    data = fp_png_file.read()

if len(data) < 16:
    print('Not walid data! Exiting')
    exit(0)

png_w, png_h = struct.unpack('>LL', data[16:24])
# print(png_w, ' ', png_h)
print('{:15}{:5}'.format('Image width: ', int(png_w)))
print('{:15}{:5}'.format('Image height: ', int(png_h)))

print('---------------------------------------------------------------------------')

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

monr = b'Montr\xe9al'
print(monr.decode('cp1252'))
print(monr.decode('iso8859_7'))
print(monr.decode('koi8_r'))

print('---------------------------------------------------------------------------')

import unicode_porto
#exec(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'unicode_porto.py')).read())

print('---------------------------------------------------------------------------')

u16     = 'El Niño'.encode('utf_16')
u16le   = 'El Niño'.encode('utf_16le')
u16be   = 'El Niño'.encode('utf_16be')

print('{:6}: {}'.format('u16', u16))
print('{:6}: {}'.format('u16', list(u16)))
print()
print('{:6}: {}'.format('u16le', u16le))
print('{:6}: {}'.format('u16le', list(u16le)))
print()
print('{:6}: {}'.format('u16be', u16be))
print('{:6}: {}'.format('u16be', list(u16be)))

print('---------------------------------------------------------------------------')

import unicodedata

norm_s1 = 'café'
norm_s2 = 'cafe\u0301'
print('norm_s1: ', norm_s1, ' | ','norm_s2: ', norm_s2)
print('norm_s1: ', len(norm_s1), ' | ','norm_s2: ', len(norm_s2))
print(norm_s1 == norm_s2)
print('Normalization form C(omposed): ')
print('norm_s1: ', len(unicodedata.normalize('NFC', norm_s1)), ' | ','norm_s2: ', len(unicodedata.normalize('NFC', norm_s2)))
print(unicodedata.normalize('NFC', norm_s1) == unicodedata.normalize('NFC', norm_s2))
print('Normalization form D(eomposed): ')
print('norm_s1: ', len(unicodedata.normalize('NFD', norm_s1)), ' | ','norm_s2: ', len(unicodedata.normalize('NFD', norm_s2)))
print(unicodedata.normalize('NFD', norm_s1) == unicodedata.normalize('NFD', norm_s2))

print('---------------------------------------------------------------------------')

ohm = '\u2126'
ohm_c = unicodedata.normalize('NFC', ohm)
print(ohm, unicodedata.name(ohm))
print(ohm_c, unicodedata.name(ohm_c))
print(ohm == ohm_c)
print(unicodedata.normalize('NFC', ohm) == unicodedata.normalize('NFC', ohm_c))

print('---------------------------------------------------------------------------')

half = '½'
half_kc = unicodedata.normalize('NFKC', half)
print(half_kc, ' -> ', [ord(x) for x in half_kc])
four_squared = '4²'
print(unicodedata.normalize('NFKC', four_squared))
micro = '\u00B5'
micro_kc = unicodedata.normalize('NFKC', micro)
print(micro, ' -> ', micro_kc)
print(ord(micro), ' -> ', ord(micro_kc))
print(unicodedata.name(micro), ' -> ', unicodedata.name(micro_kc))
micro_cf = micro.casefold()
print(unicodedata.name(micro_cf))
print(micro, ' -> ', micro_cf)
eszett = 'ß'
print(unicodedata.name(eszett))
eszett_cf = eszett.casefold()
print(micro, ' -> ', micro_cf)

print('---------------------------------------------------------------------------')
