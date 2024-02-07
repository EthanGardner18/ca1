# Ethan Gardner
# CS 456
# Coding Assignment CA1
# Modification 1: 1
# Modification 2: 4

#imports here
import math #example only
import argparse
import os
# functions and remaining code here

EMPTY = '-'
POLICEMAN = 'P'
THIEF = 'T'
ROOKIE = 'R'


def solve_PCT(grid,k):
    position1 = findPoliceOfficer(grid)
    catchDistance(grid,position1,k)


def print_Matrix(grid): # Prints the current Grid
    for row in grid:
        print(" ".join(row))
    print()

def catchColumn(grid, posy): # Checks to see if there is a theif in the same column, if caught update the theifs position to empty
    for row in range(len(grid)):
        if grid[row][posy] == THIEF:
            print("Caught Theif")
            grid[row][posy] = EMPTY
            return True
    return False    

def catchDistance(grid, position, k):  # this function will catch the thief if they are within K units away
    px, py = position
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == THIEF:
                distance = abs(px - i) + abs(py - j) 
                if distance <= k:
                    print("Caught Thief")
                    grid[i][j] = EMPTY
                    return i,j 


def findPoliceOfficer(grid): # return the position in the matrix of the police officer then set it to empty
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == POLICEMAN:
                grid[i][j] = EMPTY
                return i,j
    

    

def main():
    grid = [
        ['-', 'P','-','T'],
        ['-', '-','P','-'],
        ['P', 'T','-','-'],
        ['-', '-','P','-']
    ]
    k = 2
    print_Matrix(grid)
    solve_PCT(grid, k)
    print_Matrix(grid)

if __name__ == "__main__":
    main()