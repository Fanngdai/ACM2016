# G - Magic Knights Tour
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

MAGIC_SUM = 260     # ((64*(64+1))/2)/8
# char fixedx[66]
fixedx = []
fixedy = []
test = 0
remsum = []

movex = [1, 2, 2, 1, -1, -2, -2, -1]
movey = [-2, -1, 1, 2, 2, 1, -1, -2]

class BOARD(object):
    pass

def checkSums(level):
    global boards
    global remsum

    for i in range(8):
        # print(len(boards))
        # print(len(boards[level].rowfree))
        # print(len(remsum))
        # print(remsum[boards[level].rowfree[i]])
        if (MAGIC_SUM - boards[level].rowsum[i]) > remsum[boards[level].rowfree[i]]:
            # this row can not possibly get up to MAGIC_SUM
            return -1
        if MAGIC_SUM - boards[level].colsum[i] > remsum[boards[level].colfree[i]]:
            # this col can not possibly get up to MAGIC_SUM
            return -2
        if (boards[level].rowsum[i] + boards[level].rowfree[i]*boards[level].curmove) > MAGIC_SUM:
            # this row sum is guaranteed to be larger than MAGIC_SUM
            return -3
        if (boards[level].colsum[i] + boards[level].colfree[i]*boards[level].curmove) > MAGIC_SUM:
            # this row sum is guaranteed to be larger than MAGIC_SUM
            return -4
    return 0

# 1
# 1
# 1 48 -1 -1 33 -1 63 18
# 30 51 -1 3 -1 -1 -1 -1
# -1 -1 -1 -1 15 -1 -1 -1
# -1 -1 -1 45 -1 -1 36 -1
# -1 -1 25 -1 9 -1 21 60
# -1 -1 -1 -1 24 57 12 -1
# -1 6 -1 -1 39 -1 -1 -1
# 54 -1 42 -1 -1 -1 -1 -1

def solveBoard(level):
    global boards
    global maxlevel

    ret = -1
    curmove = boards[level].curmove

    if checkSums(level) != 0:
        return ret
    if level > maxlevel:
        maxlevel = maxlevel
    if curmove == 64:
        return level
    elif curmove == 63:
        test+=1

    for move in range(8):
        newx = boards[level].curx + movex[move]
        newy = boards[level].cury + movey[move]
        if (newx<0) or (newx>=8) or (newy<0) or (newy>=8):
            continue
        if boards[level].board[newy][newx]>=0:
            continue


        if fixedx[curmove+2]>=0:
            found = 0
            for nextmove in range(8):
                if ((newx+movex[nextmove]) == fixedx[curmove+2]) and ((newy+movey[nextmove]) == fixedy[curmove+2]):
                    print(level)
                    found = 1
                    break
            if found == 0:
                continue

        nextlevel = level+1
        nextmove = curmove+1
        boards[nextlevel] = boards[level]
        boards[nextlevel].board[newy][newx] = curmove+1
        boards[nextlevel].rowfree[newy]-=1
        boards[nextlevel].colfree[newx]-=1
        boards[nextlevel].colsum[newx] += curmove+1
        boards[nextlevel].rowsum[newy] += curmove+1
        boards[nextlevel].curx = newx
        boards[nextlevel].cury = newy
        boards[nextlevel].curmove = nextmove

        while fixedx[nextmove+1]>=0:
            nextmove+=1
            boards[nextlevel+1] = boards[nextlevel]
            # print(boards[nextlevel+1])
            boards[nextlevel+1].curx = fixedx[nextmove]
            boards[nextlevel+1].cury = fixedy[nextmove]
            boards[nextlevel+1].curmove = nextmove
            nextlevel+=1

        ret = solveBoard(nextlevel)
        return ret if ret >= 0 else -1

def is_digit(n, i, index):
    try:
        int(n)
    except ValueError:
        print("Read failed on row " + str(i) + " of problem " + str(index))
        exit()



# main
try:
    amt = int(input())
    if amt<1 or amt>10000:
        print("Value must be between 1 and 10,000 inclusive!")
        exit()
except ValueError:
    print("Please enter an integer!", end="")
else:
    boards = [BOARD() for _ in range(64)]

    for index in range(1, amt+1):
        # position (space) value (space) value
        position = input().split().pop(0)

        if position.isnumeric():
            position = int(position)
        else:
            print("Wrong problem value " + position + " for instance " + str(index) + "\n", end='')
            exit()

		# wrong position
        if position != index:
            print("Wrong problem number " + str(position) + " for instance " + str(index) + "\n", end='')
            exit()

        boards[0].rowsum = []
        boards[0].colsum = []
        boards[0].rowfree = []
        boards[0].colfree = []
        boards[0].board = [[0 for x in range(8)] for y in range(8)]

        for i in range(8):
            boards[0].rowsum.append(0)
            boards[0].colsum.append(0)
            boards[0].rowfree.append(8)
            boards[0].colfree.append(8)

        for i in range(65):
            fixedx.append(-1)
            fixedy.append(-1)

        # read region data
        for i in range(8):
            stdin = input().split()
            vals = stdin
            if len(stdin) != 8:
                print("Read failed on row " + str(i) + " of problem " + str(index))
                exit()

            # Make sure passed in values are numbers
            for j in range(8):
                is_digit(vals[j], i, index)
                val = vals[j] = int(vals[j])
                if val != -1 and ((val < 1) or val > 64):
                    print("Val at " + str(i) + ", " + str(j) + " = " + str(val) + " is out of range problem " + str(index))
                    exit()

                # Put into board
                boards[0].board[i][j] = val
                if val > 0:
                    boards[0].rowsum[i] += int(val)
                    boards[0].colsum[j] += int(val)
                    boards[0].rowfree[i] -= 1
                    boards[0].colfree[j] -= 1
                    fixedx[val] = int(j)
                    fixedy[val] = int(i)

        remsum.append(0)
        sum = 0
        j = 1
        for i in range (64, 0, -1):
            if j > 8:
                break
            fixedx[i] = int(fixedx[i])
            if fixedx[i] < 0:
                sum += i
                remsum.append(sum)
                j+=1

        if fixedx[1] >= 0 and fixedy[1] >= 0:
            i = 1
            while fixedx[i] >= 0 and fixedy[i] >= 0:
                boards[0].curx = fixedx[i]
                boards[0].cury = fixedy[i]
                boards[0].curmove = i
                i+=1
        else:
            print("Problem " + str(index) + " move 1 is not given")
            exit()

        maxlevel = 0
        ret = solveBoard(0)
        if ret >= 0:
            print(index)
            for i in range(8):
                for j in range(8):
                    print(boards[ret].board[i][j])
                print()     # new line
        else:
            print("No solution for problem " + str(index) + " maxlevel " + str(maxlevel))
