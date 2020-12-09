import math
import numpy as np

def part1(data):
    highest = 0
    for seat in data:
        minrow = 0
        maxrow = 127
        mincol = 0
        maxcol = 7
        for letter in seat:
            if letter == "B":
                minrow = minrow + math.ceil(((maxrow - minrow)/2))
            if letter == "F":
                maxrow = maxrow - math.ceil(((maxrow - minrow)/2))
            if letter == "R":
                mincol = mincol + math.ceil(((maxcol-mincol)/2))
            if letter == "L":
                maxcol = maxcol - math.ceil(((maxcol - mincol)/2))
        id = minrow*8 + mincol
        if id > highest:
            highest = id
    print(highest)

def part2(data):
    grid = np.zeros((128,8))
    for seat in data:
        minrow = 0
        maxrow = 127
        mincol = 0
        maxcol = 7
        for letter in seat:
            if letter == "B":
                minrow = minrow + math.ceil(((maxrow - minrow)/2))
            if letter == "F":
                maxrow = maxrow - math.ceil(((maxrow - minrow)/2))
            if letter == "R":
                mincol = mincol + math.ceil(((maxcol-mincol)/2))
            if letter == "L":
                maxcol = maxcol - math.ceil(((maxcol - mincol)/2))
        grid[minrow,mincol] = 1

    for row in range(9,len(grid)-9):
        for col in range(8):
            seat = grid[row][col]
            if seat == 0:
                print(row*8+col)

with open("day5.txt") as f:
    data = f.read().split("\n")
#    part1(data)
    part2(data)
