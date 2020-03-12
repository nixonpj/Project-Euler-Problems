import time, math

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

list_of_primes = get_primes(1000000)

def truncate(n):
    list_of_numbers = []
    n = str(n)
    for x in xrange(len(n)-1):
        if (int(n[x+1:])) not in list_of_primes or (int(n[:x+1])) not in list_of_primes:
            return False
    return True

total = []

for prime in list_of_primes:
    if truncate(prime):
        print prime
        total.append(prime)

print total
print 'time taken is', time.time()-start_time, 'seconds'