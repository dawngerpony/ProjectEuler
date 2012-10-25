# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primeFactors(n):
    factors = []
    d = 2
    while(n > 1):
        while(n % d == 0):
            factors.append(d)
            n /= d
        d += 1
    return factors


def run():
    print max(primeFactors(600851475143))

if __name__=='__main__':
	run()
