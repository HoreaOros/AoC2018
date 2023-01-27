
class Node:
    def __init__(self, childs, metadata):
        self.NumberOfChilds = childs
        self.Childs = []
        self.Metadata = []
    def Value(self):
        if self.Childs == []:
            return sum(self.Metadata)
        else:
            suma = 0
            for idx in self.Metadata:
                if idx >= 1 and idx <= len(self.Childs):
                    suma += (self.Childs[idx - 1]).Value()
            return suma


input = open('8.in').read().strip()

data = list(map(int, input.split(' ')))

totalMetadata = 0
metadata = []

stack = []
stack.append([data[0], data[1]])
sp = 1

k = 2
root = Node(data[0], data[1])
nodeStack = []
nodeStack.append(root)
nsp = 1 # NodeStack pointer

while sp > 0:
    if stack[sp - 1][0] > 0:
        stack[sp - 1][0] -= 1 
        stack.insert(sp, [data[k], data[k + 1]])
        sp += 1

        newNode = Node(data[k], data[k + 1])
        nodeStack[nsp - 1].Childs.append(newNode)
        nodeStack.insert(nsp, newNode)
        nsp += 1

        k += 2
    else:
        totalMetadata = stack[sp - 1][1]
        for i in range(k, k + totalMetadata):
            metadata.append(data[i])
            nodeStack[nsp - 1].Metadata.append(data[i])

        k += stack[sp - 1][1]
        sp -= 1
        nsp -= 1

print(sum(metadata))

print(root.Value())

