"""
tried depth first search and it gave the wrong answers.
will have to do breadth first search

new strategy V5:
1: keep BETTER track of extra production

1 ORE => 2 A
1 A => 1 B
1 B => 1 C
1 A, 1 C, 1 B => 1 FUEL

"""
import math

with open("Day 14/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [line.split('=>') for line in lines]

for elm in lines:
    for i in range(2):
        elm[i] = elm[i].strip()
        elm[i] = elm[i].split(",")
#print(lines)

# split things up into a nice dictionary where the keys are the products
# the first value is the ammount prouced and the second is a list of reactants
d = {}
for elm in lines:
    d[elm[1][0].split()[1]] = (int(elm[1][0].split()[0]), [])
    for i in range(len(elm[0])):
        elm[0][i] = elm[0][i].strip()
        d[elm[1][0].split()[1]][1].append((int(elm[0][i].split()[0]), elm[0][i].split()[1]))
#print(f"input: {d}")

# find a list of all elements
allElements = {}
for elm in d.keys():
    if elm not in allElements:
        allElements[elm] = 0
    for i in range(len(d[elm][1])):
        if d[elm][1][i][1] not in allElements:
            allElements[d[elm][1][i][1]] = 0
#print(f"all elements: {allElements}")
 
# find the elements that are produced from ore
basics = {}
for elm in d.keys():
    if d[elm][1][0][1] == "ORE":
        basics[elm] = 0
#print(f"basics: {basics}")

# do a breadth first search to find the ammount of ore needed
def BFS(inputElement, allElements):
    queue = []
    queuesim = []       #this is just a helper list
    for i in range(len(d[inputElement][1])):
        queue.append([d[inputElement][1][i][1], d[inputElement][1][i][0]])
        queuesim.append(d[inputElement][1][i][1])
    #print(f"queue: {queue}")
    #print(f"queue simple: {queuesim}")

    ore = 0
    while queue:
        tmp = queue.pop(0)
        queuesim.pop(0)
        elmName = tmp[0]
        qtyElmReq = tmp[1]
        qtyElmProd = d[elmName][0]
        reactList = d[elmName][1]

        #this block helps keep track of waste elements
        if allElements[elmName] > 0:
            if allElements[elmName] > qtyElmReq:
                allElements[elmName] -= qtyElmReq
                qtyElmReq = 0
            else:
                qtyElmReq -= allElements[elmName]
                allElements[elmName] = 0

            if qtyElmReq > 0:
                useOre = True
            else:
                useOre = False
        else:
            useOre = True
        # enter here if the item doesn't brake down into ore and we
        # didn't fulfill the requirements from the waste 
        if elmName not in basics.keys() and useOre:
            # check to see if we produce waste - if so keep track of it
            if (math.ceil(qtyElmReq / qtyElmProd) * qtyElmProd) > qtyElmReq:
                allElements[elmName] += ((math.ceil(qtyElmReq / qtyElmProd) * qtyElmProd) - qtyElmReq)
            
            for i in range(len(reactList)):
                reactName = reactList[i][1]
                qtyReact = reactList[i][0]
                #sum items in the queue for simplification
                if reactName in queuesim:
                    queue[queuesim.index(reactName)][1] += (math.ceil(qtyElmReq / qtyElmProd) * qtyReact)
                else:
                    queue.append([reactName, math.ceil(qtyElmReq / qtyElmProd) * qtyReact])
                    queuesim.append(reactName)

        # enter here if the item does brake down into ore and we
        # didn't fulfill the requirements from the waste 
        elif useOre:
            ore += math.ceil(qtyElmReq / qtyElmProd) * reactList[0][0]
            # check to see if we produce waste - if so keep track of it
            if (math.ceil(qtyElmReq / qtyElmProd) * qtyElmProd) > qtyElmReq:
                allElements[elmName] += ((math.ceil(qtyElmReq / qtyElmProd) * qtyElmProd) - qtyElmReq)

    return ore
  
oreRequired = BFS("FUEL", allElements)
print(oreRequired)
