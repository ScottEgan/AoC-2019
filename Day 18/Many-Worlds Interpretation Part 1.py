"""
another maze
1 = path => white
3 = wall => black
5 = robot => cyan
65 - 90 = doors => blue
97 -122 = keys => orange

color map:
1-2 white
3-4 black
5-64 cyan
64-90 blue
91-96 white
97-122 orange
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm

with open("Day 18/input.txt") as file:
    line = [list(line.replace('#', '3').replace('.', '1').replace('@', '5').strip()) for line in file]
#print(line)

maze = np.array(line, dtype=np.object)
#print(maze)

for index, value in np.ndenumerate(maze):
    if not value.isalpha():
        maze[index] = int(value)
    else:
        maze[index] = int(ord(value))
#print(maze)

maze = maze.astype(np.int, copy=False)

#print(maze)

plot = True
if plot:
    # color map:
    # 1-2 white
    # 3-4 black
    # 5-64 cyan
    # 64-90 blue
    # 91-96 white
    # 97-122 orange
    
    white = np.tile(np.array([1, 1, 1, 1]), (2, 1))
    black = np.tile(np.array([0, 0, 0, 1]), (2, 1))
    cyan = np.tile(np.array([0, 1, 1, 1]), (60, 1))
    blue = cm.get_cmap('winter', 26)(np.linspace(0, 1, 26))
    white2 = np.tile(np.array([1, 1, 1, 1]), (6, 1))
    orange = cm.get_cmap('autumn', 26)(np.linspace(0, 1, 26))
    
    newcolor = np.vstack((white, black, cyan, blue, white2, orange))
    cmap = colors.ListedColormap(newcolor)

    fig = plt.figure(figsize=(10, 8))
    fig.subplots_adjust(0.05,0.01,1,1)
    ax = plt.subplot()
    ax.set_aspect('equal')
    cmesh = ax.pcolormesh(maze, edgecolors='k', linewidths=0.5, cmap=cmap)
    plt.colorbar(cmesh, ax=ax)
    ax.invert_yaxis()
    plt.show()