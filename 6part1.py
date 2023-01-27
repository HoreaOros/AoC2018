lines = open('6.in').read().strip().split('\n')
coords = []
for line in lines:
    t = line.split(', ')
    coords.append((int(t[0]), int(t[1])))
# print(coords)
# print(len(coords))
x1 = min(coords, key = lambda x: x[0])
x2 = max(coords, key = lambda x: x[0])
y1 = min(coords, key = lambda x: x[1])
y2 = max(coords, key = lambda x: x[1])
# print(x1, x2)
# print(y1, y2)


def ManhatanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# count = [0 for _ in range(len(coords))]
# for x in range(-500, 700):
#     print(x)
#     for y in range(-500, 700):
#         distances = [0 for _ in range(len(coords))]
#         for i in range(len(coords)):
#             distances[i] = ManhatanDistance(coords[i], (x, y))
#         minim = min(distances)
#         contor = distances.count(minim)
#         if contor == 1:
#             idx = distances.index(minim)
#             count[idx] += 1
# din lista generata si sortata se gaseste raspunsul: 3840
count = [1346, 26676, 1070, 1400, 1732, 1462, 5384, 9580, 1592, 2630, 19111, 1579, 1170, 2476, 360591, 24682, 31638, 6266, 540, 2700, 2424, 2679, 10414, 1862, 46106, 23695, 2067, 2935, 24144, 1560, 23667, 2351, 5007, 251491, 145735, 25294, 33720, 1136, 1062, 627, 3840, 1645, 54331, 1465, 1054, 226995, 1712, 2737, 14123, 8247]
count = list(sorted(count))
print(count)

# [540, 627, 1054, 1062, 1070, 1136, 1170, 1346, 1400, 1462, 1465, 1560, 1579, 1592, 1645, 1712, 1732, 1862, 2067, 2351, 2424, 2476, 2630, 2679, 2700, 2737, 2935, 3840, 5007, 5384, 6266, 8247, 9580, 10414, 14123, 19111, 23667, 23695, 24144, 24682, 25294, 26676, 31638, 33720, 46106, 54331, 145735, 226995, 251491, 360591]

