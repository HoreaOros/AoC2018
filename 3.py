import re
import numpy as np
data = open('3.in').read().strip().split('\n')
rects = []
class Rect:
    def __init__(self, id, x, y, dx, dy):
        self.Id = id
        self.Left = x
        self.Top = y
        self.Width = dx
        self.Height = dy

for line in data:
    t = re.findall(r'\d+', line)
    rects.append(Rect(int(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4])))

fabric = np.zeros((2000, 2000), dtype = int)
for r in rects:
    for i in range(r.Height):
        for j in range(r.Width):
            if fabric[r.Top + i, r.Left + j] == 0:
                fabric[r.Top + i, r.Left + j] = 1
            elif fabric[r.Top + i, r.Left + j] == 1:
                fabric[r.Top + i, r.Left + j] = 2
count = 0
for i in range(2000):
    for j in range(2000):
        if fabric[i, j] == 2:
            count += 1
print(f'{count} square inches within more than one claim')

# part 2
for r in rects:
    overlap = False
    for i in range(r.Height):
        for j in range(r.Width):
            if fabric[r.Top + i, r.Left + j] == 2:
                overlap = True
    if overlap == False:
        print(f'Claim {r.Id} does not overlap with any other')
        break
