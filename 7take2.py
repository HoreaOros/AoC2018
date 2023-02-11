import copy
lines = open('7.in').read().strip().split('\n')

nodes = set()
outgoing = dict()
incoming = dict()

for line in lines:
    t = line.split(' ')
    nodeS = t[1] # source
    nodeT = t[7] # target
    nodes.add(nodeS)
    nodes.add(nodeT)
    if nodeS in outgoing:
        outgoing[nodeS].append(nodeT)
    else:
        outgoing[nodeS] = [nodeT]
    
    if nodeT in incoming:
        incoming[nodeT].append(nodeS)
    else:
        incoming[nodeT] = [nodeS]

for node in nodes:
    if not node in incoming:
        incoming[node] = []
    if not node in outgoing:
        outgoing[node] = []




def part1(incoming):
    L = []
    S = []
    # add al nodes with no incoming egdes to S
    for k, v in incoming.items():
        if v == []:
            S.append(k)
    # sort candidates
    S = list(sorted(S))
 
    while S:
        # remove nodes with no incoming edges from incoming
        for node in S:
            if node in incoming:
                incoming.pop(node)
        
        n = S.pop(0) # remove node from S
        L.append(n)  # add it to final list
        
        for k, v in incoming.items():
            if n in v:
                v.remove(n)
            if v == []:
                S.append(k)
        S = list(sorted(S))
    return L    
print('='*5 + 'Part 1' + '='*5)
L = part1(copy.deepcopy(incoming))
print(''.join(L))


def part2(incoming, cores, bias):
    L = []
    S = []
    seconds = 0
    workers = [0 for _ in range(cores)] # 0 means idle
    tasks = [None for _ in range(cores)]
    # add al nodes with no incoming egdes to S
    for k, v in incoming.items():
        if v == []:
            S.append(k)
    # sort candidates
    S = list(sorted(S))
 
    while S or incoming:
        # count idle workers
        idleWorkers = workers.count(0)
        
        

        for node in S:
            if node in incoming:
                incoming.pop(node)
                # idleWorkers -= 1
                # if idleWorkers == 0:
                #     break
        
        #schedule all tasks for which there are available workers
        for i in range(len(workers)):
            if workers[i] == 0:
                if S:
                    n = S.pop(0)
                    workers[i] = bias + ord(n) - ord('A') + 1
                    tasks[i] = n
                else:
                    break
        
        # let workers run until at least one finish
        finish = False
        done = []
        while True:
            seconds += 1
            for i in range(len(workers)):
                if workers[i] > 0:
                    workers[i] -= 1
                    if workers[i] == 0:
                        finish = True
                        done.append(tasks[i])
                        tasks[i] = None
            if finish:
                break



        done = list(sorted(done)) # can be multiple task that end simultaneously
        L = L + done # add it to final list
        
        for k, v in incoming.items():
            for n in done:
                if n in v:
                    v.remove(n)
                if v == []:
                    S.append(k)
        S = list(sorted(S))
    # if there are any unfinished task let them finish
    while any([w != 0 for w in workers]):
        seconds += 1
        for i in range(len(workers)):
            if workers[i] > 0:
                workers[i] -= 1
     
    return (seconds, L)



# cores = 2
# bias = 0
cores = 5
bias = 60
seconds, L = part2(copy.deepcopy(incoming), cores,  bias)

print('='*5 + 'Part 2' + '='*5)
print(f'Seconds to finish with {cores} workers: {seconds}')
print(''.join(L))


