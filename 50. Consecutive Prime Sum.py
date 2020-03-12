import time

start_time = time.time()

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(1000000)
print len(primes)

answer_list = []
answer=0
for x in xrange(len(primes)-500):
    for y in xrange(550,500,-1):
        if sum(primes[x:y]) in primes and len(primes[x:y])>500:
            print sum(primes[x:y]), len(primes[x:y]), primes[x:(x+3)]
            break

print answer_list

print 'time taken is', time.time()-start_time , 'seconds'