import math
import time

start_time = time.time()
def get_primes(n):
    global numbers
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

list_of_primes = get_primes(20)
primes = {2: 0, 3: 0, 5: 0, 7: 0, 11:0, 13: 0, 17: 0, 19: 0}

def factorize(n, primes):
    ans = dict()
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i))
            ans[p]= i
    if n > 1:
        factors.append((n, 1))
        ans[n]=1
    return ans


for x in xrange(11,21):
    a = factorize(x, list_of_primes)
    for prime in primes:
        if prime in a:
            if a[prime]>primes[prime]:
                primes[prime] = a[prime]

answer = 1
for x in primes:
    answer*= x**primes[x]

print answer

print "Completed in", time.time() - start_time, 'seconds'