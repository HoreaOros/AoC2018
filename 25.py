# determinare numar componente conexe intr-un graf. Varfurile grafului sunt punctele. 
# intre doua  varfuri este muchie daca distanta manhatan dintre cele doua puncte e <= 3


import re
from collections import deque
lines = open('25.in').read().strip().split('\n')
points = []
def ManhatanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])
constelations = []
for line in lines:
    t = re.findall(r'-?\d+', line)
    points.append((int(t[0]), int(t[1]), int(t[2]), int(t[3])))
print(points)

g = dict()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if ManhatanDistance(points[i], points[j]) <= 3:
            if i in g:
                g[i].append(j)
            else:
                g[i] = [j]
            if j in g.keys():
                g[j].append(i)
            else:
                g[j] = [i]
print(g)

isolatedNodes = len(points) - len(g)

cc = []
idx = 0
seen = set()
while g:
    node = list(g.keys())[0]
    cc.append([node])
    idx += 1
    Q = deque()
    Q.append(node)
    seen.add(node)
    while Q:
        node = Q.popleft()

        
        for neighbour in g[node]:
            if not neighbour in seen:
                seen.add(neighbour)
                Q.append(neighbour)
                cc[idx - 1].append(neighbour)
    for n in cc[idx - 1]:
        g.pop(n, None)
print(idx + isolatedNodes)
        
