import re
import numpy as np
from collections import deque

lines = open('17.in').read().strip().split('\n')
grid = []
for line in lines:
    t = line.split(', ')
    nums = list(map(int, re.findall(r'\d+', line)))
    grid.append((t[0].split('=')[0], nums[0], nums[1], nums[2]))

#print(grid)
xmin = 10000
ymin = 10000
xmax = 0
ymax = 0
for defs in grid:
    if defs[0] == 'x':
        ymin = min(ymin, defs[2])
        ymax = max(ymax, defs[3])
        xmin = min(xmin,defs[1])
        xmax = max(xmax,defs[1])
    elif defs[0] == 'y':
        xmin = min(xmin, defs[2])
        xmax = max(xmax, defs[3])
        ymin = min(ymin,defs[1])
        ymax = max(ymax,defs[1])
print(f'xmin = {xmin}, xmax = {xmax}, ymin = {ymin}, ymax = {ymax}')

ROWS = 2000
COLS = 700
mat = np.zeros((2000, 700), dtype = str)
for i in range(ROWS):
    for j in range(COLS):
        mat[i, j] = '.'
mat[0, 500] = '+'

for defs in grid:
    if defs[0] == 'x':
        for i in range(defs[2], defs[3] + 1):
            mat[i, defs[1]] = '#'
    elif defs[0] == 'y':
        for j in range(defs[2], defs[3] + 1):
            mat[defs[1], j] = '#'

def tipar(mat):
    for i in range(0, 14):
        for j in range(494, 508):
            print(mat[i, j], end = '')
        print()
    print()

def fill(mat, flag):
    overspill = False
    settling = False
    Q = deque()
    Q.append((0, 500))
    SEEN = set()
    SEEN.add((0, 500))
    while Q:
        row, col = Q.popleft()
        if row >= ymax:
            overspill = True
            continue
        
        
        if mat[row + 1, col] == '.':
            if not (row + 1, col) in SEEN:
                SEEN.add((row + 1, col))
                mat[row + 1, col] = '|'
                Q.append((row + 1, col))
        elif mat[row + 1, col] in '#~':
            if mat[row, col - 1] == '.':
                if not (row, col - 1) in SEEN:
                    SEEN.add((row, col - 1))
                    mat[row, col - 1] = '|'
                    Q.append((row, col - 1))
            if mat[row, col + 1] == '.':
                if not (row, col + 1) in SEEN:
                    SEEN.add((row, col + 1))
                    mat[row, col + 1] = '|'
                    Q.append((row, col + 1))
    # settle water
    if flag:
        for i in range(1, ymax + 1):
            settled = []
            for j in range(xmin - 1, xmax + 2):
                if mat[i, j] == '|':
                    left = False
                    right = False
                    k = 0
                    while mat[i, j + k] == '|':
                        k += 1
                    if mat[i, j + k] == '#':
                        right = True
                    k = 0
                    while mat[i, j - k] == '|':
                        k += 1
                    if mat[i, j - k] == '#':
                        left = True

                    if left and right:
                        settled.append(j)
                        settling = True
            pass
            for j in range(xmin - 1, xmax + 2):
                if mat[i, j] == '|':
                    if j in settled:
                        mat[i, j] = '~'
                    else:
                        mat[i, j] = '.'
    return (overspill, settling)
outFile = open('17.out', 'w')
def tiparFile(mat, xmin, xmax, ymin, ymax):
    for i in range(0, ymax):
        for j in range(xmin - 1, xmax + 2):
            outFile.write(mat[i, j])
        outFile.write('\n')
    outFile.write('\n')


i = 0
while True:
    print(i)
    i += 1
    overspill, settling = fill(mat, True)
    tiparFile(mat, xmin, xmax, ymin, ymax)
    if overspill and not settling:
        fill(mat, False)
        tiparFile(mat, xmin, xmax, ymin, ymax)
        break

cntSettled = 0
cntSpill = 0
for i in range(ymin, ROWS):
    for j in range(COLS):
        if mat[i, j] == '~':
            cntSettled += 1
        elif mat[i, j] == '|':
            cntSpill += 1
print(cntSettled + cntSpill)
print(cntSettled)
pass


