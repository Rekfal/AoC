def countTrees(down, right, grid):
    treecount = 0
    currentRight = 0
    currentDown = 0
    maxdown = len(grid) - 1
    maxright = len(grid[0]) - 1
    while currentDown <= maxdown:
        line = grid[currentDown]
        if currentRight > maxright:
            currentRight = currentRight - maxright - 1
        if line[currentRight] == "#":
            treecount += 1
        currentRight += right
        currentDown += down
    return treecount

with open("day3.txt") as file:
    grid = file.read().split("\n")
    print(countTrees(1, 3, grid)) #part1
    
    r1 = countTrees(1,1, grid)
    r2 = countTrees(1,3, grid)
    r3 = countTrees(1,5, grid)
    r4 = countTrees(1,7, grid)
    r5 = countTrees(2,1, grid)
    print(r1*r2*r3*r4*r5) #part2 