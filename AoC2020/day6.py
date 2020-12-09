import string

def part1():
    with open("day6.txt") as f:
        data = f.read().split("\n")
        allgroups = []
        group = ""
        sum = 0
        for line in data:
            if line != "":
                group += line
            else:
                allgroups.append(group)
                group = ""

        for group in allgroups:
            sum += len(set(group))
        print(sum)

def part2():
    with open("day6.txt") as f:
        data = f.read().split("\n")
        allgroups = []
        group = []

        for line in data:
            if line != "":
                group.append(line)
            else:
                allgroups.append(group)
                group = []

        sum = 0
        allletters = set(string.ascii_lowercase)
        toRemove = []
        for group in allgroups:
            for person in group:
                for letter in allletters:
                    if letter not in person and letter not in toRemove:
                        toRemove.append(letter)
            for remove in toRemove:
                allletters.remove(remove)
            sum += len(allletters)
            toRemove = []
            allletters = set(string.ascii_lowercase)
            
        print(sum)
            

part1()
part2()
