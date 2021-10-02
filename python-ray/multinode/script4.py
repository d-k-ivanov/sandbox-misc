#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ray
import time
ray.init(address='ray://172.21.151.178:10001')


@ray.remote
def add(x, y):
    time.sleep(1)
    return x + y


# Aggregate the values slowly. This approach takes O(n) where n is the
# number of values being aggregated. In this case, 7 seconds.
start = time.time()
id1 = add.remote(1, 2)
id2 = add.remote(id1, 3)
id3 = add.remote(id2, 4)
id4 = add.remote(id3, 5)
id5 = add.remote(id4, 6)
id6 = add.remote(id5, 7)
id7 = add.remote(id6, 8)
result = ray.get(id7)
print(result)
print("Finished in: {:.2f}s".format(time.time()-start))


# Aggregate the values in a tree-structured pattern. This approach
# takes O(log(n)). In this case, 4 seconds.
start = time.time()
id1 = add.remote(1, 2)
id2 = add.remote(3, 4)
id3 = add.remote(5, 6)
id4 = add.remote(7, 8)
id5 = add.remote(id1, id2)
id6 = add.remote(id3, id4)
id7 = add.remote(id5, id6)
result = ray.get(id7)
print(result)
print("Finished in: {:.2f}s".format(time.time()-start))


# Alternative: Slow
start = time.time()
values = [1, 2, 3, 4, 5, 6, 7, 8]
while len(values) > 1:
    values = [add.remote(values[0], values[1])] + values[2:]
result = ray.get(values[0])
print(result)
print("Finished in: {:.2f}s".format(time.time()-start))


# Alternative: Fast
start = time.time()
values = [1, 2, 3, 4, 5, 6, 7, 8]
while len(values) > 1:
    values = values[2:] + [add.remote(values[0], values[1])]
result = ray.get(values[0])
print(result)
print("Finished in: {:.2f}s".format(time.time()-start))


# 36
# Finished in: 7.04s
# 36
# Finished in: 4.36s
# 36
# Finished in: 7.03s
# 36
# Finished in: 3.71s
