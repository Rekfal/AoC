def run(data, fix):
    accumulator = 0
    index = 0
    indexes = set()
    while True:
        line = data[index]
        if line == "":
            continue
        parsed = line.split(" ")
        command = parsed[0]
        ammount = int(parsed[1])
        if index == fix and fix != False:
            if command == "nop":
                command = "jmp"
            else:
                command = "nop"

        if command == "acc":
            accumulator += ammount
            index += 1
        if command == "jmp":
            index += ammount
        if command == "nop":
            index += 1
        
        if index in indexes:
            #part1
            if fix == False:
                print(accumulator)
            break
        indexes.add(index)

        #part 2
        if index == len(data) - 1:
            print(accumulator)
            break


with open("day8.txt") as f:
    data = f.read().split("\n")
    indexes = []
    run(data, False)

    for i in range(len(data)):
        line = data[i]
        if line == "":
            continue
        parsed = line.split(" ")
        command = parsed[0]
        ammount = int(parsed[1])
        if command == "jmp" or command=="nop":
            indexes.append(i)

    for i in indexes:
        run(data, i)