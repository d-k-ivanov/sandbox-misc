#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import functools
import operator
import unicodedata

def factorial1(n:int) -> int:
    return functools.reduce(lambda a, b: a*b, range(1, n+1))

def factorial2(n:int) -> int:
    return functools.reduce(operator.mul, range(1, n+1))

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print('---------------------------------------------------------------------------')

    print(factorial1(10))
    print(factorial2(10))

    print('---------------------------------------------------------------------------')

    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    for city in sorted(metro_data, key=operator.itemgetter(1)):
        print(city)

    print('---------------------------------------------------------------------------')

    LatLong = collections.namedtuple('LatLong', 'lat long')
    Metropolis = collections.namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    print(metro_areas[0])
    name_lat = operator.attrgetter('name', 'coord.lat')

    for city in sorted(metro_areas, key=operator.attrgetter('coord.lat')):
        print(name_lat(city))

    print('---------------------------------------------------------------------------')

    # print(dir(operator))
    operators = [name for name in dir(operator) if not name.startswith('_')]
    print(operators)

    print('---------------------------------------------------------------------------')

    s = 'The time has come'
    upcase = operator.methodcaller('upper')
    print(upcase(s))
    print(s.upper())
    print(str.upper(s))

    hiphemate = operator.methodcaller('replace', ' ', '-')
    print(hiphemate(s))
    print(s.replace(' ', '-'))
    print(str.replace(s, ' ', '-'))

    print('---------------------------------------------------------------------------')

    triple = functools.partial(operator.mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))
    mmm = map(triple, range(1, 10))
    print(dir(mmm))
    for item in mmm:
        print(item)

    print('---------------------------------------------------------------------------')

    nfc = functools.partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print('Not normalized:')
    print(s1, s2)
    print(s1 == s2)
    print(len(s1), len(s2))

    print('Normalized:')
    print(nfc(s1), nfc(s2))
    print(nfc(s1) == nfc(s2))
    print(len(nfc(s1)), len(nfc(s2)))

    print('---------------------------------------------------------------------------')

    picture = functools.partial(tag, 'img', cls='pic-frame')
    print(picture)
    print(picture())
    print(picture(src='image001.jpg'))
    print(picture.func)
    print(picture.args)
    print(picture.keywords)

    print('---------------------------------------------------------------------------')

    picture2 = functools.partial(tag, 'img', 'image', cls='pic-frame', id=111)
    print(picture2)
    print(picture2())
    print(picture2(src='image001.jpg'))
    print(picture2.func)
    print(picture2.args)
    print(picture2.keywords)

    print('---------------------------------------------------------------------------')
