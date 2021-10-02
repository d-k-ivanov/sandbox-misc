#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ray
import time

# Start Ray.
# ray.init(address='auto', _redis_password='5241590000000000')
ray.init(address='ray://172.21.151.178:10001',
         _redis_password='5241590000000000')


@ray.remote
def f():
    time.sleep(0.01)
    return ray._private.services.get_node_ip_address()


# Get a list of the IP addresses of the nodes that have joined the cluster.
# set(ray.get([f.remote() for _ in range(1000)]))
print(set(ray.get([f.remote() for _ in range(1000)])))
