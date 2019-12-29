import numpy as np


with open("Day 22/inputTest.txt") as file:
    input = [line.strip() for line in file]
print(input)
deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    
print(deck)