import itertools

with open("day9.txt") as f:
    data = f.read().split("\n")
    data = [int(x) for x in data]
    target = 0

    #part1
    for i in range(25,len(data)):
        #do we find 2 numbers in the preamble that sum up to the current number
        found = False
        startofpreamble = i-25
        preamble = data[startofpreamble:i]
        current = data[i]
        for numbers in itertools.combinations(preamble,2):
            if sum(numbers) == current:
                found = True
                break
        if not found:
            target = current
            print(target)

    #part2
    sum = 0
    startindex = 0
    contiguous = []
    started = False
    i = 0

    while True:
        if not started:
            current = data[startindex]
            contiguous.append(current)
            started = True
        else:
            current = data[i]
            contiguous.append(current)
        if sum + current > target:
            contiguous = []
            startindex += 1
            i = startindex
            sum = 0
            started = False
            continue
        sum += current
        i += 1
        if sum == target and len(contiguous) >= 2:
            print(min(contiguous)+max(contiguous))
            break

    #28289238 too high