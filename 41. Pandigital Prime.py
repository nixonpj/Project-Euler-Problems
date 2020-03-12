import math, time, itertools


start_time = time.time()

def pandigital_numbers():
    list_of_pandigital_nos = []
    for x in xrange(7,6,-1):
        for y in itertools.permutations([idx for idx in xrange(1,x+1)],x):
            temp = ''
            for digit in y:
                temp+=str(digit)
            list_of_pandigital_nos.append(int(temp))
    return list_of_pandigital_nos

pans = pandigital_numbers()
print len(pans)

def isprime(n):
    """Returns True if n is prime"""
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

print max(filter(isprime, pans))
print "time taken is", time.time()-start_time, 'seconds'
