# D - Tight-Fit Sudoku
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

import math
import copy
import sys

def sudoku(position):
    Board = []
    for i in range(6):
        Board.append(list(map(lambda x : x.replace("/", " ").split(), file.readline().split())))
        if len(Board[-1]) != 6:
            print("Incorrect Format")
            exit()

    inrow = [set(map(str, range(1, 10))) for _ in range(6)]
    incol = [set(map(str, range(1, 10))) for _ in range(6)]
    insqr = [set(map(str, range(1, 10))) for _ in range(6)]

    def ri(r, c):
        return math.floor(math.floor(r/2)*2+c/3)

    left = {}

    dash = 0
    for r, row in enumerate(Board):
        for c, cell in enumerate(list(row)):
            for v in cell:
                if v != '-':
                    inrow[r].remove(v)
                    incol[c].remove(v)
                    insqr[ri(r,c)].remove(v)
                else:
                    dash += 1

    options = {}
    for r, row in enumerate(Board):
        for c, cell in enumerate(list(row)):
            for i, v in enumerate(list(cell)):
                if v == '-':
                    options[(r, c, i)] = inrow[r] & incol[c] & insqr[ri(r,c)]

    def printBoard():
        print(position)
        for row in Board:
            for cell in row:
                if len(cell) == 2:
                    print ("%s/%s" % (cell[0], cell[1]), end=" ")
                else:
                    print (cell[0], end=" ")
            print()     # new line

    def solveSudoku(dash):
        if dash == 0:
            printBoard()
            return True

        picks = []
        for (r, c, i), ch in options.items():
            if Board[r][c][i] == '-':
                picks.append((len(ch), r, c, i, ch))

        picks.sort()

        l, r, c, i, left = picks[0]
        for k in left:
            cell = Board[r][c]
            cell[i] = k

            # check x/y x < y condition
            if len(cell)==2 and cell[1-i]!='-' and cell[0]>cell[1]:
                cell[i] = '-'
                continue

            undo = []
            for (r0, c0, i0), ch in options.items():
                if Board[r0][c0][i0] == '-' and (r0 == r or c0 == c or ri(r, c) == ri(r0, c0)):
                    if k in options[(r0, c0, i0)]:
                        undo.append((r0, c0, i0))

            for u in undo:
                options[u].discard(k)

            if solveSudoku(dash-1):
                return True

            cell[i] = '-'
            for u in undo:
                options[u].add(k)

        return False
    solveSudoku(dash)

try:
    file = open(sys.argv[1])
except IOError:
    print("Unable to open the file")
    exit()

try:
    amt = int(file.readline())
    if amt<1 or amt>100:
        print("Value must be between 1 and 1,000 inclusive!")
        exit()
except ValueError:
    print("Please enter an integer!", end="")
else:
    for i in range(1, amt+1):
        position = file.readline().split()
        position = position[0]

        # Make sure a number is inserted
        if position.isnumeric():
            position = int(position)
        else:
            print("Wrong problem value " + position + " for instance " + str(i) + "\n", end='')
            exit()

        # wrong position
        if position != i:
            print("Wrong problem number " + str(position) + " for instance " + str(i) + "\n", end='')
            exit()

        sudoku(position)
