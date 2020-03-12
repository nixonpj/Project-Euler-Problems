import time, math

start_time = time.time()

def valid_number(n, m):
    """This function returns True if there are no repeated digits in
    the multiples of this number. n is the number and m is the number
     of multiples to be checked. Eg: 4591 returns True but 4588 returns False"""
    for multiple in xrange(2,m+1):
        if len(str(n))!=len(str(m*n)):
            return False
    for digit in str(n):
        for multiple in xrange(2,m+1):
            if digit not in str(multiple*n):
                return False
    return True

def valid_multiples(n):
    """This function checks each number to see if its valid multiple.
    Remember only numbers starting in 1 can be an asnwer since the multiple of 6 otherwise
    would result in an increase in no. of digits."""
    i=100000
    while i<n:
        if valid_number(i,6):
            print i,2*i,3*i,4*i,5*i,6*i
            break
        i+=1


valid_multiples(1000000)

print 'time taken is', time.time() - start_time, 'seconds'