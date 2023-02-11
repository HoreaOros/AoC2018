from collections import deque
input = open('20.in').read().strip()[1:-1]


currentR = (0, 0)
rooms = set()
rooms.add(currentR)
doors = set()
Q = deque()
Q.append((currentR, input))
SEEN = set()
SEEN.add((currentR, input))
while Q:
    (currentR, s) = Q.popleft()
    try:
        prefix = s[:s.index('(')]
    except:
        prefix = s

    for c in prefix:
        x, y = currentR
        if c == 'N':
            currentR = (x, y - 2)
            currentD = (x, y - 1)
        elif c == 'S':
            currentR = (x, y + 2)
            currentD = (x, y + 1)
        elif c == 'W':
            currentR = (x - 2, y)
            currentD = (x - 1, y)
        elif c == 'E':
            currentR = (x + 2, y)
            currentD = (x + 1, y)
        rooms.add(currentR)
        doors.add(currentD)
    
    if prefix == s:
        continue
    
    pIdx = s.index('(')
    p = 0
    buf = ''
    tokens = []
    while True:
        c = s[pIdx]
        if c == '(':
            p += 1
            if p > 1:
                buf += c
        elif c == ')':
            p -= 1
            if p == 0:
                tokens.append(buf)
                pIdx += 1
                break
            elif p > 0:
                buf += c
        elif c == '|':
            if p == 1:
                tokens.append(buf)
                buf = ''
            else:
                buf += c
        else:
            buf += c
        pIdx += 1
    for t in tokens:
        newState = (currentR, t + s[pIdx:])
        if not newState in SEEN:
            Q.append(newState)
            SEEN.add(newState)
    pass

def tipar():
    for y in range(-10, 10):
        for x in range(-10, 10):
            if (x, y) == (0, 0):
                print('X', end = '')
            elif (x, y) in rooms:
                print('.', end = '')
            elif (x, y) in doors:
                if (x - 1, y) in rooms and (x + 1, y) in rooms:
                    print('|', end = '')
                elif (x, y + 1) in rooms and (x, y - 1) in rooms:
                    print('-', end = '')
            else:
                print('#', end = '')
        print()
    
#tipar()


SEEN = set()
Q = deque()
SEEN.add((0, 0))
start = ((0, 0), 0)
Q.append(start)

maxDepth = 0
part2 = 0
while Q:
    (point, depth) = Q.popleft()
    
    if depth >= 1000:
        part2 += 1
    if depth > maxDepth:
        maxDepth = depth

    x, y = point

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        newDoor = (x + dx[i], y + dy[i])
        newPoint = (x + 2 * dx[i], y + 2 * dy[i])
        if newDoor in doors:
            if not newPoint in SEEN:
                SEEN.add(newPoint)
                Q.append(((newPoint), depth + 1))
print(maxDepth)
print(part2)


