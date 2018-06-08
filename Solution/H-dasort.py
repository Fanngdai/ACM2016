# H - DA-Sort
# Solution by Fred Pickel
# ACM ICPC GNYR 2016

import sys
import math

def sort_ed(a):
    s = a[:]
    s = sorted(a)
    if a == s:
        return True
    return False

def sort(lst):
    counter = 0

    while(not sort_ed(lst)):
        m = max(lst)
        lst.remove(m)
        counter+=1

    return counter

try:
    file = open(sys.argv[1])
except IOError:
    print("Unable to open the file")
    exit()

# Get the first number
try:
    amt = int(file.readline())
    if amt<1 or amt>100:
        print("Value must be between 1 and 100 inclusive!")
        exit()
except ValueError:
    print("Please enter an integer!", end="")
else:
    for i in range(1,amt+1):
        # position (space) value
        val = file.readline().split()

        if len(val) > 2:
            print("Extra values were entered!")
            exit()
        elif len(val) <= 1:
            val.append('0')

        # Get problem number; first thing on line
        position = val[0]
        if position.isnumeric():
            position = int(position)
        else:
            print("Wrong problem value " + position + " for instance " + str(i) + "\n", end='')
            exit()

        # wrong position
        if position != i:
            print("Wrong problem number " + str(position) + " for instance " + str(i) + "\n", end='')
            exit()

        # Skip to first space; basically, skipping over problem number
        amtNum = val[1]

        if not amtNum.isnumeric():
            print("Value not accepted!")
            exit()

        amtNum = int(amtNum)
        if amtNum < 1 or amtNum > 1000:
            print("Value must be 1 <= N <= 1,000")
            exit()

        loopTimes = math.ceil(amtNum/10)
        numbers = []
        for j in range(loopTimes):
            line = file.readline().split()
            numbers.extend(line)

        numbers = list(map(int, numbers))
        print(str(position) + " " + str(sort(numbers)))

    file.close()
