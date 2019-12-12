# -------------------------------------------
# Day 1:
# Multiple lines
# Number on every line
#
inputList = []
with open("Day 1/input.txt") as file:
    for line in file:
        inputList.append(int(line.strip('\n')))

# ------------------------------------------
# Day 2, 5, 7, 9, 11:
# Single line
# comma delimited numbers
# 
with open("Day 2/input.txt") as file:
    inputList = [int(x) for x in file.read().split(",")]

# ------------------------------------------
# Day 3:
# Two lines
# comma delimited values that start with a letter
# 
with open("Day 3/input.txt") as file:
    lines = [line.strip('\n') for line in file]
    inputList = [line.split(',') for line in lines]

# ------------------------------------------
# Day 6:
# Multiple lines
# two numbers on each line delimited by ")"
# 
with open("Day 6/input.txt") as file:
   input = list(map(lambda x: x.split(")"), [line.strip("\n") for line in file]))

# ------------------------------------------
# Day 8:
# Single stream of digits
# Read digits into list 150 at a time
# 
layers = []
with open("Day 8/input.txt") as file:
    while True:
        layer = list(file.read(150))
        if not layer:
            break
        else:
            layers.append(layer)

# ------------------------------------------
# Day 10:
# Multiple Lines
# store each line as an element in a list
# 
with open("Day 10/input.txt") as file:
   input = [line.strip() for line in file]

# ------------------------------------------
# Day 12:
# Multiple Lines
# sets of items delimited by commas then by "=" signs
#
with open("Day 12/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [line.split(',') for line in lines]
    for i, line in enumerate(lines):
        lines[i] = [elm.split('=') for elm in line]