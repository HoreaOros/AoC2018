def part1():
    input = 236021

    receipt = [3, 7]

    elf1 = 0
    elf2 = 1

    for i in range(input + 10):
        # if i % 1000 == 0:
        #     print(i)
        receipt = receipt + [ ord(c) - ord('0') for c in str(receipt[elf1] + receipt[elf2]) ]
        elf1 = (elf1 + 1 + receipt[elf1]) % len(receipt)
        elf2 = (elf2 + 1 + receipt[elf2]) % len(receipt)
        #print(receipt)
    print(''.join(map(str,receipt[input:input + 10])))

part1()

def part2():
    input = '236021'
 
    receipt = [0 for i in range(25_000_000)]
    receipt[0] = 3
    receipt[1] = 7
    N = 2

    elf1 = 0
    elf2 = 1
    i = 0
    while True:
        # i += 1
        # if i % 100_000 == 0:
        #     print(i)
        
        newDigits = [ ord(c) - ord('0') for c in str(receipt[elf1] + receipt[elf2]) ]
        for d in newDigits:
            receipt[N] = d
            N += 1 
        elf1 = (elf1 + 1 + receipt[elf1]) % N
        elf2 = (elf2 + 1 + receipt[elf2]) % N

        
        a = ''.join(map(str,receipt[N-len(input):N]))
        b = ''.join(map(str,receipt[N-len(input) - 1:N-1])) 
        if a == input:
            print(N - len(input))
        elif b == input:
            print(N - len(input) - 1)
        else:
            continue
        break
            
part2()