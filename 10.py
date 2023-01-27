import re
lines = open('10.in').read().strip().split('\n')
points = []
for line in lines:
    t = re.findall(r'-?\d+', line)
    points.append([int(t[0]), int(t[1]), int(t[2]), int(t[3])])



def tipar(points, x1, x2, y1, y2):
    outfile = open('10.out', 'w')
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            ok = False
            for p in points:
                if p[0] == x and p[1] == y:
                    outfile.write('#')
                    ok = True
                    break
            if not ok:
                outfile.write(' ')
        outfile.write('\n')


count = 0
while True:
    count += 1
    for i in  range(len(points)):
        points[i][0] += points[i][2]
        points[i][1] += points[i][3]
    x1 = min(points, key = lambda arg: arg[0])[0]
    x2 = max(points, key = lambda arg: arg[0])[0]

    y1 = min(points, key = lambda arg: arg[1])[1]
    y2 = max(points, key = lambda arg: arg[1])[1]
    
    if y2 - y1 < 12:
        tipar(points, x1, x2, y1, y2)
        break
print(count)
