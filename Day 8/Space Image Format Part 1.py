"""
"""
from collections import Counter

layers = []

with open("Day 8/input.txt") as file:
    while True:
        layer = list(file.read(150))
        if not layer:
            break
        else:
            layers.append(layer)

        
    
zeros = 150
multi = 0

for elm in layers:
    c = Counter(elm)
    if c['0'] < zeros:
        zeros = c['0']
        multi = c['1'] * c['2']

print(multi)
