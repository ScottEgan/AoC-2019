"""
"""
from itertools import permutations

def load_file(filename):
    """Loads a file to a list

    Parameters:
    filename (string): the name of the file containing input on a
    single line

    Returns: 
    a (list) of ints
    """
    inputList = []
    print("Loading list from file...") 
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

    def get_memory(self):
        """
        """
        return self.memory.copy()
    

    def parseInstruction(self, instruction):
        """
        Returns:
        opCode, p1, p2
        """
        #print(f"instruction : {instruction}")

        if len(str(instruction)) == 1:
            return instruction, 0, 0

        elif instruction == 99:
            return instruction, 0, 0
        
        elif len(str(instruction)) == 3:
            return int(str(instruction)[-2:]), int(str(instruction)[-3:-2]), 0

        else:
            return int(str(instruction)[-2:]), int(str(instruction)[-3:-2]), int(str(instruction)[-4:-3])

    def getValue(self, mode, parameter, memory):
        """
        """
        #memory = self.get_memory()

        if mode == 0:
            return memory[memory[parameter]]
        else:
            return memory[parameter]

    def Compute(self, phaseSetting, someInput):
            """Mostly copied from Part 1
            """
            memory = self.get_memory()
            inputNum = 1
            currentIndex = 0
            while currentIndex != 'end' and currentIndex < len(memory):

                if memory[currentIndex] == 3 or memory[currentIndex] == 4:
                    #print(f"instruction : {memory[currentIndex]}")
                    opCode, p1, p2 = memory[currentIndex], 0, 0
                else:
                    opCode, p1, p2 = self.parseInstruction(memory[currentIndex])

                if opCode == 1:
                    #print(f"storing {getValue(p1, currentIndex + 1, memory)} + {getValue(p2, currentIndex + 2, memory)} at {memory[currentIndex + 3]}")
                    memory[memory[currentIndex + 3]] = self.getValue(p1, currentIndex + 1, memory) + self.getValue(p2, currentIndex + 2, memory)
                    currentIndex += 4
                    #print("1 Add")
                elif opCode == 2:
                    memory[memory[currentIndex + 3]] = self.getValue(p1, currentIndex + 1, memory) * self.getValue(p2, currentIndex + 2, memory)
                    currentIndex += 4
                    #print("2 Multiply")
                elif opCode == 3:
                    if inputNum == 1:
                        #set phase
                        #print(f"storing {phaseSetting} at {memory[currentIndex + 1]}")
                        memory[memory[currentIndex + 1]] = phaseSetting
                        currentIndex += 2
                        inputNum += 1
                        #print("3 Input")
                    else:
                        #print(f"storing {someInput} at {memory[currentIndex + 1]}")
                        memory[memory[currentIndex + 1]] = someInput
                        currentIndex += 2
                        #print("3 Input")
                elif opCode == 4:
                    if p1 == 0:
                        print(f"output: {memory[memory[currentIndex + 1]]}")
                        return memory[memory[currentIndex + 1]]
                    else:
                        print(f"output: {memory[currentIndex + 1]}")
                        return memory[currentIndex + 1]
                    currentIndex += 2
                    #print("4 Output")  
                elif opCode == 99:
                    currentIndex = 'end'
                    #print("99 End")

# find all tests to run
testsToRun = list(permutations(range(0, 5)))

#load memory
memory = load_file("Day 7/input test.txt")

# initialize amplifiers
A = IntcodeComputer(memory.copy())
B = IntcodeComputer(memory.copy())
C = IntcodeComputer(memory.copy())
D = IntcodeComputer(memory.copy())
E = IntcodeComputer(memory.copy())

maxThrust = 0
for elm in testsToRun:
    Aout = A.Compute(elm[0], 0)
    Bout = B.Compute(elm[1], Aout)
    Cout = C.Compute(elm[2], Bout)
    Dout = D.Compute(elm[3], Cout)
    Eout = E.Compute(elm[4], Dout)
    if Eout > maxThrust:
        maxThrust = Eout

print(maxThrust)

