"""
tried depth first search and it gave the wrong answers.
will have to do breadth first search

9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
2 AB => 1 D
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

print(d)

requirements = {}


# new strategy:
# 1: find all base elements that break down into ORE
# 2: keep reducing 
for elm in d["FUEL"][1]:
    if elm[1] not in requirements:
        requirements[elm[1]] = elm[0]
    else:
        requirements[elm[1]] += elm[0]

print(requirements)



# ore = 0
# for elm in requirements.keys():
#     ore += math.ceil(requirements[elm]/d[elm][0]) * d[elm][1][0][0]

# print(ore)
