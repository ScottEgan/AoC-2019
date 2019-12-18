"""
tried depth first search and it gave the wrong answers.
will have to do breadth first search

9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
2 E => 5 D
2 AB => 1 E
3 A, 4 B => 3 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 D, 2 AB, 3 BC, 4 CA => 1 FUEL

"""
import math

with open("Day 14/inputTest.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [line.split('=>') for line in lines]

for elm in lines:
    for i in range(2):
        elm[i] = elm[i].strip()
        elm[i] = elm[i].split(",")
   
#print(lines)

d = {}
for elm in lines:
    d[elm[1][0].split()[1]] = (int(elm[1][0].split()[0]), [])
    for i in range(len(elm[0])):
        elm[0][i] = elm[0][i].strip()
        d[elm[1][0].split()[1]][1].append((int(elm[0][i].split()[0]), elm[0][i].split()[1]))

print(f"input: {d}")

requirements = {}


# new strategy:
# 1: find all base elements that break down into ORE
# 2: find everything that is one level up from those
# 3: break down everything into how many of each second level is needed
# 4: calculate the basic level needs based on the second level

basics = {}
for elm in d.keys():
    if d[elm][1][0][1] == "ORE":
        basics[elm] = 0

print(f"basics: {basics}")

secondLevel = {}
for elm in d.keys():

    for i in range(len(d[elm][1])):
        if d[elm][1][i][1] in basics:
            secondLevel[elm] = 0


print(f"second level: {secondLevel}")

# do a breadth first search to find requirements for second level elements
def BFS(inputElement):
    queue = []

    for i in range(len(d[inputElement][1])):
        queue.append((d[inputElement][1][i][1], d[inputElement][1][i][0]))

    print(f"queue: {queue}")

    while queue:
        tmp = queue.pop(0)
        if tmp[0] in secondLevel.keys():
            secondLevel[tmp[0]] += tmp[1]
        elif tmp[0] in basics.keys():
            basics[tmp[0]] += tmp[1]
        else:
            for i in range(len(d[tmp[0]][1])):
                queue.append((d[tmp[0]][1][i][1], math.ceil(tmp[1] / d[tmp[0]][0]) * d[tmp[0]][1][i][0]))

        
BFS("FUEL")



# calculate second level needs based on second level elements
for elm in secondLevel.keys():
    for i in range(len(d[elm][1])):
        if d[elm][1][i][1] in secondLevel.keys():
            secondLevel[d[elm][1][i][1]] += math.ceil(secondLevel[elm] / d[elm][0]) * d[elm][1][i][0]

# find basic level needs based on second level needs
# total basic level = required second level / produced second level * basic level required
for elm in secondLevel.keys():
    for i in range(len(d[elm][1])):
        if d[elm][1][i][1] in basics.keys():
            basics[d[elm][1][i][1]] += math.ceil(secondLevel[elm] / d[elm][0]) * d[elm][1][i][0]
        
        
            
print(f"second level requirements: {secondLevel}")
print(f"basics requirements: {basics}")

# find ore requirements based on basic level needs
# ore total = required basic / produced basic * ore required
ore = 0
for elm in basics.keys():
    ore += math.ceil(basics[elm] / d[elm][0]) * d[elm][1][0][0]

print(f"ore required: {ore}")
