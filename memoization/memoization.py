#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

def timeit(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
    return result

def stepcount1(n, steps):
    if n == 0:
        return 1

    if n < 0:
        return 0
    return sum(stepcount1(n - step, steps) for step in steps)

def stepcount2(n, steps):
    sys.setrecursionlimit(10000)
    return stepcount_with_cache(n, steps, {})

def stepcount_with_cache(n, steps, cache):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    total = sum(stepcount_with_cache(n - step, steps, cache) for step in steps)
    cache[n] = total
    return total