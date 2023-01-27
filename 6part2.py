lines = open('6.in').read().strip().split('\n')
coords = []
for line in lines:
    t = line.split(', ')
    coords.append((int(t[0]), int(t[1])))
# print(coords)
# print(len(coords))


def ManhatanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

size = 0
for x in range(-500, 700):
    for y in range(-500, 700):
        sum = 0
        for i in range(len(coords)):
            sum += ManhatanDistance(coords[i], (x, y))
            if sum > 10000:
                break
        if sum < 10000:
            size += 1
print(size)
