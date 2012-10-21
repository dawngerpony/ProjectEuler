# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def ver1():
    '''
    1. Create lists of the two numbers using built-in range() function.
    2. Use built-in set() to produce unordered sets of each of the lists.
    3. Union the two sets with the "|" operator.
    4. Sum the new set with in-built function sum().
    '''
    print sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5)))

def ver2():
    '''
    An optimisation I found on the forum (so I take no credit for it).
    '''
    print sum(set(range(0, 1000, 3) + range(0, 1000, 5)))
    
ver1()
