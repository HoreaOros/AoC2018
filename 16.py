import re
infile = open('16.in')

opcodes = [set() for i in range(16)]

# Addition
def addr(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] + regBefore[op[2]]
    return regBefore == regAfter
def addi(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] + op[2]
    return regBefore == regAfter

# Multiplication
def mulr(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] * regBefore[op[2]]
    return regBefore == regAfter
def muli(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] * op[2]
    return regBefore == regAfter

# Bitwise AND
def banr(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] & regBefore[op[2]]
    return regBefore == regAfter
def bani(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] & op[2]
    return regBefore == regAfter

# Bitwise OR
def borr(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] | regBefore[op[2]]
    return regBefore == regAfter
def bori(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]] | op[2]
    return regBefore == regAfter

# Assignment
def setr(regBefore, op, regAfter):
    regBefore[op[3]] = regBefore[op[1]]
    return regBefore == regAfter
def seti(regBefore, op, regAfter):
    regBefore[op[3]] = op[1]
    return regBefore == regAfter

# Greater-than testing
def gtir(regBefore, op, regAfter):
    if op[1] > regBefore[op[2]]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter
def gtri(regBefore, op, regAfter):
    if regBefore[op[1]] > op[2]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter
def gtrr(regBefore, op, regAfter):
    if regBefore[op[1]] > regBefore[op[2]]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter

# Equality testing
def eqir(regBefore, op, regAfter):
    if op[1] == regBefore[op[2]]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter
def eqri(regBefore, op, regAfter):
    if regBefore[op[1]] == op[2]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter
def eqrr(regBefore, op, regAfter):
    if regBefore[op[1]] == regBefore[op[2]]:
        regBefore[op[3]] = 1
    else:
        regBefore[op[3]] = 0
    return regBefore == regAfter

op16 = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

count = 0
totalSample = 0
while True:
    line1 = infile.readline()
    if line1.startswith('Before'):
        totalSample += 1
        line2 = infile.readline()
        line3 = infile.readline()
        _ = infile.readline() # blank line
        regsBefore = list(map(int, re.findall(r'\d+', line1)))
        instr = list(map(int, re.findall(r'\d+', line2)))
        regsAfter = list(map(int, re.findall(r'\d+', line3)))
        #print(regsBefore, instr, regsAfter)
        r = [op(list(regsBefore), instr, regsAfter) for op in op16]
        if r.count(True) >= 3:
            count += 1
        for i, b in enumerate(r):
            if b:
                opcodes[instr[0]].add(op16[i])
    else:
        break

print(count)

def tipar(opcode):
    for i, oc in enumerate(opcodes):
        print(i, ':', end = '')
        for c in oc:
            print(c.__name__, end = '')
            print(' ', end = ' ' )
        print()
#tipar(opcodes)

for i in range(16):
    opcodes[i] = list(opcodes[i])

removed = set()
while True:
    toRemove = None
    for oc in opcodes:
        if len(oc) == 1 and not oc[0] in removed:
            toRemove = oc[0]
            break
    if toRemove == None:
        break
    
    for oc in opcodes:
        if len(oc) > 1 and toRemove in oc:
            oc.remove(toRemove)
    removed.add(toRemove)

    
#tipar(opcodes)

line = infile.readline()

lines = infile.read().strip().split('\n')

regs = [0, 0, 0, 0]
for line in lines:
    instr = list(map(int, re.findall(r'\d+', line)))
    opcodes[instr[0]][0](regs, instr, regs)
    #print(regs)
print(regs[0])
