#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('-------------------- Tuple Examples ---------------------------------------')
svo_coordinates = (55.9736, 37.4125)
print(svo_coordinates)

print('---------------------------------------------------------------------------')

tID = [('RU', '111222333'), ('DE', '111222333'), ('ES', '111222333'), ('UK', '111222333')]
for passport in sorted(tID):
    print('%s/%s' % passport)

print('---------------------------------------------------------------------------')

for country, _ in tID:
    print(country)

print('-------------------- Tuple Unpacking --------------------------------------')

city, year, pop, coordinates = ('Beijing', 2017, 21707000, (59.55, 116.23))
print (' City: ', city, '\n Year: ', year, '\n Population: ', pop, '\n Coordinates: ', coordinates)

svo_LONG, svo_LAT = svo_coordinates
print('Lattitude: {}, Longtitude: {}'.format(svo_LAT, svo_LONG))

print('---------------------------------------------------------------------------')

t = (1239, 203)
print("Divmod: {}".format(divmod(*t)))
q, r = divmod(*t)
print("Quotient: {0}\nRemainder: {1}".format(q, r))

print('--------------------------------- <*> -------------------------------------')

aaa, bbb, *rest = range(10)
print(aaa, bbb, rest)

ccc, *midle, ddd = range(5)
print(ccc, midle, ddd)

print('----------------------------- Nested --------------------------------------')
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

print('------------------------------ Named --------------------------------------')

from collections import namedtuple
import array

City = namedtuple('City', 'name country population coordinates')
cities = []
cities.append(City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)))
cities.append(City('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)))
cities.append(City('Mexico City', 'MX', 20.142, (19.433333, -99.133333)))
cities.append(City('New York-Newark', 'US', 20.104, (40.808611, -74.020386)))
cities.append(City('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)))
fmt2 = '{:15} | {:9.3f} | {:15}'
for city in cities:
    print(fmt2.format(city.name, city.population, str(city.coordinates)))

print('---------------------------------------------------------------------------')

print(City._fields)

print('---------------------------------------------------------------------------')
for city in cities:
    for key, value in city._asdict().items():
        print(key + ": ", value)

print('---------------------------------------------------------------------------')
