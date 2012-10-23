# problem7.py

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def isPrime(x):
	isPrime = True
	for y in range(2, x/2):
		# print "y = %d " % y
		if(x % y == 0):
			isPrime = False
			break
	return isPrime

def findPrime(n):
	if(n == 1):
		return 2
	i = 1
	candidate = 1
	while(i < n):
		if(isPrime(candidate) == True):
			lastPrime = candidate
			print "%d = %d" % (i, lastPrime)
			if(i == n):
				break
			else:
				i += 1
		candidate += 2
	return lastPrime

findPrime(10002)
