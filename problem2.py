# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def ver1():
    '''
    1. Use plain old iteration to find all of the terms, breaking out at 4,000,000.
        Using Python's nifty "terms[-1]" array index to avoid the need for counters.
    2. Use list comprehension to filter the list by even numbers.
    3. Sum the list with sum().
    '''
    terms = [1, 2]
    while(terms[-1] < 4000000):
        terms.append(terms[-2] + terms[-1])
    
    evenTerms = [x for x in terms if (x % 2 == 0)]
    print evenTerms
    print sum(evenTerms)

if __name__=='__main__':
    ver1()
