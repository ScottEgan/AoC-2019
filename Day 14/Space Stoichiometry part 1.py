"""
tried depth first search and it gave the wrong answers.
will have to do breadth first search

1 ORE => 2 A
1 A => 1 B
1 B => 1 C
1 A, 1 C, 1 B => 1 FUEL

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

allElements = {}
for elm in d.keys():
    if elm not in allElements:
        allElements[elm] = 0
    for i in range(len(d[elm][1])):
        if d[elm][1][i][1] not in allElements:
            allElements[d[elm][1][i][1]] = 0

print(f"all elements: {allElements}")
 


# new strategy V4:
# 1: keep track of extra production
# 4: profit

# levels = {}
# def findlevels(element):
#     productList = d[element][1]

#     for i in range(len(productList)):
#         productName = productList[i][1]
        
#         if productName == "ORE":
#             return 1
#         else:
#             level = findlevels(productName)
#             if productName not in levels.keys():
#                 levels[productName] = level
#                 print(f"{productName} is level {level}")

#     if element != "FUEL":
#         return level + 1
#     else:
#         return max(levels.values()) + 1

basics = {}
for elm in d.keys():
    if d[elm][1][0][1] == "ORE":
        basics[elm] = 0

print(f"basics: {basics}")

# secondLevel = {}
# for elm in d.keys():

#     for i in range(len(d[elm][1])):
#         if d[elm][1][i][1] in basics:
#             secondLevel[elm] = 0


#print(f"second level: {secondLevel}")

# do a breadth first search to find requirements for second level elements
def BFS(inputElement):
    queue = []

    for i in range(len(d[inputElement][1])):
        queue.append((d[inputElement][1][i][1], d[inputElement][1][i][0]))

    print(f"queue: {queue}")
    ore = 0
    while queue:
        tmp = queue.pop(0)
        elmName = tmp[0]
        qtyElmReq = tmp[1]
        qtyElmProd = d[elmName][0]
        reactList = d[elmName][1]

        if allElements[elmName] >= qtyElmReq:
            allElements[elmName] -= qtyElmReq
            useOre = False
        elif qtyElmProd > qtyElmReq:
                allElements[elmName] += (qtyElmProd - qtyElmReq)
                useOre = True
        else:
            useOre = True

        if elmName not in basics.keys() and useOre:
            for i in range(len(reactList)):
                reactName = reactList[i][1]
                qtyReact = reactList[i][0]
                queue.append((reactName, math.ceil(qtyElmReq / qtyElmProd) * qtyReact))
        elif useOre:
            ore += reactList[0][0]

    return ore

#topLevel = findlevels("FUEL")

#print(f"fuel is level {topLevel}")
#print(f"levels: {levels}")    
oreRequired = BFS("FUEL")
print(oreRequired)



# calculate second level needs based on second level elements
# for elm in secondLevel.keys():
#     for i in range(len(d[elm][1])):
#         if d[elm][1][i][1] in secondLevel.keys():
#             secondLevel[d[elm][1][i][1]] += math.ceil(secondLevel[elm] / d[elm][0]) * d[elm][1][i][0]

# find basic level needs based on second level needs
# total basic level = required second level / produced second level * basic level required
# for elm in secondLevel.keys():
#     for i in range(len(d[elm][1])):
#         if d[elm][1][i][1] in basics.keys():
#             basics[d[elm][1][i][1]] += math.ceil(secondLevel[elm] / d[elm][0]) * d[elm][1][i][0]
        
        
# print(f"all elements: {allElements}")            
# print(f"second level requirements: {secondLevel}")
# print(f"basics requirements: {basics}")

# find ore requirements based on basic level needs
# ore total = required basic / produced basic * ore required

# for elm in basics.keys():
#     ore += math.ceil(basics[elm] / d[elm][0]) * d[elm][1][0][0]

# print(f"ore required: {ore}")
