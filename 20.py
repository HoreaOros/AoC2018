input = open('20.ex').read().strip()[1:-1]


lst = []
def f(s):
    if not '|' in s:
        lst.append(s)
    else:
        try:
            idx1 = s.index('(')
        except:
            idx1 = len(s)
        prefix = s[:idx1]
        #print(prefix)
        
        s = s[idx1:]

        #print(s)

        tokens = []
        p = 0
        buf = ''
        for i, c in enumerate(s):
            if c == '(':
                p += 1
                if p > 1:
                    buf += c
            elif c == ')':
                p -= 1
                if p > 0:
                    buf += c
                else:
                    break
            elif c == '|':
                if p == 1:
                    tokens.append(buf)
                    buf = ''
                else:
                    buf += c
            else:
                buf += c
        tokens.append(buf)

        #print(tokens)
        s = s[i + 1:]
        #print(s)

        for t in tokens:
            f(prefix + t + s)




f(input)
print(len(lst))
lst = list(sorted(lst, key = lambda arg: len(arg)))
print(lst)
print(len(max(lst, key = lambda arg: len(arg))))
