from collections import deque
input = open('5.in').read()


def react1():
    Q = deque()
    for c in input:
        try:
            top = Q.pop()
        except:
            Q.append(c)
            continue
        if abs(ord(c) - ord(top)) != 32:
            Q.append(top)
            Q.append(c)
    print(len(Q))

react1()


def react2():
    def react(ch):
        Q = deque()
        for c in input:
            if c.lower() == ch:
                continue
            try:
                top = Q.pop()
            except:
                Q.append(c)
                continue
            if abs(ord(c) - ord(top)) != 32:
                Q.append(top)
                Q.append(c)
        return len(Q)

    minim = len(input)
    for i in range(26):
        length = react(chr(ord('a') + i))
        if minim > length:
            minim = length
    print(minim)
react2()