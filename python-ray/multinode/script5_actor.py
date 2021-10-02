#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ray
ray.init(address='ray://172.21.151.178:10001')

@ray.remote
class Counter(object):
    def __init__(self):
        self.x = 0

    def inc(self):
        self.x += 1

    def get_value(self):
        return self.x


# Create an actor process.
c = Counter.remote()

# Check the actor's counter value.
print(ray.get(c.get_value.remote()))

# Increment the counter twice and check the value again.
c.inc.remote()
c.inc.remote()
print(ray.get(c.get_value.remote()))

# Increment the counter twice and check the value again.
c.inc.remote()
c.inc.remote()
c.inc.remote()
c.inc.remote()
c.inc.remote()
print(ray.get(c.get_value.remote()))
