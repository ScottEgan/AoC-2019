"""
Incode Program
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

    def Compute(self, input1=1, input2=1):
        """Mostly copied from Part 1
        """
        self.phaseSetting = input1
        self.someInput = input2
        inputNum = 1
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
                if inputNum == 1:
                    self.setValue(p1, currentIndex + 1, self.phaseSetting)
                    #print(f"current index: {currentIndex} input {self.phaseSetting}")
                    currentIndex += 2
                    inputNum += 1
                else:
                    self.setValue(p1, currentIndex + 1, self.someInput)
                    #print(f"current index: {currentIndex} input {self.someInput}")
                    currentIndex += 2   

            elif opCode == 4:
                #print("4 Output")
                output.append(self.getValue(p1, currentIndex + 1))
                #print(f"current index: {currentIndex} output {self.getValue(p1, currentIndex + 1)}")
                currentIndex += 2
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
memory = load_file("Day 19/input.txt")


total = 0
for x in range(50):
    for y in range(50):
        tractorBeam = IntcodeComputer(memory.copy())
        output = tractorBeam.Compute(x, y)
        print(x, y, output)
        total += output[0]

print(total)

# x = 0
# y = 0
# tractorBeam = IntcodeComputer(memory.copy())
# output = tractorBeam.Compute(x, y)
# print(x, y, output)



