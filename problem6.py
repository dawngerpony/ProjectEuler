# Problem 6

# NB. The proper formatting of the equations is messed up in ASCII, and should be checked on the website:
# http://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquaresIterative(n):
	sum = 0
	for x in range(1, n+1):
		sum += x*x
	return sum

def squareOfSumsIterative(n):
	sum = 0
	for x in range(1, n+1):
		sum += x
	return sum*sum

def difference(n):
	sumofSquares = sumOfSquaresIterative(n)
	squareOfSums = squareOfSumsIterative(n)
	print "%d: %d - %d = %d" % (n, squareOfSums, sumofSquares, (squareOfSums - sumofSquares))

difference(10)
difference(100)
