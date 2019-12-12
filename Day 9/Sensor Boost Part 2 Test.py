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
            #print(f"setting memory at {memory[parameter]} to {value}")

        elif mode == 1:
            try:
                memory[parameter] = value
            except IndexError:
                memory.extend([0] * (parameter - (len(memory) - 1)))
                memory[parameter] = value
            #print(f"setting memory at {parameter} to {value}")

        else:
            try:
                memory[self.relativeBase + memory[parameter]] = value
            except IndexError:
                memory.extend([0] * ((self.relativeBase + memory[parameter]) - (len(memory) - 1)))
                memory[self.relativeBase + memory[parameter]] = value
            #print(f"setting memory at {self.relativeBase + memory[parameter]} to {value}")

    def Compute(self, index, input):
        """Mostly copied from Part 1
        """
        memory = self.get_memory()
        self.phaseSetting = input
        self.someInput = input
        inputNum = 1
        currentIndex = index
        output = []
        while currentIndex != 'end' and currentIndex < len(memory):

            if memory[currentIndex] == 3 or memory[currentIndex] == 4:
                #print(f"instruction : {memory[currentIndex]}")
                opCode, p1, p2, p3 = memory[currentIndex], 0, 0, 0
            else:
                opCode, p1, p2, p3 = self.parseInstruction(memory[currentIndex])
            #print(f"opcode:{opCode}, p1:{p1}, p2:{p2}, p3:{p3}")

            if opCode == 1:
                #print("1 Add")
                toSet = self.getValue(p1, currentIndex + 1, memory) + self.getValue(p2, currentIndex + 2, memory)
                self.setValue(p3, currentIndex + 3, toSet, memory)
                currentIndex += 4
                #print(f"current index: {currentIndex}")
                

            elif opCode == 2:
                #print("2 Multiply")
                toSet = self.getValue(p1, currentIndex + 1, memory) * self.getValue(p2, currentIndex + 2, memory)
                self.setValue(p3, currentIndex + 3, toSet, memory)
                currentIndex += 4
                #print(f"current index: {currentIndex}")
                

            elif opCode == 3:
                if inputNum == 1:
                    #set phase
                    #print("3 Input")
                    self.setValue(p1, currentIndex + 1, self.phaseSetting, memory)
                    currentIndex += 2
                    inputNum += 1
                    #print(f"current index: {currentIndex}")
                    
                else:
                    #print("3 Input")
                    self.setValue(p1, currentIndex + 1, self.someInput, memory)
                    currentIndex += 2
                    #print(f"current index: {currentIndex}")
                    

            elif opCode == 4:
                #print("4 Output")
                output.append(self.getValue(p1, currentIndex + 1, memory))
                currentIndex += 2
                #print(f"current index: {currentIndex}")
                if len(output) == 2:
                    return output, currentIndex
                

            elif opCode == 5:
                #print("5 jump-if-true")
                if self.getValue(p1, currentIndex + 1, memory) != 0:
                    currentIndex = self.getValue(p2, currentIndex + 2, memory)
                    #print(f"jumping to index {currentIndex}")
                else:
                    currentIndex += 3
                    #print(f"current index: {currentIndex}")

            elif opCode == 6:
                #print("6 jump-if-false")
                if self.getValue(p1, currentIndex + 1, memory) == 0:
                    currentIndex = self.getValue(p2, currentIndex + 2, memory)
                    #print(f"jumping to index {currentIndex}")
                else:
                    currentIndex += 3
                    #print(f"current index: {currentIndex}")

            elif opCode == 7:
                #print("7 less than")
                if self.getValue(p1, currentIndex + 1, memory) < self.getValue(p2, currentIndex + 2, memory):
                    self.setValue(p3, currentIndex + 3, 1, memory)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

                else:
                    self.setValue(p3, currentIndex + 3, 0, memory)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

            elif opCode == 8:
                #print("8 equals")
                if self.getValue(p1, currentIndex + 1, memory) == self.getValue(p2, currentIndex + 2, memory):
                    self.setValue(p3, currentIndex + 3, 1, memory)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

                else:
                    self.setValue(p3, currentIndex + 3, 0, memory)
                    currentIndex += 4
                    #print(f"current index: {currentIndex}")

            elif opCode == 9:
                #print("9 relative base")
                self.relativeBase += self.getValue(p1, currentIndex + 1, memory)
                currentIndex += 2
                #print(f"current index: {currentIndex}")
                
            else:
                #print("99 End")
                currentIndex = 'end'
                return output, currentIndex
                
        
        return output, currentIndex

memory = load_file("Day 9/input.txt")


# initialize amplifiers
A = IntcodeComputer(memory.copy())

# A.Compute(currentIndex, input)
Aout = A.Compute(0, 2)

print(Aout)