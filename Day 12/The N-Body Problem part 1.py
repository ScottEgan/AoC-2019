"""
input:
<x=-15, y=1, z=4>
<x=1, y=-10, z=-8>
<x=-5, y=4, z=9>
<x=4, y=6, z=-2>

test1:
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>

test2:
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>

"""

import itertools as itt

# dictionary organized by time step
# each time step contaings the following:
#         x, y, z, vx, vy, vz
#         0   1  2  3  4  5
Io = {0: (-1, 0, 2, 0, 0, 0)}
Eu = {0: (2, -10, -7, 0, 0, 0)}
Ga = {0: (4, -8, 8, 0, 0, 0)}
Ca = {0: (3, 5, -1, 0, 0, 0)}

moons = [Io, Eu, Ga, Ca]

print(list(itt.combinations(range(4), 2)))

def applyGravityAxis(firstMoonValue, secondMoonValue):
    """
    """
    if firstMoonValue > secondMoonValue:
        firstMoonUpdate = -1
        secondMoonUpdate = 1
    elif firstMoonValue == secondMoonValue:
        firstMoonUpdate = 0
        secondMoonUpdate = 0
    else:
        firstMoonUpdate = 1
        secondMoonUpdate = -1

    return firstMoonUpdate, secondMoonUpdate

def Gravity(moons, step):
    """
    """
    for elm in list(itt.combinations(range(4), 2)):
        first = elm[0]
        second = elm[1]
        for i in range(2):
            firstupdate, secondupdate = applyGravityAxis(moons[first][step][i], moons[second][step][i])
            moons[first][step][i + 3] = firstupdate
            moons[second][step][i + 3] = secondupdate

