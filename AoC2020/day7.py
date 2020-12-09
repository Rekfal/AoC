import re

class Bag:
    def __init__(self, color, rules, golden):
        self.color = color
        self.bags = []
        self.parents = []

        #list of tuples (ammount, color) or False(no rules)
        self.rules = rules

        self.golden = golden
        self.counted = False
        self.outer = True
        self.bagcount = 0
        self.inner = False
    
    def getCounted(self):
        return self.counted

    def getBagcount(self):
        return self.bagcount

    def setInner(self, inner):
        self.bagcount = 1
        self.inner = inner

    def getinner(self):
        return self.inner

    def setGolden(self, golden):
        self.golden = golden

    def addParent(self,parent):
        self.parents.append(parent)

    def setBags(self, newbags):
        self.bags = newbags

    def getOuter(self):
        return self.outer

    def setOuter(self, outer):
        self.outer = outer

    def getGolden(self):
        return self.golden

    def getBags(self):
        return self.bags

    def getRules(self):
        return self.rules

    def addBag(self, newbag):
        self.bags.append(newbag)

    def setAllGoldens(self):
        for parent in self.parents:
            parent.setGolden(self.golden)
            parent.setAllGoldens()

    def initBags(self):
        if self.inner:
            return

        for rule in self.rules:
            ammount = rule[0]
            color = rule[1]
            child = bagMap[color]
            if child.getinner():
                self.bagcount += ammount
                continue
            if child.getCounted() == False:
                child.initBags()
            self.bagcount += ammount * (child.getBagcount() + 1)
        self.counted = True



def checkRules(s):
    if re.search(r"no", s) != None:
        return False
    result = re.findall(r"(\d \w+ \w+)",line)
    rules = []
    for entry in result:
        temprule = entry.split(" ")
        rule = (int(temprule[0]),f"{temprule[1]} {temprule[2]}")
        rules.append(rule)
    return rules

with open("day7.txt") as f:
    data = f.read().split("\n")
    allBags = []
    bagMap = {}
    outerBags = []
    innerbags = []

    for line in data:
        golden = False
        result = re.search(r"(\w+ \w+)", line)
        color = result.group(0)
        rules = checkRules(line)
        if color == "shiny gold":
            golden = True
        newbag = Bag(color, rules, golden)
        allBags.append(newbag)
        bagMap[color] = newbag

    for bag in allBags:
        if bag.getRules() != False:
            for rule in bag.getRules():
                color = rule[1]
                newbag = bagMap[color]
                newbag.setOuter(False)
                bag.addBag(newbag)
                newbag.addParent(bag)
        else:
            bag.setInner(True)
            innerbags.append(bag)

    for bag in allBags:
        if bag.getOuter():
            outerBags.append(bag)

    for bag in allBags:
        if bag.getGolden():
            bag.setAllGoldens()

    #it counts itself
    sum = -1
    for bag in allBags:
        if bag.getGolden():
            sum += 1
    print(sum)

#unecessary for this day
#    for bag in outerBags:
#       bag.initBags()


    goldbag = bagMap["shiny gold"]
    goldbag.initBags()
    print(goldbag.getBagcount())