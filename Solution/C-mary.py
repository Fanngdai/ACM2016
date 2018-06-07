# C - M-ary Partitions
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

# m is the power
# n is the value (list)
# Doesn't work fully
def partition2(m, firstVal, max):
    lst = []
    power = []
    for i in range(1,firstVal):
        if(m**i>=firstVal):
            break
        else:
            power.append(m**i)

    for i in reversed(power):
        while firstVal>=i:
            lst.append(i)
            firstVal-=i
    return lst

# RecursionError
def partition(power, result, index, lst, target):
    if target == 0:
        result.append(list(lst))
    while index < len(power) and power[index] <= target:
        lst.append(power[index])
        partition(power, result, index, lst, target - power[index])
        lst.pop()
        index += 1

# works
def coin(power, target):
    ans = [0]*(target+1)
    ans[0]=1
    for n in power:
        for i in range(1, target+1):
            if i >= n:
                ans[i] += ans[i - n]
    return ans[target];

try:
    amt = int(input())
    if amt<1 or amt>1000:
        print("Value must be between 1 and 1,000 inclusive!")
        exit()
except ValueError:
    print("", end="")
else:
    for i in range(1, amt+1):
        # position (space) value (space) value
        val = input().split()

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

        pow = val[1]
        target = val[2]
        if pow.isnumeric() and target.isnumeric():
            target = int(target)
            pow = int(pow)
        else:
            print("Values must be integer!")
            exit()

        if pow < 3 or pow > 100 or target < 3 or target > 10000:
            print("Make sure that 3 <= m <= 100 and 3 <= n <= 10,000")
            exit()

        power = list(filter(lambda x: x<=target, [ pow**i for i in range(target)]))
        result = []
        # partition(power, result, 0, [], target)
        print(str(position) + " " + str(coin(power, target)))
        # print(str(position) + " " + str(len(result)))

        # lst = [1] * target
        # while len(lst) >= pow:
        #     for j in range(pow):
        #         lst.pop(0)
        # print(target-len(lst))

        # # For when removing all 1's.
        # count = 1
        # lst = [target]
        # # list not empty
        # while lst:
        #     print(lst)
        #     fVal = lst.pop(0)
        #     lst = lst + partition(pow, fVal, target)
        #     filter(lambda x: x!=1, lst)
        #     count+=1
        # print(str(position) + " " + str(len(alreadyHave)+1))
