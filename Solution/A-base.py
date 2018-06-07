# A - Which base is it anyway?
# Solution by Fanng Dai
# ACM GNYR 2016

# Makes sure that all chars in value is valid
def checker(value, base):
    possibleValue = list(range(base))

    # Make sure it can be converted
    for ch in value:
        if int(ch) not in possibleValue:
            return False
    return True

def convertToBase10(value, base):
    lst = list(value)
    sum = 0
    for i in range(len(value)):
        val = int(lst.pop())
        sum += base**i * val
    return sum

# Get the first number
try:
    amt = int(input())
    if amt<1 or amt>10000:
        print("Value must be between 1 and 10,000 inclusive!")
        exit()
except ValueError:
    print("", end="")
else:
    for i in range(1,amt+1):
        # position (space) value
        val = input()
        val = val.split()

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
        value = val[1]

        if not value.isnumeric() or len(value)>7:
            print("Value not accepted!")
            exit()

        # For this problem, the octal value is the only one that presents
        # us with an issue.
        # If the input value is "9", sscanf does not touch the octal value.
        # If the input is 19, the octal value will be 1 and this is wrong.
        # So, we have to validate the octal one by hand.
        # We  go through character by character and build up the value until
        # we hit the end of string ('\0') or we get a bad digit.
        print(str(i) + " ", end='')
        if checker(value, 8):
            print(str(convertToBase10(value, 8)), end='')
        else:
            print("0", end='')

        print(" "+ str(int(value)) + " " + str(convertToBase10(value, 16)))
