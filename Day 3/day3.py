import numpy as np
import re

with open('input.txt') as file:
    board = file.readlines()

barray = np.array([list(row.rstrip('\n')) for row in board])

carray = ~np.isin(barray, list('0123456789.') + ['\n'])

chars = {}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = np.zeros_like(barray, dtype=bool)
        edge[max(r-1, 0):min(r+2, barray.shape[0]), 
             max(n.start()-1, 0):min(n.end()+1, barray.shape[1])] = True

        overlap = np.where(carray & edge)
        for position in zip(*overlap):
            chars.setdefault(position, []).append(int(n.group()))

p1 = np.sum([sum(p) for p in chars.values()])
p2 = np.prod([p for p in chars.values() if len(p) == 2], axis=1).sum()

print(p1, p2)
