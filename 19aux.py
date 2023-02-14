C =  10551418 #10550400

d = 1
A = 0
while d * d < C:
    if C % d == 0:
        A = A + d + C // d
    d += 1
if d * d == C:
    A = A + d
print(A)