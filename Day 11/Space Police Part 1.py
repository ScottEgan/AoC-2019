"""
"""

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

    def get_memory(self):
        """
        """
        return self.memory.copy()
    

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

    def getValue(self, mode, parameter, memory):
        """
        """
        #memory = self.get_memory()

        if mode == 0:
            try:
                return memory[memory[parameter]]
            except IndexError:
                memory.extend([0] * (memory[parameter] - (len(memory) - 1)))
                return memory[memory[parameter]]

        elif mode == 1:
            try:
                return memory[parameter]
            except IndexError:
                memory.extend([0] * (parameter - (len(memory) - 1)))
                return memory[parameter]

        else:
            try:
                return memory[self.relativeBase + memory[parameter]]
            except IndexError:
                memory.extend([0] * ((self.relativeBase + memory[parameter]) - (len(memory) - 1)))
                return memory[self.relativeBase + memory[parameter]]

    def setValue(self, mode, parameter, value, memory):
        """
        """
        if mode == 0:
            try:
                memory[memory[parameter]] = value
            except IndexError:
                memory.extend([0] * (memory[parameter] - (len(memory) - 1)))
                memory[memory[parameter]] = value

        elif mode == 1:
            try:
                memory[parameter] = value
            except IndexError:
                memory.extend([0] * (parameter - (len(memory) - 1)))
                memory[parameter] = value

        else:
            try:
                memory[self.relativeBase + memory[parameter]] = value
            except IndexError:
                memory.extend([0] * ((self.relativeBase + memory[parameter]) - (len(memory) - 1)))
                memory[self.relativeBase + memory[parameter]] = value

    def setInput(self, input):
        """
        """
        self.phaseSetting = input
        self.someInput = input

    def Compute(self):
        """Mostly copied from Part 1
        """
        memory = self.get_memory()
        inputNum = 1
        currentIndex = 0
        output = []
        while currentIndex != 'end' and currentIndex < len(memory):

            if memory[currentIndex] == 3 or memory[currentIndex] == 4:
                #print(f"instruction : {memory[currentIndex]}")
                opCode, p1, p2, p3 = memory[currentIndex], 0, 0, 0
            else:
                opCode, p1, p2, p3 = self.parseInstruction(memory[currentIndex])

            if opCode == 1:
                #print(f"storing {self.getValue(p1, currentIndex + 1, memory)} + {self.getValue(p2, currentIndex + 2, memory)} at {memory[currentIndex + 3]}")
                toSet = self.getValue(p1, currentIndex + 1, memory) + self.getValue(p2, currentIndex + 2, memory)
                self.setValue(p3, currentIndex + 3, toSet, memory)
                currentIndex += 4
                #print("1 Add")

            elif opCode == 2:
                #print(f"storing {self.getValue(p1, currentIndex + 1, memory)} * {self.getValue(p2, currentIndex + 2, memory)} at {memory[currentIndex + 3]}")
                toSet = self.getValue(p1, currentIndex + 1, memory) * self.getValue(p2, currentIndex + 2, memory)
                self.setValue(p3, currentIndex + 3, toSet, memory)
                currentIndex += 4
                #print("2 Multiply")

            elif opCode == 3:
                if inputNum == 1:
                    #set phase
                    #print(f"storing {self.phaseSetting} at {memory[currentIndex + 1]}")
                    self.setValue(p1, currentIndex + 1, self.phaseSetting, memory)
                    currentIndex += 2
                    inputNum += 1
                    #print("3 Input")
                else:
                    #print(f"storing {self.someInput} at {memory[currentIndex + 1]}")
                    self.setValue(p1, currentIndex + 1, self.someInput, memory)
                    currentIndex += 2
                    #print("3 Input")

            elif opCode == 4:
                output = self.getValue(p1, currentIndex + 1, memory)
                currentIndex += 2
                return output
                #print("4 Output")

            elif opCode == 5:
                if self.getValue(p1, currentIndex + 1, memory) != 0:
                    currentIndex = self.getValue(p2, currentIndex + 2, memory)
                else:
                    currentIndex += 3

            elif opCode == 6:
                if self.getValue(p1, currentIndex + 1, memory) == 0:
                    currentIndex = self.getValue(p2, currentIndex + 2, memory)
                else:
                    currentIndex += 3

            elif opCode == 7:
                if self.getValue(p1, currentIndex + 1, memory) < self.getValue(p2, currentIndex + 2, memory):
                    self.setValue(p3, currentIndex + 3, 1, memory)
                    currentIndex += 4

                else:
                    self.setValue(p3, currentIndex + 3, 0, memory)
                    currentIndex += 4

            elif opCode == 8:
                if self.getValue(p1, currentIndex + 1, memory) == self.getValue(p2, currentIndex + 2, memory):
                    self.setValue(p3, currentIndex + 3, 1, memory)
                    currentIndex += 4

                else:
                    self.setValue(p3, currentIndex + 3, 0, memory)
                    currentIndex += 4

            elif opCode == 9:
                self.relativeBase += self.getValue(p1, currentIndex + 1, memory)
                currentIndex += 2
                
            else:
                currentIndex = 'end'
                #print("99 End")
        

#load memory
#memory = [104,1125899906842624,99]
memory = load_file("Day 11/input.txt")


# initialize amplifiers
robot = IntcodeComputer(memory.copy())

robot.setInput(0)
firstOutput = robot.Compute()

print(firstOutput)