#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random
import timeit
import time


def test_dict(haystack_len=1000):
    tt0 = timeit.default_timer()
    random.seed(int(datetime.datetime.now().timestamp()))
    haystack = {round(random.uniform(0.0, 1.0),7): round(random.uniform(0.0, 1.0),7) for i in range(haystack_len)}
    needles = {round(random.uniform(0.0, 1.0),7): round(random.uniform(0.0, 1.0),7) for i in range(1000)}
    found = 0
    t0 = timeit.default_timer()
    for n in needles:
        if n in haystack:
            found += 1
    print('{:>21d} | {:>15.6f} | {:>13d} | {:>11.6f}'.format(
            haystack_len,
            timeit.default_timer()-t0,
            found,
            timeit.default_timer()-tt0)
        )


def test_set(haystack_len=1000):
    tt0 = timeit.default_timer()
    random.seed(int(datetime.datetime.now().timestamp()))
    haystack = {round(random.uniform(0.0, 1.0),7) for i in range(haystack_len)}
    needles = {round(random.uniform(0.0, 1.0),7) for i in range(1000)}
    t0 = timeit.default_timer()
    found = len(needles & haystack)
    print('{:>21d} | {:>15.6f} | {:>13d} | {:>11.6f}'.format(
            haystack_len,
            timeit.default_timer()-t0,
            found,
            timeit.default_timer()-tt0)
        )


def test_list(haystack_len=1000):
    tt0 = timeit.default_timer()
    random.seed(int(datetime.datetime.now().timestamp()))
    haystack = [round(random.uniform(0.0, 1.0),7) for i in range(haystack_len)]
    needles = [round(random.uniform(0.0, 1.0),7) for i in range(1000)]
    found = 0
    t0 = timeit.default_timer()
    for n in needles:
        if n in haystack:
            found += 1
    print('{:>21d} | {:>15.6f} | {:>13d} | {:>11.6f}'.format(
            haystack_len,
            timeit.default_timer()-t0,
            found,
            timeit.default_timer()-tt0)
        )


if __name__ == '__main__':
    print('{:>21} | {:>15} | {:>13} | {:>11}'.format('Length of Dictionary', 'Execution time', 'Intersection', 'Total time'))
    print('{}'.format('-' * (21+15+13+11+9)))
    for num in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]:
        test_dict(num)
    print('{}'.format('-' * (21+15+13+11+9)))
    print()

    print('{:>21} | {:>15} | {:>13} | {:>11}'.format('Length of Set', 'Execution time', 'Intersection', 'Total time'))
    print('{}'.format('-' * (21+15+13+11+9)))
    for num in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]:
        test_set(num)
    print('{}'.format('-' * (21+15+13+11+9)))
    print()

    print('{:>21} | {:>15} {:>13} | {:>11}'.format('Length of List', 'Execution time', 'Intersection', 'Total time'))
    print('{}'.format('-' * (21+15+13+11+9)))
    for num in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]:
        test_list(num)
    print('{}'.format('-' * (21+15+13+11+9)))
    print()

    exit(0)
