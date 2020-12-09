def part1():
    with open("day1.txt") as f:
        data = f.read().split("\n")
        data = [int(n) for n in data]
        data.sort()

        # the index of the first number larger than 1010
        #https://stackoverflow.com/questions/2236906/first-python-list-index-greater-than-x
        larger= next(x for x, val in enumerate(data) if val > 1010)
        found = False
        for i in range(larger):
            testNumber = data[i]
            for j in range(larger, len(data)):
                if testNumber + data[j] == 2020:
                    print(testNumber*data[j])
                    found = True
                    break
            if found:
                break


def part2():
    with open("day1.txt") as f:
        data = f.read().split("\n")
        data = [int(n) for n in data]
        data.sort()

    found = False
    for i in range(len(data)):
        a=data[i]
        if a >= 2020/3:
            break
        for j in range(i,len(data)):
            b = data[j]
            if a+b < 2020:
                for k in range(j,len(data)):
                    c = data[k]
                    if a+b+c == 2020:
                        print(a*b*c)
                        found = True
                        break
                    if found:
                        break
            if found:
                break
        if found:
            break
