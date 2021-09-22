#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ray

# ray.init(address='auto', _redis_password='5241590000000000')
ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures)) # [0, 1, 4, 9]
