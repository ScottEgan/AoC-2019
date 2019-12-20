"""
Intcode
"""
from itertools import chain
import numpy as np
import matplotlib.pyplot as plt

def load_file(filename):
    """Loads a file to a list

    Parameters:
    filename (string): the name of the file containing input on a
    single line

    Returns: 
    a (list) of ints
    """
    inputList = []
    print(f"Loading list from file... {filename}") 
    with open(filename) as file:
        inputList = [int(x) for x in file.read().split(",")]

    return inputList

class IntcodeComputer(object):
    """
    """
    def __init__(self, memory):
        """
        """
        self.memory = memory
        self.relativeBase = 0
        self.phaseSetting = 0
        self.someInput = 0

    def parseInstruction(self, instruction):
        """
        Returns:
        opCode, p1, p2, p3
        """
        #print(f"instruction : {instruction}")

        if len(str(instruction)) == 1:
            return instruction, 0, 0, 0

        elif instruction == 99:
            return instruction, 0, 0, 0
        
        elif len(str(instruction)) == 3:
            return int(str(instruction)[-2:]), int(str(instruction)[-3:-2]), 0, 0

        elif len(str(instruction)) == 4:
            return int(str(instruction)[-2:]), int(str(instruction)[-3:-2]), int(str(instruction)[-4:-3]), 0
        else:
            return int(str(instruction)[-2:]), int(str(instruction)[-3:-2]), int(str(instruction)[-4:-3]), int(str(instruction)[-5:-4])

    def getValue(self, mode, parameter):
        """
        """

        if mode == 0:
            try:
                return self.memory[self.memory[parameter]]
            except IndexError:
                self.memory.extend([0] * (self.memory[parameter] - (len(self.memory) - 1)))
                return self.memory[self.memory[parameter]]

        elif mode == 1:
            try:
                return self.memory[parameter]
            except IndexError:
                self.memory.extend([0] * (parameter - (len(self.memory) - 1)))
                return self.memory[parameter]

        else:
            try:
                return self.memory[self.relativeBase + self.memory[parameter]]
            except IndexError:
                self.memory.extend([0] * ((self.relativeBase + self.memory[parameter]) - (len(self.memory) - 1)))
                return self.memory[self.relativeBase + self.memory[parameter]]

    def setValue(self, mode, parameter, value):
        """
        """
        if mode == 0:
            try:
                self.memory[self.memory[parameter]] = value
            except IndexError:
                self.memory.extend([0] * (self.memory[parameter] - (len(self.memory) - 1)))
                self.memory[self.memory[parameter]] = value
            #print(f"setting self.memory at {self.memory[parameter]} to {value}")

        elif mode == 1:
            try:
                self.memory[parameter] = value
            except IndexError:
                self.memory.extend([0] * (parameter - (len(self.memory) - 1)))
                self.memory[parameter] = value
            #print(f"setting self.memory at {parameter} to {value}")

        else:
            try:
                self.memory[self.relativeBase + self.memory[parameter]] = value
            except IndexError:
                self.memory.extend([0] * ((self.relativeBase + self.memory[parameter]) - (len(self.memory) - 1)))
                self.memory[self.relativeBase + self.memory[parameter]] = value
            #print(f"setting self.memory at {self.relativeBase + self.memory[parameter]} to {value}")

    def Compute(self, input=1):
        """Mostly copied from Part 1
        """
        self.phaseSetting = input
        self.someInput = input
        currentIndex = 0
        output = []
        while currentIndex != 'end' and currentIndex < len(self.memory):

            #print(f"index is: {currentIndex}")
            if self.memory[currentIndex] == 3 or self.memory[currentIndex] == 4:
                #print(f"instruction : {self.memory[currentIndex]}")
                opCode, p1, p2, p3 = self.memory[currentIndex], 0, 0, 0
            else:
                opCode, p1, p2, p3 = self.parseInstruction(self.memory[currentIndex])
            #print(f"opcode:{opCode}, p1:{p1}, p2:{p2}, p3:{p3}")

            if opCode == 1:
                #print("1 Add")
                toSet = self.getValue(p1, currentIndex + 1) + self.getValue(p2, currentIndex + 2)
                self.setValue(p3, currentIndex + 3, toSet)
                currentIndex += 4
                #print(f"current index: {currentIndex}")
                
            elif opCode == 2:
                #print("2 Multiply")
                toSet = self.getValue(p1, currentIndex + 1) * self.getValue(p2, currentIndex + 2)
                self.setValue(p3, currentIndex + 3, toSet)
                currentIndex += 4
                #print(f"current index: {currentIndex}")
                
            elif opCode == 3:
                #print("3 Input")
                self.setValue(p1, currentIndex + 1, self.someInput)
                currentIndex += 2
                #print(f"current index: {currentIndex}")       

            elif opCode == 4:
                #print("4 Output")
                output.append(self.getValue(p1, currentIndex + 1))
                currentIndex += 2
                #print(f"current index: {currentIndex}")
                #return self.getValue(p1, currentIndex + 1)

            elif opCode == 5:
                #print("5 jump-if-true")
                if self.getValue(p1, currentIndex + 1) != 0:
                    currentIndex = self.getValue(p2, currentIndex + 2)
                    #print(f"jumping to index {currentIndex}")
                else:
                    currentIndex += 3
                    #print(f"current index: {currentIndex}")

            elif opCode == 6:
                #print("6 jump-if-false")
                if self.getValue(p1, currentIndex + 1) == 0:
                    currentIndex = self.getValue(p2, currentIndex + 2)
                    #print(f"jumping to index {currentIndex}")
                else:
                    currentIndex += 3
                    #print(f"current index: {currentIndex}")

            elif opCode == 7:
                #print("7 less than")
                if self.getValue(p1, currentIndex + 1) < self.getValue(p2, currentIndex + 2):
                    self.setValue(p3, currentIndex + 3, 1)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

                else:
                    self.setValue(p3, currentIndex + 3, 0)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

            elif opCode == 8:
                #print("8 equals")
                if self.getValue(p1, currentIndex + 1) == self.getValue(p2, currentIndex + 2):
                    self.setValue(p3, currentIndex + 3, 1)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

                else:
                    self.setValue(p3, currentIndex + 3, 0)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

            elif opCode == 9:
                #print("9 relative base")
                self.relativeBase += self.getValue(p1, currentIndex + 1)
                currentIndex += 2
                #print(f"current index: {currentIndex}")
                
            else:
                #print("99 End")
                currentIndex = 'end'
                return output
                
        
        return output

#load memory
memory = load_file("Day 17/input.txt")

robot = IntcodeComputer(memory.copy())

output = []

output = robot.Compute()

# find all values of 10 in the output list
idxlist = [idx + 1 for idx, val in enumerate(output) if val == 10]

temp = zip(chain([0], idxlist), chain(idxlist, [None])) 
res = list(output[i:j] for i, j in temp)

res = res[:-2]
res = [elm[:-1] for elm in res]

intersects = []
sum = 0
for i in range(len(res)):
    for j in range(len(res[0])):
        if (res[i][j] == 35 and i > 1 and j > 1 and
            i < (len(res) - 1) and j < (len(res[0]) - 1)):

            if (res[i + 1][j] == 35 and res[i - 1][j] == 35 and
                res[i][j + 1] == 35 and res[i][j - 1] == 35):

                intersects.append((j, i))
                sum += (i * j)

print(intersects)
print(sum)

plt.figure()
ax = plt.subplot()
plt.pcolormesh(res, edgecolors='k', linewidths=0.5)
ax.invert_yaxis()
plt.show()



    