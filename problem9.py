# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.# 

def findPythagoreanTriplets(n):
	for c in range(1, n):
		for a in range(1, c):
			for b in range(1, a):
				if ((a*a) + (b*b) == (c*c)) and (a + b + c == 1000):
					return (a, b, c)
		print c

def run():
	a,b,c = findPythagoreanTriplets(1000)
	print "a=%d, b=%d, c=%d, abc=%d" % (a, b, c, a*b*c)


if __name__=='__main__':
	run()
