lines = open("1.in").read().split("\n")
nums=[int(line) for line in lines]
print(nums)
print(sum(nums))

value = 0
SEEN = set()
SEEN.add(value)

i = 0
N = len(nums)

while True:
    value = value + nums[i]
    print(value, end = '')
    print(' ', end = '')
    if not value in SEEN:
        SEEN.add(value)
    else:
        print(value)
        break
    i = (i + 1) % N