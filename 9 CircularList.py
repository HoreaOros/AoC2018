players = 427
last = 7072300

class Node:
    def __init__(self, value):
        self.Value = value
        self.Next = None
        self.Previous = None
class CircularList:
    def __init__(self):
        self.Current = None
        self.Count = 0
    def AddAfterCurrent(self, value):
        node = Node(value)
        if self.Count == 0:
            self.Current = node
            self.Current.Next = self.Current
            self.Current.Previous = self.Current
        elif self.Count == 1:
            node.Next = self.Current.Next
            node.Previous = self.Current
            self.Current.Next = node
            self.Current.Previous = node
            self.Current = node
        else:
            node.Next = self.Current.Next
            node.Previous = self.Current
            self.Current.Next.Previous = node
            self.Current.Next = node
            self.Current = node
        self.Count += 1
    def Print(self):
        p = self.Current
        for _ in range(self.Count):
            print(f'{p.Value} ', end = '')
            p = p.Next
        print()
    def MoveClockWise(self):
        self.Current = self.Current.Next
    def MoveCounterClockWise(self):
        self.Current = self.Current.Previous
    def RemoveCurrent(self):
        p = self.Current.Next
        self.Current.Previous.Next = p
        p.Previous = self.Current.Previous
        self.Current = p

# lst = CircularList()
# lst.AddAfterCurrent(0)
# for i in range(1, 11):
#     lst.MoveClockWise()
#     lst.AddAfterCurrent(i)
#     lst.Print()

lst = CircularList()
lst.AddAfterCurrent(0)
c = [0]
currentElf = 1
currentMarble = 0

score = [0 for i in range(0, players)]
for m in range(1, last + 1):
    if m % 23 != 0:
        lst.MoveClockWise()
        lst.AddAfterCurrent(m)
    else:
        score[currentElf - 1] += m
        for _ in range(7):
            lst.MoveCounterClockWise()
        
        score[currentElf - 1] += lst.Current.Value
        lst.RemoveCurrent()
    
    currentElf += 1
    if currentElf == players + 1:
        currentElf = 1 
print(max(score))
