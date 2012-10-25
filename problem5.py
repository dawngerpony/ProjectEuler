# Problem 5

# "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

# This took a long time to execute. 

def dividesBy(n):
    numbers = range(1, n+1)
    numbers.reverse()
    # print numbers
    i = 0
    looking = True
    while(looking):
        looking = False
        i += n
        print i
        for x in numbers:
            if(i % x != 0):
                looking = True
                break
    return i

def run():
    print "Answer = %i " % dividesBy(19)

if __name__=='__main__':
    run()
