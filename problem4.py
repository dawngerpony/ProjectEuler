# Problem 4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    '''
    Uses the funky Python [::-1] notation to determine whether a string
    is equal to the reverse of the string, i.e. is a palindrome."
    '''
    if(str(n) == str(n)[::-1]):
        return True
    else:
        return False

def findLargestPalindrome():
    '''
    Finds the largest palindrome from a list of factors:
    1. Create a set of tuples containing all combinations of the elements in the list.
    2. Create a list containing the product of all the tuples.
    3. Sort/reverse the list so the highest number comes first (an optimization)).
    4. Return the highest number that matches the qualification of being a palindrome.
    '''
    numbers = range(10, 100)
    tuples = []
    for x in numbers:
        tuples += [[x,y] for y in numbers]
    products = [x*y for x,y in tuples]
    products.sort()
    products.reverse()
    for x in products:
        if(isPalindrome(x)):
            return x


def run():
    print findLargestPalindrome()

if __name__=='__main__':
    run()
