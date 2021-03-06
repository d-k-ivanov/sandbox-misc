#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install bobo
# bobo -f .\3_FunctionsAsObjects\bobobo.py
# curl http://localhost:8080/?person=Dmitry

import bobo

@bobo.query('/')
def hello(person):
    return "Hello %s!" % person
