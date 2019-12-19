"""
"""

import numpy as np
import matplotlib.pyplot as plt


# dictionary to hold coordinates (x, y) and what is there:
# 0 => not explored
# 1 => path
# 2 => o2 system
# 3 => wall

coord = {(0, 0): 1, (0, 1): 3, (1, 0): 1, (2, 0): 1, (3, 0): 3, (2, -1): 3, (-1, 0): 3}
size = 80

A = np.zeros((size, size))

fig = plt.figure(figsize=(8,8))
for key, value in coord.items():
    xdraw = int(key[0] + (size / 2))
    ydraw = int(key[1] + (size / 2))
    A[xdraw, ydraw] = value

    plt.cla()
    plt.pcolormesh(A, edgecolors='k', linewidths=0.5)
    plt.axes().set_aspect('equal')
    plt.pause(0.5)



plt.show()