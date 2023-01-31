input = 236021

receipt = [3, 7]

elf1 = 0
elf2 = 1

for i in range(input + 10):
    if i % 1000 == 0:
        print(i)
    receipt = receipt + [ ord(c) - ord('0') for c in str(receipt[elf1] + receipt[elf2]) ]
    elf1 = (elf1 + 1 + receipt[elf1]) % len(receipt)
    elf2 = (elf2 + 1 + receipt[elf2]) % len(receipt)
    #print(receipt)
print(''.join(map(str,receipt[input:input + 10])))