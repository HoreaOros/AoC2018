import numpy as np

lines = open('18.in').read().strip().split('\n')
N = len(lines)


f = np.zeros((N + 2, N + 2), dtype=int)

for i, line in enumerate(lines, 1):
    for j, c in enumerate(line, 1):
        match c:
            case '.':
                f[i, j] = 1
            case '|':
                f[i, j] = 2
            case '#':
                f[i, j] = 3


def countAdjacent(f, i, j):
    dr = [0, 0,   1, 1, 1, -1, -1, -1]
    dc = [1, -1, -1, 0, 1, -1,  0,  1]
    open = 0
    tree = 0
    lumberyard = 0
    for k in range(len(dr)):
        nr = i + dr[k]
        nc = j + dc[k]
        match f[nr, nc]:
            case 1:
                open += 1
            case 2:
                tree += 1
            case 3:
                lumberyard += 1
    return (open, tree, lumberyard)

def step(f):
    f2 = np.zeros((N + 2, N + 2), dtype=int)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            (open, trees, lumberyard) = countAdjacent(f, i, j)
            match f[i, j]:
                case 1: # open
                    if trees >= 3:
                        f2[i, j] = 2
                    else:
                        f2[i, j] = 1
                case 2: # trees
                    if lumberyard >= 3:
                        f2[i, j] = 3
                    else:
                        f2[i, j] = 2
                case 3: # lumberyard
                    if lumberyard >= 1 and trees >= 1:
                        f2[i, j] = 3
                    else:
                        f2[i, j] = 1

    return f2


def tipar(s, f):
    print(s)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            match f[i, j]:
                case 1:
                    print('.', end = '')
                case 2:
                    print('|', end = '')
                case 3:
                    print('#', end = '')
        print()
def resourceValue(f):
    tree = 0
    lumberyard = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
                match f[i, j]:
                    case 2:
                        tree += 1
                    case 3:
                        lumberyard += 1
    return (tree * lumberyard)

def part1(f, minutes):
    #tipar('Initial state', f)
    for _ in range(minutes):
        f = step(f)
    #    tipar(f'After {i + 1} minutes', f)
    print(resourceValue(f))
    print('End part 1')


def matrixHash(f):
    p = 3 
    q = 5
    prime = 1500450271
    h = 0
    suma = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            suma += f[i, j] * (p ** i % prime) * (q ** j % prime) % prime
    return suma

def part2(f):
    SEEN = []
    SEEN.append(matrixHash(f))
    while True:
        f = step(f)
        mh = matrixHash(f)
        if mh in SEEN:
            break
        else:
            SEEN.append(mh)
    # print(len(SEEN))
    # print(SEEN.index(mh))


    
    cycleLenght = len(SEEN) - SEEN.index(mh)
    nonCycleStart = SEEN.index(mh)
    # cycles = (1_000_000_000 - nonCycleStart + 1) / cycleLenght
    rem = (1_000_000_000 - nonCycleStart + 1) % cycleLenght

    for _ in range(rem - 1):
        f = step(f)
    print(resourceValue(f))


part1(f, 10)
part2(f)

