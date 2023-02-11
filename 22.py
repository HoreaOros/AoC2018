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
        
ROWS = target[1] + 1
COLS = target[0] + 1
geoIndex = np.zeros((ROWS, COLS), dtype = np.int64)
eroLevel = np.zeros((ROWS, COLS), dtype = np.int64)
type = np.zeros((ROWS, COLS), dtype = np.int64)

geoIndex[0, 0] = 0
geoIndex[ROWS - 1, COLS - 1] = 0

for i in range(ROWS):
    for j in range(COLS):
        if (i == 0 and j == 0) or (i == ROWS - 1 and j == COLS - 1):
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
for i in range(ROWS):
    for j in range(COLS):
        riskLevel += type[i, j]
print(riskLevel)
