input = 8561
#input = 18
N = 300
cells = [ [0 for x in range(1, N + 1)]   for y in range(1, N + 1)]
#print(cells)

for y in range(1, N + 1):
    for x in range(1, N + 1):
        rackID = x + 10
        powerLevel = rackID * y
        powerLevel += input
        powerLevel *= rackID
        powerLevel = powerLevel % 1000 // 100
        powerLevel -= 5
        cells[y - 1][x - 1] = powerLevel

def part1(size):
    largestTotalPower = 0
    xmax = 0
    ymax = 0
    for y in  range(N - size + 1):
        for x in range(N - size + 1):
            sum = 0
            for i in range(size):
                for j in range(size):
                    sum += cells[y + i][x + j]
            if sum > largestTotalPower:
                largestTotalPower = sum
                xmax = x
                ymax = y

    return (xmax + 1, ymax + 1, largestTotalPower)


xmax, ymax, largestTotalPower = part1(3)
print(str(xmax) + ',' + str(ymax))

largestTotalPower = 0
xmax = 0
ymax = 0
sizeMax = 0
for size in range(1, N + 1):
    x, y, power = part1(size)
    if power > largestTotalPower:
        largestTotalPower = power
        xmax = x
        ymax = y
        sizeMax = size
print(str(xmax) + ',' + str(ymax) + ',' + str(sizeMax))

