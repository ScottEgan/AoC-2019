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
    print("Loading list from file...") 
    with open(filename) as file:
        inputList = [int(x) for x in file.read().split(",")]

    return inputList

def parseInstruction(instruction):
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

def getValue(mode, parameter, memory):
    """
    """
    if mode == 0:
        return memory[memory[parameter]]
    else:
        return memory[parameter]

def Computer(memoryIn, someInput):
        """Mostly copied from Part 1
        """
        memory = memoryIn.copy()

        currentIndex = 0
        while currentIndex != 'end' and currentIndex < len(memory):

            if memory[currentIndex] == 3 or memory[currentIndex] == 4:
                #print(f"instruction : {memory[currentIndex]}")
                opCode, p1, p2 = memory[currentIndex], 0, 0
            else:
                opCode, p1, p2 = parseInstruction(memory[currentIndex])

            if opCode == 1:
                #print(f"storing {getValue(p1, currentIndex + 1, memory)} + {getValue(p2, currentIndex + 2, memory)} at {memory[currentIndex + 3]}")
                memory[memory[currentIndex + 3]] = getValue(p1, currentIndex + 1, memory) + getValue(p2, currentIndex + 2, memory)
                currentIndex += 4
                #print("1 Add")
            elif opCode == 2:
                memory[memory[currentIndex + 3]] = getValue(p1, currentIndex + 1, memory) * getValue(p2, currentIndex + 2, memory)
                currentIndex += 4
                #print("2 Multiply")
            elif opCode == 3:
                #print(f"storing {someInput} at {memory[currentIndex + 1]}")
                memory[memory[currentIndex + 1]] = someInput
                currentIndex += 2
                #print("3 Input")  
            elif opCode == 4:
                if p1 == 0:
                    print(f"output: {memory[memory[currentIndex + 1]]}")
                else:
                    print(f"output: {memory[currentIndex + 1]}")
                currentIndex += 2
                #print("4 Output")
            elif opCode == 5:
                if getValue(p1, currentIndex + 1, memory) != 0:
                    currentIndex = getValue(p2, currentIndex + 2, memory)
                else:
                    currentIndex += 3
            elif opCode == 6:
                if getValue(p1, currentIndex + 1, memory) == 0:
                    currentIndex = getValue(p2, currentIndex + 2, memory)
                else:
                    currentIndex += 3
            elif opCode == 7:
                if getValue(p1, currentIndex + 1, memory) < getValue(p2, currentIndex + 2, memory):
                    memory[memory[currentIndex + 3]] = 1
                    currentIndex += 4
                else:
                    memory[memory[currentIndex + 3]] = 0
                    currentIndex += 4

            elif opCode == 8:
                if getValue(p1, currentIndex + 1, memory) == getValue(p2, currentIndex + 2, memory):
                    memory[memory[currentIndex + 3]] = 1
                    currentIndex += 4
                else:
                    memory[memory[currentIndex + 3]] = 0
                    currentIndex += 4

            else:
                currentIndex = 'end'
                print("99 End")

#test = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
#test = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
#Computer(test, 2)

Computer(load_file('Day 5/input.txt'), 5)

