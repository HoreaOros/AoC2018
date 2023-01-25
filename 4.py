import re
lines = open('4.in').read().strip().split('\n')

def nextDay(month, day):
    if month == 1 and day == 31:
        return (2, 1)
    elif month == 2 and day == 28:
        return (3, 1)
    elif month == 3 and day == 31:
        return (4, 1)
    elif month == 4 and day == 30:
        return (5, 1)
    elif month == 5 and day == 31:
        return (6, 1)
    elif month == 6 and day == 30:
        return (7, 1)
    elif month == 7 and day == 31:
        return (8, 1)
    elif month == 8 and day == 31:
        return (9, 1)
    elif month == 9 and day == 30:
        return (10, 1)
    elif month == 10 and day == 31:
        return (11, 1)
    elif month == 11 and day == 30:
        return (12, 1)
    return (month, day + 1)
records = []
for line in lines:
    t = re.search(r'^\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\]', line)
    time = (int(t.group(1)), int(t.group(2)), int(t.group(3)), int(t.group(4)), int(t.group(5)))
    if time[3] == 23:
        (month, day) = nextDay(time[1], time[2])
        time = (time[0], month, day, 0, 0)
    records.append((time, line[19:].split(' ')))


outfile = open('4.out', 'w')
records = sorted(records, key = lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[1][0]))
for r in records:
    outfile.write(str(r) + '\n')

g = dict()

guardId = -1
time = 0
sleeping = False
for r in records:
    if r[1][0] == 'Guard':
        # rezolvam dormitul la final de shit pentru cel anterior
        if guardId != -1 and sleeping:
            for t in range(time, 60):
                g[guardId][t] += 1
        
        guardId = int(r[1][1][1:])
        sleeping = False
        time = 0
        if not guardId in g:
            g[guardId] = [0 for _ in range(60)]

    elif r[1][0] == 'falls':
        time = r[0][4]
        sleeping = True
    elif r[1][0] == 'wakes':
        for t in range(time, r[0][4]):
            g[guardId][t] += 1
        sleeping = False


maxMinutesAsleep = 0
maxMinute = 0
maxid = 0
for id in g:
    suma = sum(g[id])
    if suma > maxMinutesAsleep:
        maxMinutesAsleep = suma
        maxMinute = g[id].index(max(g[id]))
        maxid = id

print(maxid * maxMinute)


maxSleepMinute = 0
for id in g:
    if max(g[id]) > maxSleepMinute:
        maxSleepMinute = max(g[id])
        maxid2 = id
        maxMinute2 = g[id].index(max(g[id]))
print(maxid2 * maxMinute2)


