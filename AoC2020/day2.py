def part1():
    with open("day2.txt") as file:
        data = file.read().split("\n")
        validcount = 0
        for entry in data:
            test = entry.split(" ")
            password = test[2]
            testletter = test[1][:-1]
            numbers = test[0].split("-")
            numbers = [int(n) for n in numbers]
            count = 0
            for letter in password:
                if letter == testletter:
                    count += 1
            if numbers[0] <= count and count <= numbers[1]:
                validcount += 1
        print(validcount)

def part2():
    with open("day2.txt") as file:
        data = file.read().split("\n")
        validcount = 0
        for entry in data:
            test = entry.split(" ")
            password = test[2]
            testletter = test[1][:-1]
            numbers = test[0].split("-")
            numbers = [int(n) for n in numbers]
            indexes = [n-1 for n in numbers]
            if testletter == password[indexes[0]] or testletter == password[indexes[1]]:
                if not (testletter == password[indexes[0]] and testletter == password[indexes[1]]):
                    validcount += 1

        print(validcount)
            

part1()

part2()