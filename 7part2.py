from Scheduler import Scheduler
lines = open('7.in').read().strip().split('\n')
g = dict()
for line in lines:
    t = line.split(' ')
    if t[7] in g:
        g[t[7]].append(t[1])
    else:
        g[t[7]] = [t[1]]


alphabet = [chr(ord('A') + i) for i in range(26)]
for lit in alphabet:
    if lit not in g.keys():
        g[lit] = []

for k in g:
    print(k, g[k])

sch = Scheduler(5)

result = ''
while len(g) > 0:
    cand = ''
    for k in g:
        if g[k] == []:
            cand += k
    cand = ''.join(sorted(cand))
    
    # schimbam lista de joburi care asteapta
    sch.ClearJobs()
    for c in cand:
        sch.AddJob(c)
    sch.Schedule()
    

    result += cand[0]
    toRemove = cand[0]
    g.pop(toRemove)
    for k in g:
        if toRemove in g[k]:
            g[k].remove(toRemove)
                
    
print(sch.Time)

