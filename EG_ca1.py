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

EMPTY = 'R'
POLICEMAN = 'P'
THIEF = 'T'

def solve_PCT(grid, k):
    numCaught = 0
    position = findPoliceOfficer(grid) # finds the first police officer
    
    while True:
        posx, posy = position # find police officer position
        if catchColumn(grid, position): # check column, if he can catch a theif increment number of caught theives
            numCaught += 1
        elif catchDistance(grid, position, k): # if not found in column check to see if the thief is within a k distance away
            numCaught += 1
        else:
            print("Police Officer: (" + str(posx) + ", " + str(posy) + ") did not catch any thieves") # if the police officer couldn't catch a thief print that
        position = findPoliceOfficer(grid) # find a new policeman
        if position == (-1, -1): # if we are out of possible police officers print the number caught and break
            print("There were " + str(numCaught) + " theives caught")
            break


def print_Matrix(grid): # Prints the current Grid
    for row in grid:
        print(" ".join(row))
    print()

def catchColumn(grid, position): # Checks to see if there is a theif in the same column, if caught update the theifs position to empty
    posx,posy = position
    for row in range(len(grid)):
        if grid[row][posy] == THIEF: # checks to see if the policeman is in the same column as the theif
            grid[row][posy] = EMPTY # if true make the theif caught and and print
            print("Police Officer at (" + str(posx) + ", " + str(posy) + ") caught the theif at (" + str(row) + ", " + str(posy) + ")") 
            return True
    return False    

def catchDistance(grid, position, k):  # this function will catch the thief if they are within K units away
    posx, posy = position
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == THIEF: #checks to see if the policeman can see if the theif is in the same row
                distance = abs(posx - i) + abs(posy - j) # find distance from police officer
                if distance <= k: # if they are within catching distance set theif to caught and print
                    grid[i][j] = EMPTY
                    print("Police Officer at (" + str(posx) + ", " + str(posy) + ") caught the theif at (" + str(i) + ", " + str(j) + ")")
                    return True 
    return False

def findPoliceOfficer(grid): # return the position in the matrix of the police officer then set it to empty
    
    for i in range(len(grid)):
        for j in range(len(grid)): # finds the first policeman and then sets up to taken
            if grid[i][j] == POLICEMAN:
                grid[i][j] = EMPTY
                return i,j
    return -1,-1
    
def main(grid,k):
    print(grid)
    solve_PCT(grid, k) # solves the number of theives

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process grid and unit information.')
    parser.add_argument('grid', type=str, nargs='+')
    parser.add_argument('units', type=int)
    args = parser.parse_args()
    
    grid = [list(row) for row in args.grid]
    k = args.units
    
# when running the scipt it must be in the format python EG_ca1.py 'PRTP' 'TPRP' 'RTTP' 'PPRT' 2
# note the matrix must be NxN and the k values is at the end, when inputing the matrix the format must be as followed

    main(grid,k)