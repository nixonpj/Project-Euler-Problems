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

print sum(get_primes(2000000))

print("--- %s seconds ---" % (time.time() - start_time))