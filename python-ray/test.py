#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

while True:
    try:
        print("Working...")
        time.sleep(0.1)
    # except:
    except Exception:
        print("Catched!")

