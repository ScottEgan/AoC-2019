"""
deal into new stack = 1
cut = 2
deal with increment = 3
"""

import numpy as np


with open("Day 22/input.txt") as file:
    input = [line.strip() for line in file]
# print(input)

def dealNewStack(deck):
    d = deck.copy()
    return d[::-1]

def cut(deck, num):
    d = deck.copy()
    return d[num:] + d[:num]

def dealWithIncr(deck, num):
    d = deck.copy()
    s = np.zeros((len(deck),), dtype=int)
    index = 0
    s[index] = d.pop(0)
    while d:
        if (index + num) < len(deck):
            index += num
        else:
            index = (index + num) - len(deck)
            
        s[index] = d.pop(0)
    return list(s)

# deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
deck = list(range(10007))   
#print(deck)

#taskList = []
for elm in input:
    
    if elm.split()[0] == 'cut':
        #taskList.append((2, int(elm.split()[1])))
        newDeck = cut(deck, int(elm.split()[1]))
    elif elm.split()[0] == 'deal':
        if elm.split()[1] == 'with':
            #taskList.append((3, int(elm.split()[3])))
            newDeck = dealWithIncr(deck, int(elm.split()[3]))
        elif elm.split()[1] == 'into':
            #taskList.append((1, 0))
            newDeck = dealNewStack(deck)
    deck = newDeck

#print(deck)

print(deck.index(2019))
