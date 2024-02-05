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


def solve_PCT(grid):
    position = findPoliceOfficer(grid)
    catchColumn(grid,position)


def print_Matrix(grid):
    for row in grid:
        print(" ".join(row))
    print()

def catchColumn(grid, position):
    posx,posy = position

    for row in range(len(grid)):
        if grid[row][posy] == THIEF:
            print("Caught Theif")
            grid[row][posy] = EMPTY
            return True
    return False    

def catchDistance():
    #this function will catch the theif if they are within K units away
    pass

def findPoliceOfficer(grid): # return the position in the matrix of the police officer then set it to empty
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == POLICEMAN:
                grid[i][j] = EMPTY
                return i,j
    

    

def main():
    grid = [
        ['-', 'P','-','T'],
        ['-', '-','p','-'],
        ['p', 't','-','-'],
        ['-', '-','p','-']
    ]

    print_Matrix(grid)
    solve_PCT(grid)
    print_Matrix(grid)


if __name__ == "__main__":
    main()