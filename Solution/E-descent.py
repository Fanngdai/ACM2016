# E - Permutation Descent Counts
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

import sys

def permutation(N,v):
    index = N * 101 + v;
    if v==0 or v==N-1:
        mem[index]=1
    if index not in mem:
        mem[index] = ((v+1) * permutation(N-1,v) + (N-v) * permutation(N-1, v-1)) % 1001113
    return mem[index]

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
    print("", end="")
else:
    for i in range(1, amt+1):
        # position (space) value (space) value
        val = file.readline().split()

        if len(val) > 3:
            print("Extra values were entered!")
            exit()
        elif len(val) < 3:
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

        N = val[1]
        v = val[2]
        if N.isnumeric() and v.isnumeric():
            N = int(N)
            v = int(v)
        else:
            print("Values must be integer!")
            exit()

        if N < 2 or N > 100 or v < 0 or v > N-1:
            print("Make sure that 2 <= N <= 100 and 0 <= v <= N-1")
            exit()

        mem = {}
        print(str(position) + " " + str(permutation(N , v)))
        
    file.close()
