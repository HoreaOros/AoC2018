infile = open('12.in')
outfile = open('12.out', 'w')
initialState = infile.readline().strip()[15:]


infile.readline()
lines = infile.read().strip().split('\n')
r = dict()
for line in lines:
    t = line.split(' => ')
    r[t[0]] = t[1]


padding = 100
initialState = '...'  + initialState + '.' * (padding * 10)


def iterate(i, initialState):
    result = '..'
    for c in range(len(initialState) - 4):
        if initialState[c:c+5] in r:
            result += r[initialState[c:c+5]]
        else:
            result += '.'
    result += '..'
    outfile.write(str(i).rjust(3, ' ') + ' ' + result.rstrip('.'))
    outfile.write('\n')
    return result


def solve(initialState, iterations):
    state = initialState
    outfile.write('########### Part 1 ####################\n')
    outfile.write(str(0).rjust(3, ' ') + ' ' + initialState.rstrip('.'))
    outfile.write('\n')
    for i in range(iterations):
        state = iterate(i + 1, state)

    sum = 0
    for i, c in enumerate(state):
        if c == '#':
            sum += (i - 3) # pentru ca am adaugat 3 puncte la inceput
    print(sum)
    outfile.write('\n')

# part1
solve(initialState, 20)


def part2(initialState):
    S = list()
    S.append(initialState.strip('.'))

    i = 1
    state = initialState
    while True:
        r = iterate(i, state)
        try:
            idx = S.index(r.strip('.'))
            break
        except:
            i += 1
            state = r
            S.append(state.strip('.'))
    print(f'After {i} iterations repeats index {idx}')
    #print(r)

#part2(initialState)

def part2_2(initialState):
    state = initialState
    for i in range(300):
        r = iterate(i, state)
        state = r
        

part2_2(initialState)

pots = '.............................##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##....##.##.##.##.##.##....##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##.##'
def score(line):
    score = 0
    for i, c in enumerate(line):
        if c == '#':
            score += i
    return score

flori = pots.count('#')

print(score(pots) + flori * (50000000000 - 93))




