"""
"""
import matplotlib.pyplot as plt
import time

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

    def Compute(self, index, input):
        """Mostly copied from Part 1
        """
        self.phaseSetting = input
        self.someInput = input
        inputNum = 1
        currentIndex = index
        output = []
        while currentIndex != 'end' and currentIndex < len(self.memory):

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
                if inputNum == 1:
                    #set phase
                    #print("3 Input")
                    self.setValue(p1, currentIndex + 1, self.phaseSetting)
                    currentIndex += 2
                    inputNum += 1
                    #print(f"current index: {currentIndex}")
                    
                else:
                    #print("3 Input")
                    self.setValue(p1, currentIndex + 1, self.someInput)
                    currentIndex += 2
                    #print(f"current index: {currentIndex}")
                    

            elif opCode == 4:
                #print("4 Output")
                output.append(self.getValue(p1, currentIndex + 1))
                currentIndex += 2
                #print(f"current index: {currentIndex}")
                if len(output) == 2:
                    return output, currentIndex
                

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
                return output, currentIndex
                
        
        return output, currentIndex

#load memory
memory = load_file("Day 11/input.txt")

#dictionary to hold coordinates (x, y) and if that panel is white '1' or black '0'
coord = {(0, 0): 0}

# initialize robot
robot = IntcodeComputer(memory.copy())

step = 0
direction = 'N'
currentIndex = 0
x = 0
xlist = []
y = 0
ylist = []
fig = plt.figure()

plot = True

while currentIndex != 'end' and step < 150:

    xlist.append(x)
    ylist.append(y)
    
    if (x, y) not in coord.keys():
        coord[(x, y)] = 0

    print(f"robot at ({x}, {y}) facing {direction} tile is {coord[(x, y)]}")
    print(f"starting robot with index {currentIndex} and input {coord[(x, y)]}")

    output, currentIndex = robot.Compute(currentIndex, coord[(x, y)])

    print(output, currentIndex)

    if output[0] == 0:
        #paint panel black
        print(f"paint panel black at {x}, {y}")
        coord[(x, y)] = 0
    else:
        #paint panel white
        print(f"paint panel white at {x}, {y}")
        coord[(x, y)] = 1
    
    if output[1] == 0:
        #robot turns left 90 deg
        #and moves forward 1 space
        print("robot turns to the left")
        if direction == 'N':
            direction = 'W'
            x -= 1
        elif direction == 'E':
            direction = 'N'
            y += 1
        elif direction == 'S':
            direction = 'E'
            x += 1
        elif direction == 'W':
            direction = 'S'
            y -= 1
    else:
        #robot turns right 90 deg
        #and moves forward 1 space
        print("robot turns to the right")
        if direction == 'N':
            direction = 'E'
            x += 1
        elif direction == 'E':
            direction = 'S'
            y -= 1
        elif direction == 'S':
            direction = 'W'
            x -= 1
        elif direction == 'W':
            direction = 'N'
            y += 1

    if plot:
        plt.cla()
        plt.axis([-20, 20, -20, 20])
        plt.plot(xlist, ylist, 'b-')
        plt.pause(0.2)

    step += 1
    print(f"step number: {step}")
    print(f"robot at {x}, {y} facing {direction}")
    print("")

print("END")
print(len(coord.keys())) 
if plot:
    plt.show()
