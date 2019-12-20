"""
650 digits
"""
import numpy as np

with open("Day 16/input.txt") as file:
   inputArray = np.fromiter((int(char) for char in file.readline()), int)

print(f"Starting Input: {inputArray}")
size = len(inputArray)
#print(size)

def doOnePhase(inputArray):
    """
    """
    # build multiplication array
    tmp = []
    multi = []
    for i in range(1, (len(inputArray) + 1)):
        a = [0 for x in range(i)]
        b = [1 for x in range(i)]
        c = [0 for x in range(i)]
        d = [-1 for x in range(i)]
        tmp = a + b + c + d
        #print(tmp)
        while len(tmp) < (len(inputArray) + 1):
            tmp.extend(tmp)
        #print(tmp)
        tmp = tmp[1:(len(inputArray) + 1)]
        multi.append(tmp)

    multi = np.array(multi)
    #print(multi)
    inputMatrix = np.tile(inputArray, (len(inputArray), 1))
    final = multi * inputMatrix
    #print(final)
    nextInput = np.fromiter([int(str(x)[-1]) for x in np.sum(final, axis=1)], int)
    #print(nextInput)
    return nextInput
    
step = 0
while step < 100:
    output = doOnePhase(inputArray)
    inputArray = output
    step += 1
    firstEight = output[0:8]
    print(f"After {step} phase: {firstEight}")



