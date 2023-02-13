from collections import deque
import numpy as np
depth = 5913
target = (8,701)
# depth = 510
# target = (10,10)
def erosionLevel(x, y):
    return (geologicalIndex(x, y) + depth) % 20183
def geologicalIndex(x, y):
    if x == 0 and y == 0 or (x, y) == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosionLevel(x-1, y) * erosionLevel(x, y - 1)

def regionType(x, y):
    match erosionLevel(x, y) % 3:
        case 0:
            return 'R' # rocky
        case 1:
            return 'W' # wet
        case 2:
            return 'N' # narrow
        
# ROWS = target[1] + 1
# COLS = target[0] + 1
ROWS = target[1] +1000
COLS = target[0] +1000
geoIndex = np.zeros((ROWS, COLS), dtype = np.int64)
eroLevel = np.zeros((ROWS, COLS), dtype = np.int64)
type = np.zeros((ROWS, COLS), dtype = np.int64)

geoIndex[0, 0] = 0
geoIndex[target[1], target[0]] = 0

for i in range(ROWS):
    for j in range(COLS):
        if (i == 0 and j == 0) or (i == target[1] and j == target[0]):
            geoIndex[i, j] = 0
        elif i == 0:
            geoIndex[i, j] = j * 16807
        elif j == 0:
            geoIndex[i, j] = i * 48271
        else:
            geoIndex[i, j] = eroLevel[i - 1, j] * eroLevel[i, j - 1]
        eroLevel[i, j] = (geoIndex[i, j] + depth) % 20183
        type[i, j] = eroLevel[i, j] % 3

# for i in range(ROWS):
#     for j in range(COLS):
#         match type[i, j]:
#             case 0:
#                 print('.', end = '')
#             case 1:
#                 print('=', end = '')
#             case 2:
#                 print('|', end = '')
#     print()

riskLevel = 0
for i in range(target[1] + 1):
    for j in range(target[0] + 1):
        riskLevel += type[i, j]
print(riskLevel)


targetPosition = (target[1], target[0])
 # (0, 0) == neither, (1, 0) torch, (0, 1) climbing
torch = 'torch'
climbing = 'climbing'
neither = 'neither'
equipment = torch


time = 0


import heapq
stateQ = (time, (0, 0), equipment)

Q = [stateQ]

best = dict() # (x, y, cannot) : minutes

target = ((target[1], target[0]),torch)

while Q:
    state = heapq.heappop(Q)
    time, currentPosition, equipment = state
    
    best_key = (currentPosition, equipment)
    if best_key in best and best[best_key] <= time:
        continue
    best[best_key] = time
    if best_key == target:
        print(time)
        break

    i, j = currentPosition
    #change equipment:
    if type[i, j] == 0: # rocky
        if equipment == torch:
            newEquipment = climbing
        elif equipment == climbing:
            newEquipment = torch
    elif type[i, j] == 1: # wet
        if equipment == climbing:
            newEquipment = neither
        elif equipment == neither:
            newEquipment = climbing
    elif type[i, j] == 2: # narrow
        if equipment == torch:
            newEquipment = neither
        elif equipment == neither:
            newEquipment = torch
    newStateWithChngEquipment = (time + 7, (i, j), newEquipment)
    heapq.heappush(Q, newStateWithChngEquipment)

    #change position
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in range(4):
        newi = i + dx[t]
        newj = j + dy[t]

        if newi >= 0 and newj >= 0 and newi < ROWS and newj < COLS:
            newStateWithSameEquipment = (time + 1, (newi, newj), equipment)


            okSame = False
            okChng = False
            if equipment == torch:
                if type[newi, newj] == 0 or type[newi, newj] == 2: # rocky or narrow
                    okSame = True
            elif equipment == climbing:
                if type[newi, newj] == 0 or type[newi, newj] == 1: # rocky or wet
                    okSame = True
            elif equipment == neither:
                if type[newi, newj] == 1 or type[newi, newj] == 2: # wet or narrow
                    okSame = True
            
            if newEquipment == torch:
                if type[newi, newj] == 0 or type[newi, newj] == 2: # rocky or narrow
                    okChng = True
            elif newEquipment == climbing:
                if type[newi, newj] == 0 or type[newi, newj] == 1: # rocky or wet
                    okChng = True
            elif newEquipment == neither:
                if type[newi, newj] == 1 or type[newi, newj] == 2: # wet or narrow
                    okChng = True
            
            if okSame:
                heapq.heappush(Q, newStateWithSameEquipment)
            

