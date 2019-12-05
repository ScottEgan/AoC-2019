"""
Part One
Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, 
take its mass, divide by three, round down, and subtract 2.
What is the sum of the fuel requirements for all of the modules on your spacecraft?

Part Two
Fuel itself requires fuel just like a module - 
take its mass, divide by three, round down, and subtract 2. 
However, that fuel also requires fuel, and that fuel requires fuel, and so on.
What is the sum of the fuel requirements for all of the modules on your spacecraft 
when also taking into account the mass of the added fuel? 
(Calculate the fuel requirements for each module separately, then add them all up at the end.)
"""

import math

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
        for line in file:
            inputList.append(int(line.strip('\n')))
    return inputList



def partOne(inputText):
    """Part One

    Parameters:
    inputText (string): file name of file to import

    Returns:
    int: total fuel required for all parts
    """

    masses = load_file(inputText)
    fuel_required = 0

    print("Calculating fuel required...")
    for mass in masses:
        fuel_required += (math.floor(mass/3)) - 2

    return fuel_required
 
def partTwo(inputText):
    """Part Two - going to have to be a recursive solution

    Parameters:
    inputText (string): file name of file to import

    Returns:
    int: total fuel required for all parts
    """
    def calc_fuel(mass):
        """This function will be used for the recursive part
        Parameters:
        mass (int): input mass

        Returns:
        int: fuel required for the input mass
        """
        fuel = (math.floor(mass/3)) - 2
        if fuel <= 0:
            return  0
        else:
            return fuel + calc_fuel(fuel)
    
    masses = load_file(inputText)
    fuel_required = 0

    print("Calculating fuel required...")
    for mass in masses:
        fuel_required += calc_fuel(mass)

    return fuel_required

print("Total fuel required for Part 1 =", partOne('input.txt'))
print("Total fuel required for Part 2 =", partTwo('input.txt'))