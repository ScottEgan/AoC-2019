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
Io = {0: [-15, 1, 4, 0, 0, 0]}
Eu = {0: [1, -10, -8, 0, 0, 0]}
Ga = {0: [-5, 4, 9, 0, 0, 0]}
Ca = {0: [4, 6, -2, 0, 0, 0]}

moons = [Io, Eu, Ga, Ca]

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
    #initialize the next steps from current step
    for elm in range(len(moons)):
        moons[elm][step + 1] = moons[elm][step].copy()

    for elm in list(itt.combinations(range(4), 2)):
        first = elm[0]
        second = elm[1]
        for i in range(3):
            firstupdate, secondupdate = applyGravityAxis(moons[first][step][i], moons[second][step][i])
            moons[first][step + 1][i + 3] += firstupdate
            moons[second][step + 1][i + 3] += secondupdate

def Velocity(moons, step):
    """
    """
    for elm in range(len(moons)):
        for i in range(3):
            moons[elm][step + 1][i] = moons[elm][step][i] + moons[elm][step + 1][i + 3]

def totEnergy(moons, step):
    """
    """
    
    tot = 0
    for elm in range(len(moons)):
        pot = 0
        kin = 0
        for i in range(3):
            pot += abs(moons[elm][step][i])
            kin += abs(moons[elm][step][i + 3])

        tot += pot * kin

    return tot

for i in range(1001):

    #print pretty output
    print("")
    print(f"After {i} steps:")
    for elm in range(len(moons)):
        print(f"pos=<x= {moons[elm][i][0]:<4}, y= {moons[elm][i][1]:<4}, z= {moons[elm][i][2]:<4}>," 
               f"vel= < x={moons[elm][i][3]:<4}, y={moons[elm][i][4]:<4}, z={moons[elm][i][5]:<4} > ")

    #do gravity
    Gravity(moons, i)
    #do velocity
    Velocity(moons, i)
    

#do energy
totalEnergy = totEnergy(moons, i)   
print(totalEnergy)