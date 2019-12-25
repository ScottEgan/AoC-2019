"""
another maze
1 = path => white
3 = wall => black
5 = robot => cyan
65 - 90 = doors => blue
97 -122 = keys => orange

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm

with open("Day 18/inputTest.txt") as file:
    line = [list(line.replace('#', '3').replace('.', '1').replace('@', '5').strip()) for line in file]
#print(line)

maze = np.array(line, dtype=np.object)
#print(maze)
doors = {}
keys = {}
path = set()
for index, value in np.ndenumerate(maze):
    if not value.isalpha():
        maze[index] = int(value)
        if value == '5':
            robot = tuple(index)
        elif value == '1':
            path.add(index)
    else:
        maze[index] = int(ord(value))   #convert letters to ASCII numbers for plotting
        if value.isupper():
            doors[index] = value
            #path.add(index)
        else:
            keys[index] = value
            #path.add(index)

maze = maze.astype(np.int, copy=False)

print(f"doors: {doors}")
print(f"keys: {keys}")
print(f"robot: {robot}")
print(f"path {path}")
#print(maze)

possibleMovement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
moveQueue = [(robot, 0)]
keyList = []
stateList = {}
step = 0
# not sure what to do here in order to solve this. may need to look into path finding algorithms
while step < 10:
    current = moveQueue.pop(0)
    currentCoord = current[0]
    step = current[1] + 1

    for elm in possibleMovement:
        updatedCoord = tuple(e + v for e, v in zip(elm, currentCoord))
        if updatedCoord in path:
            moveQueue.append((updatedCoord, step))
            stateList[updatedCoord] = (step, keyList)
        elif updatedCoord in keys.keys():
            moveQueue.append((updatedCoord, step))
            keyList.append(keys[updatedCoord])
            # if you find a key remove the door by adding it to the list of accepted paths
            path.add(doors[[k for k, v in doors.items() if v == keys[updatedCoord].upper()][0]])
            stateList[updatedCoord] = (step, keyList)
    
    


plot = False
if plot:
    # color map:
    # 1-2 white => path
    # 3-4 black => walls
    # 5-64 cyan => robot
    # 64-90 blue => doors
    # 91-96 white 
    # 97-122 orange => keys
    
    white = np.tile(np.array([1, 1, 1, 1]), (2, 1))
    black = np.tile(np.array([0, 0, 0, 1]), (2, 1))
    cyan = np.tile(np.array([0, 1, 1, 1]), (60, 1))
    blue = np.tile(np.array([0, 0, 1, 1]), (26, 1))
    white2 = np.tile(np.array([1, 1, 1, 1]), (6, 1))
    orange = np.tile(np.array([1, 165/255, 0, 1]), (26, 1))
    
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