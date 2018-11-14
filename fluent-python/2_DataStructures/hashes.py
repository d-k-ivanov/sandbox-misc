#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def hash_diff(num1, num2):
    hash1 = hash(num1)
    hash2 = hash(num2)
    print('{:20}{:^6}{:064b}'.format(num1,'->', hash1))
    sys.stdout.write('{:26}'.format(' '))
    for i,j in zip(format(hash1,'064b'), format(hash2,'064b')):
        if i == j:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('!')
    sys.stdout.write('\n')
    print('{:20}{:^6}{:064b}'.format(num2,'->', hash2))
    print('-' * (20+6+64))


if __name__ == '__main__':
    print('-' * (20+6+64))
    print('|{:^20}{:^6}{:^62}|'.format('Number',' | ', 'Binary representation'))
    print('-' * (20+6+64))
    hash_diff(1, 1.0)
    hash_diff(1.1, 1.2)
    hash_diff(1.0, 1.0001)
    hash_diff(1.0001, 1.0002)
    hash_diff(1.0002, 1.0003)
    hash_diff(sys.maxsize-4, sys.maxsize-5)






