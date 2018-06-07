# B - FBI Control Numbers
# Solution by Fanng Dai
# ACM ICPC GNYR 2016

# Compute the sum in base 27
def compute(value):
	factor = [2, 4, 5, 7, 8, 10, 11, 13]
	alphaLookup = ['0','1','2','3','4','5','6','7','8','9','A','C','D','E','F','H','J','K','L','M','N','P','R','T','V','W','X']
	sum = 0
	for ch in value:
		if ch == 'B':
			sum += factor.pop(0) * alphaLookup.index('8')
		elif ch == 'G':
			sum += factor.pop(0) * alphaLookup.index('C')
		elif ch == 'I':
			sum += factor.pop(0) * alphaLookup.index('1')
		elif ch == 'O' or ch == 'Q':
			sum += factor.pop(0) * alphaLookup.index('0')
		elif ch == 'S':
			sum += factor.pop(0) * alphaLookup.index('5')
		elif ch == 'U' or ch == 'Y':
			sum += factor.pop(0) * alphaLookup.index('V')
		elif ch == 'Z':
			sum += factor.pop(0) * alphaLookup.index('2')
		elif ch in alphaLookup:
			sum += factor.pop(0) * alphaLookup.index(ch)
		else:
			print("Value entered is not correct!")
			exit()
	return sum

def convert(value):
	alphaLookup = ['0','1','2','3','4','5','6','7','8','9','A','C','D','E','F','H','J','K','L','M','N','P','R','T','V','W','X']
	lst = list(value)
	sum = 0
	for i in range(len(lst)):
		val = alphaLookup.index(lst.pop())
		sum += 27**i * val
	return sum

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
			print("Missing values!")
			exit()

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

		if len(value) != 9:
			print("Value must contain 9 characters!")
			exit()

		alphaLookup = ['0','1','2','3','4','5','6','7','8','9','A','C','D','E','F','H','J','K','L','M','N','P','R','T','V','W','X']
		base27 = compute(value[:-1])
		if base27%27 == alphaLookup.index(value[-1]):
			print(str(position) + " " + str(convert(value[:-1])))
		else:
			print(str(position) + " Invalid")
