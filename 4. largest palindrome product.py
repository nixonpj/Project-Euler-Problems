import math
import time
#print 999*999
#print 100*100

start_time = time.time()
def check_palindrome(n):
    x = str(n)
    for i in xrange(len(x)/2):
        if x[i]!=x[-1-i]:
            return False
    return True


def check_divisor(n):
    for x in xrange(100,999):
        if n%x==0 and len(str(n/x))==3:
            print x, n, n/x
            return True
    return False


def proc():
    for x in range(998001, 10000, -1):
        if check_palindrome(x):
            if check_divisor(x):
                return x

print proc()

print("--- %s seconds ---" % (time.time() - start_time))


