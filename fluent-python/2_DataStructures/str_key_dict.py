#!/use/bin/env python
# -*- coding, utf-8 -*-

import collections


class StrKeyDict0(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print('----------------------------------------------------------------------')
    print('Tests for item retrieval using `d[key]` notation::')
    print(d['2'])
    print(d[4])
    # print(d[1])
    print('KeyError: \'1\'')
    print('----------------------------------------------------------------------')
    print('Tests for item retrieval using `d.get(key)` notation::')
    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'n/a'))
    print('----------------------------------------------------------------------')
    print('Tests for the `in` operator::')
    print(2 in d)
    print(1 in d)
    print('----------------------------------------------------------------------')
