#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tkinter as tk

width, height = 900, 900
pixels = [0] * (width * height)

x, y = 0, 1
for n in range(60 * width * height):

    r = random.random() * 100
    xn, yn = x, y
    if r < 1:
        x = 0
        y = 0.16 * yn
    elif r < 86:
        x = 0.85 * xn + 0.04 * yn
        y = -0.04 * xn + 0.85 * yn + 1.6
    elif r < 93:
        x = 0.20 * xn - 0.26 * yn
        y = 0.23 * xn + 0.22 * yn + 1.6
    else:
        x = -0.15 * xn + 0.28 * yn
        y = 0.26 * xn + 0.24 * yn + 0.44

    x_pix = int(width * (0.45 + 0.195 * x))
    y_pix = int(height * (1 - 0.099 * y ))
    pixels[x_pix + y_pix * width] += 1

greys = [ max(0, (256 - p) / 256) for p in pixels]
colors = [int(c * 255) for g in greys for c in [g ** 6, g, g ** 6]]
root = tk.Tk()
p6header = bytes("P6\n{} {}\n255\n".format(width, height), "ascii")
img = tk.PhotoImage(data=p6header + bytes(colors))
tk.Label(root, image=img).pack()
img.write("barnsley_fern.png", format='png')
tk.mainloop()
