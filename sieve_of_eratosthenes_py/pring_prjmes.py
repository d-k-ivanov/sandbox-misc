#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nats(n):
    yield n
    yield from nats(n + 1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)



if __name__=='__main__':
    import sys
    print("Max recurson depth is {}".format(sys.getrecursionlimit()))

    # Maximum value before overflow
    sys.setrecursionlimit(2733)

    print("Max recurson depth now is {}".format(sys.getrecursionlimit()))

    p = sieve(nats(2))

    while True:
        try:
            n = next(p)
        except StopIteration:
            break
        except RecursionError:
            break
        print(n)
