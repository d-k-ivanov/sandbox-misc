#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dis

def factorial(n):
    """Function that returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

def factorial_negative(n):
    return 1/-1 if n > -2 else 1 / (-n * factorial_negative(n+1))

def reverse0(word):
    return word[::-1]


if __name__ == '__main__':
    print('---------------------------------------------------------------------------')

    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))
    fact = factorial
    print(fact)
    print(map(factorial, range(11)))
    print(list(map(factorial, range(11))))
    print({k:v for k in range(11) for v in map(factorial, range(k))})
    print({k:k**2 for k in range(11)})

    print('---------------------------------------------------------------------------')

    print(factorial_negative(-42))
    print(list(map(factorial_negative, range(0, -11, -1))))
    print({k:v for k in range(0, -11, -1) for v in map(factorial_negative, range(0, k, -1))})
    neg_fac_dict = {k:v for k in range(0, -110, -1) for v in map(factorial_negative, range(0, k, -1))}
    for item in neg_fac_dict.items():
        print(item)

    print('---------------------------------------------------------------------------')

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))
    print(reverse0('abracadabra'))
    print(sorted(fruits, key=reverse0))

    print('---------------------------------------------------------------------------')

    print(list(map(factorial, range(6))))
    print([factorial(n) for n in range(6)])
    print(list(map(factorial, filter(lambda x: x % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])

    from functools import reduce
    from operator import add
    print(reduce(add, range(100)))
    print(sum(range(100)))
    print(all(range(10)))
    print(all(range(1,10)))
    print(any(range(10)))

    print('--------------------     Lambdas     --------------------------------------')

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1] ))

    print('---------------------------------------------------------------------------')

    print(dir(factorial))
    print()
    print(dir(lambda n: 1 if n < 2 else n * factorial(n-1) ))
    print()
    print(factorial.__dict__)

    print('---------------------------------------------------------------------------')
