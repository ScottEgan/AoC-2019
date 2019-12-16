"""
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
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

#print(d)

requirements = {}
def findSupplies(input_num, input_elm):
    """
    """
    for i in range(len(d[input_elm][1])):
        req_num = d[input_elm][1][i][0]
        req_elm = d[input_elm][1][i][1]
        if req_elm == "ORE":
            return input_num, input_elm
        else:
            ret_num, ret_elm = findSupplies(req_num, req_elm)
            if ret_elm == "exit":
                return 0, "exit"
            elif ret_elm not in requirements.keys():
                requirements[ret_elm] = ret_num
            else:
                requirements[ret_elm] += ret_num
    
    return 0, "exit"

finalNum, finalElm = findSupplies(1, 'FUEL')

print(requirements)

ore = 0
for elm in requirements.keys():
    ore += math.ceil(requirements[elm]/d[elm][0]) * d[elm][1][0][0]

print(ore)
