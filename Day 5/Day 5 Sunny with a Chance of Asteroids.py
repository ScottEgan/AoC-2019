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
    """
    opCode = int(str(instruction)[-2:])
    p1 = int(str(instruction)[-3:-2])
    p2 = int(str(instruction)[-4:-3])

    return opCode, p1, p2

def getValue(mode, parameter, memory):
    """
    """
    if mode == 0:
        return memory[memory[parameter]]
    else:
        return parameter

def Computer(memoryIn, someInput):
        """Mostly copied from Part 1
        """
        memory = memoryIn.copy()

        currentIndex = 0
        while currentIndex != 'end' and currentIndex < len(memory):

            opCode, p1, p2 = parseInstruction(currentIndex)

            if opCode == 1:
                memory[memory[currentIndex + 3]] = getValue(p1, currentIndex + 1, memory) + getValue(p2, currentIndex + 2, memory)
                currentIndex += 4
                #print("1 Add")
            elif opCode == 2:
                memory[memory[currentIndex + 3]] = getValue(p1, currentIndex + 1, memory) * getValue(p2, currentIndex + 2, memory)
                currentIndex += 4
                #print("2 Multiply")
            elif opCode == 3:
                memory[memory[currentIndex + 1]] = someInput
                currentIndex += 2
                #print("3 Input")  
            elif opCode == 4:
                print(memory[memory[currentIndex + 1]])
                currentIndex += 2
                #print("4 Output")  
            elif opCode == 99:
                currentIndex = 'end'
                #print("99 End")

Computer(load_file('Day 5/input.txt'), 1)

