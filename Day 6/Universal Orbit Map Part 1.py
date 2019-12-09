"""
"""

with open("Day 6/input.txt") as file:
   input = list(map(lambda x: x.split(")"), [line.strip("\n") for line in file]))

orbits = {}

for elm in input:
    if elm[0] not in orbits:
        orbits[elm[0]] = [elm[1]]
    else:
        orbits[elm[0]].append(elm[1])

total = 0
i = 0

def followPath(planet, orbits):
    """
    """
    if planet in orbits:
        sum = len(orbits[planet])
        for i in range(len(orbits[planet])):
            sum += followPath(orbits[planet][i], orbits)
        
        return sum
    else:
        return 0


for elm in orbits.keys():
    total += len(orbits[elm])
    for i in range(len(orbits[elm])):
        total += followPath(orbits[elm][i], orbits)

print(total)