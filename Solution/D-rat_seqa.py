# D - Rational Sequence
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

import math
import sys

def getNodes(value):
    i = value
    lst = []
    while i > 1:
        lst.append(i)
        i = math.ceil((i-1)/2)
    return lst

try:
    file = open(sys.argv[1])
except IOError:
    print("Unable to open the file")
    exit()

try:
    amt = int(file.readline())
    if amt<1 or amt>1000:
        print("Value must be between 1 and 1,000 inclusive!")
        exit()
except ValueError:
    print("Please enter an integer!", end="")
else:
    for i in range(1, amt+1):
        # position (space) value (space) value
        val = file.readline().split()

        if len(val) > 2:
            print("Extra value(s) were entered!")
            exit()
        elif len(val) < 2:
            print("Missing values!")
            exit()

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

        n = val[1]
        if n.isnumeric():
            n = int(n)
        else:
            print("Value must be integer!")
            exit()

        if n < 1 or n > 2147483647:
            print("Value must be 1 <= value <= 2,147,483,647")
            exit()

        path = getNodes(n)
        n = 1       # numerator
        d = 1       # denominator
        while path:
            val = path.pop()
            # right child
            if val%2==0:
                d = n + d
            else:
                n = n + d

        print(str(position) + " " + str(n) + "/" + str(d))
        
    file.close()
