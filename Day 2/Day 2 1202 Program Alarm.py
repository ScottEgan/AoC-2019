"""
Part 1
Once you have a working computer, the first step is to restore the gravity assist program
(your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. 
To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. 
What value is left at position 0 after the program halts?

Part 2
With terminology out of the way, we're ready to proceed. To complete the gravity assist, 
you need to determine what pair of inputs produces the output 19690720.
"""
import copy

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

def partOne(inputText):
    """Part 1
    """

    input = load_file(inputText)
    #print("Original input", input)
    print("Making Changes: replacing pos 1 with 12 and pos 2 with 2")
    input[1] = 12
    input[2] = 2
    #print("Modified Input", input)

    currentIndex = 0
    while currentIndex != 'end' and currentIndex < len(input):
        if input[currentIndex] == 1:
            input[input[currentIndex + 3]] = input[input[currentIndex + 1]] + input[input[currentIndex + 2]]
            currentIndex += 4
            #print("1 Add")
        elif input[currentIndex] == 2:
            input[input[currentIndex + 3]] = input[input[currentIndex + 1]] * input[input[currentIndex + 2]]
            currentIndex += 4
            #print("2 Multiply")
        elif input[currentIndex] == 99:
            currentIndex = 'end'
            #print("99 End")

    
    #print("Final", input)
    return input[0]


def partTwo(inputText):
    """
    """
    memory = load_file(inputText)

    def Computer(memory, noun, verb):
        """Mostly copied from Part 1
        """
        input = copy.deepcopy(memory)
        #print("Making Changes: replacing pos 1 with 12 and pos 2 with 2")
        input[1] = noun
        input[2] = verb

        currentIndex = 0
        while currentIndex != 'end' and currentIndex < len(input):
            if input[currentIndex] == 1:
                input[input[currentIndex + 3]] = input[input[currentIndex + 1]] + input[input[currentIndex + 2]]
                currentIndex += 4
                #print("1 Add")
            elif input[currentIndex] == 2:
                input[input[currentIndex + 3]] = input[input[currentIndex + 1]] * input[input[currentIndex + 2]]
                currentIndex += 4
                #print("2 Multiply")
            elif input[currentIndex] == 99:
                currentIndex = 'end'
                #print("99 End")

        return input[0]
    

    for i in range(99):
        for j in range(99):
            output = Computer(memory, i, j)
            if output == 19690720:
                print("noun is", i)
                print("verb is", j)
                print("100 * noun + verb = ", (100 * i + j))



partTwo('input.txt')