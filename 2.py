lines = open('2.in').read().strip().split('\n')

def part1():
    def calculFrecventa(line):
        d = dict()
        for ch in line:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        return d

    c2=0
    c3=0

    for line in lines:
        d=calculFrecventa(line) 
        if 2 in d.values():
            c2 += 1
        if 3 in d.values():
            c3 += 1
    print(c2 * c3)



part1()

def countDiffPos(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def getFirstDiffIndex(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return i
    return -1

def part2():
    N = len(lines)
    for i in range(N):
        for j in range(i):
            if countDiffPos(lines[i], lines[j]) == 1:
               pos = getFirstDiffIndex(lines[i], lines[j])
               result = lines[i][:pos] + lines[i][pos+1:]
               print(result)

part2()
