"""
"""
import numpy as np
from fractions import Fraction

with open("Day 10/inputTest.txt") as file:
   input = [line.strip() for line in file]

#print(input)

asteroidLoc = []
for c in range(len(input)):
    for r in range(len(input[0])):
        if input[c][r] == '#':
            asteroidLoc.append((r, c))

#print(asteroidLoc)


#asteroidLocTest = [(1, 0), (4, 0), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (3, 4), (4, 4)]

seen = {}
for a in asteroidLoc:
    for b in asteroidLoc:
        if a != b:
            if b[1] == a[1]:
                #just compare x distance
                # distance = x2 - x1
                dist = (b[0] - a[0])
                if np.sign(dist) == -1:
                    slope = '-y'
                else:
                    slope = 'y'
    
            elif b[0] == a[0]:
                #just compare y distance
                # distance = y2 - y1
                dist = (b[1] - a[1])
                if np.sign(dist) == -1:
                    slope = '-x'
                else:
                    slope = 'x'
                
            else:
                #TODO: change slope to an angle measurement 
                # and change distance to absolute value

                #compare slope and distance
                # slope = y2 - y1 / x2 - x1
                slope = Fraction(b[1] - a[1], b[0] - a[0])
                # distance = y2 - y1 + x2 - x1
                dist = (b[1] - a[1]) + (b[0] - a[0])
                if np.sign(dist) == -1:
                    slope = slope * -1
            
            if a not in seen:
                seen[a] = [[b, slope, dist]]
            else:
                #check to see if the slope matches anything in the current list
                slopeflag = False
                for i in range(len(seen[a])):
                    if seen[a][i][1] == slope and np.sign(seen[a][i][2]) == np.sign(dist):
                        slopeflag = True
                        #check distance
                        if abs(seen[a][i][2]) < abs(dist):
                            pass
                        else:
                            seen[a].append([b, slope, dist])
                            seen[a].remove(seen[a][i])
                    
                if [b, slope, dist] not in seen[a] and not slopeflag:
                    seen[a].append([b, slope, dist])
    
total = 0
for key in seen.keys():
    print(key, len(seen[key]))
    if len(seen[key]) > total:
        total = len(seen[key])

print(total)

