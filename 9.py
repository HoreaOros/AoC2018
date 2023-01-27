players = 427
last = 70723


def solve(last):
    c = [0]
    currentElf = 1
    currentMarble = 0

    score = [0 for i in range(0, players)]
    for m in range(1, last + 1):
        if m % 23 != 0:
            dest = currentMarble + 2
            if dest < len(c):
                c.insert(dest, m)
                currentMarble = dest
            elif dest == len(c):
                c.append(m)
                currentMarble = len(c) - 1
            else:
                c.insert(1, m)
                currentMarble = 1
        else:
            score[currentElf - 1] += m
            dest = currentMarble - 7
            if dest < 0:
                dest = len(c) + dest
            score[currentElf - 1] += c[dest]
            c.pop(dest)
            if dest == len(c):
                currentMarble = 0
            else:
                currentMarble = dest
        # print(f'[{currentElf}] ', end = '')
        # for i in range(len(c)):
        #     if i == currentMarble:
        #         print(f'({c[i]}) ', end = '')
        #     else:
        #         print(f' {c[i]} ', end = '')
        # print()
        
        currentElf += 1
        if currentElf == players + 1:
            currentElf = 1   
    print(max(score))

            
#solve(last)
solve(last * 100)