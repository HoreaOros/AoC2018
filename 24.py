import copy
import re
class Group:
    def __init__(self, groupType, units, hitpoints, intiative, damage, damageType, immune, weak):
        self.GroupType = groupType
        self.Units = units
        self.HitPoints = hitpoints
        self.Initiative = intiative
        self.Damage = damage
        self.DamageType = damageType
        self.Immune = immune
        self.Weak = weak
        self.AttackedBy = None
        self.Attacking = None
    def EffectivePower(self):
        return self.Units * self.Damage
    def isAlive(self):
        return self.Units > 0
    def DamageTo(self, a):
        damage = self.EffectivePower()
        if self.DamageType in a.Immune:
            damage = 0
        elif self.DamageType in a.Weak:
            damage *= 2
        return damage

class Army:
    def __init__(self):
        self.Groups = []
    def isAlive(self):
        for g in self.Groups:
            if g.isAlive():
                return True
        return False
    def TotalUnits(self):
        suma = 0
        for g in self.Groups:
            if g.Units > 0:
                suma += g.Units
        return suma

lines = open('24.in').read().strip().split('\n')

immSystem = Army()
infection = Army()


def getGroup(line, groupType):
    reg = r'(\d+) units each with (\d+) hit points (\(.+\) )?with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)'
    m = re.search(reg, line)
    
    units = int(m.group(1))
    hitpoints = int(m.group(2))
    wi = m.group(3)
    damage = int(m.group(4))
    damageType = m.group(5)
    initiative = int(m.group(6))
    weakness = []
    immuness = []
    if wi != None:
        wi = wi[1:-2]
        t = wi.split('; ')
        p = re.split(r',? ', t[0])
        if p[0] == 'weak':
            weakness = p[2:]
        else:
            immuness = p[2:]
        if len(t) == 2:
            p = re.split(r',? ', t[1])
            if p[0] == 'weak':
                weakness = p[2:]
            else:
                immuness = p[2:]

    return Group(groupType, units, hitpoints, initiative, damage, damageType, immuness, weakness)


#N = 2
N = 10
for i in range(1, N + 1):
    immSystem.Groups.append(getGroup(lines[i], 'ImmuneSystem'))
for i in range(N + 3, 2 * N + 3):
    infection.Groups.append(getGroup(lines[i], 'Infection'))


pass

def acquireTarget(u, army):
    target = None
    maxDamage = -1
    for a in army.Groups:
        if a.AttackedBy == None and a.Units > 0:
            damage = u.DamageTo(a)
            if damage == 0:
                continue
            if damage > maxDamage:
                maxDamage = damage
                target = a
            elif damage == maxDamage:
                if a.EffectivePower() > target.EffectivePower():
                    target = a
                elif a.EffectivePower() == target.EffectivePower():
                    if a.Initiative > target.Initiative:
                        target = a
    return target



def part1(boost, immSystem, infection):
    immSystem = copy.deepcopy(immSystem)
    for g in immSystem.Groups:
        g.Damage += boost
    while immSystem.isAlive() and infection.isAlive():
       
        # Target selection
        # create list of alive units ordered decreasingly by effective power
        units = []
        for g in immSystem.Groups:
            if g.isAlive():
                units.append(g)
        for g in infection.Groups:
            if g.isAlive():
                units.append(g)
        units = sorted(units, key = lambda arg: (-arg.EffectivePower(), -arg.Initiative))


        for u in units:
            if u.GroupType == 'ImmuneSystem':
                u.Attacking = acquireTarget(u, infection)
            else:
                u.Attacking = acquireTarget(u, immSystem)
            if u.Attacking != None:
                u.Attacking.AttackedBy = u
        

        # Attacking in decreasing order of initiative
        units = sorted(units, key = lambda arg: -arg.Initiative)
        for u in units:
            if immSystem.isAlive() and infection.isAlive():
                if u.Units > 0 and u.Attacking != None:
                    damage = u.DamageTo(u.Attacking)
                    u.Attacking.Units -= damage // u.Attacking.HitPoints

        #reset Attacking and AttackeBy
        for g in immSystem.Groups:
            g.AttackedBy = None
            g.Attacking = None
        for g in infection.Groups:
            g.AttackedBy = None
            g.Attacking = None

    if immSystem.isAlive():
        return ('ImmuneSystem', immSystem.TotalUnits())
    else:
        return ('Infection', infection.TotalUnits())

print(part1(0, immSystem, infection)[1])

boost = 0
while True:
    winning, unitsLeft = part1(boost, immSystem, infection)
    if winning == 'ImmuneSystem':
        print(unitsLeft, immSystem, infection)
        break
    boost += 1



