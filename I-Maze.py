# ACM GNYR 2016 - I - Amazing
# Interactive maze solver.
# Does not use dfs.  Does not use recursion.

import sys

try:
    file = open(sys.argv[1])
except IOError:
    print("Unable to open the file")
    exit()

# Get the first number
try:
    amt = int(file.readline())
    if amt<1 or amt>10000:
        print("Value must be between 1 and 10,000 inclusive!")
        exit()
except ValueError:
    print("Please enter an integer!", end="")
else:
    for i in range(1,amt+1):
        # position (space) value
        val = file.readline().split()
