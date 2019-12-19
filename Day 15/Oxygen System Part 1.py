"""
Intcode maze robot
found 02 at 12, -14
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import time
import random

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

    def Compute(self, input):
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
                return self.getValue(p1, currentIndex + 1)
                #currentIndex += 2
                #print(f"current index: {currentIndex}")
                
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
                return currentIndex
                
        
        return output

#load memory
memory = load_file("Day 15/input.txt")

robot = IntcodeComputer(memory.copy())

# dictionary to hold coordinates (x, y) and what is there:
# 0 => not explored
# 1 => path
# 2 => o2 system
# 3 => wall
coord = {(0, 0): 1}

# initial conditions
step = 0
direction = 1
x = 0
y = 0
end = False
# stuff for plotting
size = 60
A = np.zeros((size, size))
fig = plt.figure(figsize=(8, 8))
fig.subplots_adjust(0,0,1,1)
plt.axes().set_aspect('equal')
cmap = matplotlib.colors.ListedColormap(['black', 'white', 'chartreuse', 'crimson', 'cyan'])
xdraw = int(x + (size / 2))
ydraw = int(y + (size / 2))
A[xdraw, ydraw] = coord[(x, y)]
plt.pcolormesh(A, edgecolors='k', linewidths=0.5, cmap=cmap)

while step < 10000000 and not end:

    output = robot.Compute(direction)
    preset = set(coord.copy())
    #wall in direction
    if output == 0:
        # trying to go north
        if direction == 1:
            coord[(x, y + 1)] = 3

        # trying to go east
        elif direction == 4:
            coord[(x + 1, y)] = 3

        # trying to go south
        elif direction == 2:
            coord[(x, y - 1)] = 3
     
        #trying to go west
        elif direction == 3:
            coord[(x - 1, y)] = 3

        direction = random.randint(1, 4)
            
    # moved one step in direction passed
    elif output == 1:
        # going north
        if direction == 1:
            y += 1
            
        # going east
        elif direction == 4:
            x += 1
            
        # going south
        elif direction == 2:
            y -= 1

        # going west
        elif direction == 3:
            x -= 1
        
        coord[(x, y)] = 1
        direction = random.randint(1, 4)

    #found o2 system
    elif output == 2:
        # going north
        if direction == 1:
            y += 1
        # going east
        elif direction == 4:
            x += 1
        # going south
        elif direction == 2:
            y -= 1
        # going west
        elif direction == 3:
            x -= 1
        
        coord[(x, y)] = 2
        print(f"found 02 at {x}, {y}")
        end = True

    new = {k: coord[k] for k in set(coord) - preset}
    if new:
        newList = [[elm[0], elm[1]] for elm in new.keys()]
        xdraw = int(newList[0][0] + (size / 2))
        ydraw = int(newList[0][1] + (size / 2))
        A[xdraw, ydraw] = 4
        plt.cla()
        plt.pcolormesh(A, edgecolors='k', linewidths=0.5, cmap=cmap)
        plt.pause(0.02)
        A[xdraw, ydraw] = new[(newList[0][0], newList[0][1])]

    step += 1
    print(step)

plt.show()
