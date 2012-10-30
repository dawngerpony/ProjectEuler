# problem10.py

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math

def isPrime(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if(x % 2 == 0):
		return False
	isPrime = True
	for y in range(3, int(math.sqrt(x))+1, 2):
		if(x % y == 0):
			isPrime = False
			break
	return isPrime

def sumOfPrimes(n):
	sum = 2
	for i in range(3, n, 2):
		if isPrime(i):
			sum += i
			print i
	print sum

def findPrimes(n):
	for i in range(n):
		if isPrime(i):
			print "%d (is prime)" % i

def run():
	# findPrimes(100)
	sumOfPrimes(2000000)


if __name__=='__main__':
	run()
