#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ray
import numpy as np
# ray.init(address='ray://172.21.151.178:10001', _redis_password='5241590000000000')
ray.init(address='ray://172.21.151.178:10001')



@ray.remote
def create_matrix(size):
    return np.random.normal(size=size)


@ray.remote
def multiply_matrices(x, y):
    return np.dot(x, y)


x_id = create_matrix.remote([1000, 1000])
y_id = create_matrix.remote([1000, 1000])
z_id = multiply_matrices.remote(x_id, y_id)

# Get the results.
z = ray.get(z_id)
print(z)
