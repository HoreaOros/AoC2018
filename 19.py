import re
lines = open('19.in').read().strip().split('\n')
ipReg = int(lines[0].split(' ')[1])


regs = [0, 0, 0, 0, 0, 0]
prog = []
for i in range(1, len(lines)):
    t = lines[i].split(' ')
    prog.append((t[0], int(t[1]), int(t[2]), int(t[3])))

# Addition
def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
def addi(regs, a, b, c):
    regs[c] = regs[a] + b

# Multiplication
def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
def muli(regs, a, b, c):
    regs[c] = regs[a] * b

# Bitwise AND
def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
def bani(regs, a, b, c):
    regs[c] = regs[a] & b

# Bitwise OR
def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
def bori(regs, a, b, c):
    regs[c] = regs[a] | b

# Assignment
def setr(regs, a, b, c):
    regs[c] = regs[a]
def seti(regs, a, b, c):
    regs[c] = a

# Greater-than testing
def gtir(regs, a, b, c):
    if a > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

def gtri(regs, a, b, c):
    if regs[a] > b:
        regs[c] = 1
    else:
        regs[c] = 0
def gtrr(regs, a, b, c):
    if regs[a] > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

# Equality testing
def eqir(regs, a, b, c):
    if a == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0
def eqri(regs, a, b, c):
    if regs[a] == b:
        regs[c] = 1
    else:
        regs[c] = 0
def eqrr(regs, a, b, c):
    if regs[a] == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

op16 = {
'addr' : addr, 'addi': addi, 
'mulr' : mulr, 'muli': muli,
'banr' : banr, 'bani': bani, 'borr': borr, 'bori': bori, 
'setr' : setr, 'seti': seti, 
'gtir' : gtir, 'gtri': gtri, 'gtrr': gtrr, 
'eqir' : eqir, 'eqri': eqri, 'eqrr': eqrr}


def run(regs):
    ip = 0
    while True:
        regs[ipReg] = ip

        # execute instruction
        instr, a, b, c = prog[ip]
        op16[instr](regs, a, b, c)
        ip = regs[ipReg]
        ip += 1
        if ip < 0 or ip >= len(prog):
            break
    print(regs[0])

#run(list(regs))

regs[0] = 1
run(list(regs))
