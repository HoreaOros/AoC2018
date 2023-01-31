class Cart:
    def __init__(self, i, j, dir):
        self.Row = i
        self.Column = j
        self.Direction = dir
        self.Turn = 0 # 0 == left, 1 == straight, 2 == right
    def GetLocation(self):
        return (self.Row, self.Column)
    def MoveForeword(self):
        if self.Direction == 'N':
            self.Row -= 1
        elif self.Direction == 'S':
            self.Row += 1
        elif self.Direction == 'W':
            self.Column -= 1
        elif self.Direction == 'E':
            self.Column += 1

    def TurnLeft(self):
        if self.Direction == 'N':
            self.Direction = 'W'
        elif self.Direction == 'S':
            self.Direction = 'E'
        elif self.Direction == 'W':
            self.Direction = 'S'
        elif self.Direction == 'E':
            self.Direction = 'N'
    

    def TurnRight(self):
        if self.Direction == 'N':
            self.Direction = 'E'
        elif self.Direction == 'S':
            self.Direction = 'W'
        elif self.Direction == 'W':
            self.Direction = 'N'
        elif self.Direction == 'E':
            self.Direction = 'S'
    def Move(self, tracks):
        # daca e cazul ma intorc
        ch = tracks[self.Row][self.Column]
        if ch == '+':
            if self.Turn == 0:
                self.TurnLeft()
            elif self.Turn == 2:
                self.TurnRight()
            self.Turn  = (self.Turn + 1) % 3
        elif ch == '/':
            if self.Direction == 'N':
                self.Direction = 'E'
            elif self.Direction == 'S':
                self.Direction = 'W'
            elif self.Direction == 'W':
                self.Direction = 'S'
            elif self.Direction == 'E':
                self.Direction = 'N'
        elif ch == '\\':
            if self.Direction == 'N':
                self.Direction = 'W'
            elif self.Direction == 'S':
                self.Direction = 'E'
            elif self.Direction == 'W':
                self.Direction = 'N'
            elif self.Direction == 'E':
                self.Direction = 'S'
        # ma duc inainte
        self.MoveForeword()
tracks = open('13.in').read().split('\n')
carts = []
for i, line in enumerate(tracks):
    for j, c in enumerate(line):
        if c == '<':
            carts.append(Cart(i, j, 'W'))
        elif c == '>':
            carts.append(Cart(i, j, 'E'))
        elif c == 'v':
            carts.append(Cart(i, j, 'S'))
        elif c == '^':
            carts.append(Cart(i, j, 'N'))
    
for i in range(len(tracks)):
    tracks[i] = tracks[i].replace('<', '-')
    tracks[i] = tracks[i].replace('>', '-')
    tracks[i] = tracks[i].replace('v', '|')
    tracks[i] = tracks[i].replace('^', '|')

print()

def crash(carts):
    for i in range(len(carts) - 1):
        for j in range(i + 1, len(carts)):
            if carts[i].GetLocation() == carts[j].GetLocation():
                return (True, carts[i].GetLocation())
    return (False, (-1, -1))


def tipar(carts, tracks):
    for i, line in enumerate(tracks):
        for j, c in enumerate(line):
            found = False
            for cart in carts:
                if (i, j) == cart.GetLocation():
                    found = True
                    if cart.Direction == 'N':
                        print('^', end = '')
                    elif cart.Direction == 'S':
                        print('v', end = '')
                    elif cart.Direction == 'W':
                        print('<', end = '')
                    elif cart.Direction == 'E':
                        print('>', end = '')
                    break
            if not found:
                print(tracks[i][j], end = '')
        print()
    print()


part1 = False
while True:
    carts = list(sorted(carts, key = lambda arg: (arg.Row, arg.Column)))
    for c in carts:
        c.Move(tracks)
        (result, location) = crash(carts)
        if result:
            print(str(location[1]) + ',' + str(location[0]))
            part1 = True
            break
    #tipar(carts, tracks)
    if part1:
        break