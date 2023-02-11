import re
class NanoBot:
    def __init__(self, x, y, z, r):
        self.X = x
        self.Y = y
        self.Z = z
        self.R = r
    def DistanceTo(self, bot):
        return abs(self.X - bot.X) + abs(self.Y - bot.Y) + abs(self.Z - bot.Z) 
    def __str__(self):
        return f'pos = <{self.X, self.Y, self.Z}>, range = {self.R}'
lines = open('23.in').read().strip().split('\n')
bots = []
for line in lines:
    nums = re.findall(r'-?\d+', line)
    bots.append(NanoBot(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])))

maxRangeBot = max(bots, key = lambda arg: arg.R)

print(len(list(filter(lambda arg: arg.DistanceTo(maxRangeBot) <= maxRangeBot.R, bots))))
