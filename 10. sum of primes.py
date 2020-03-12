import time

start_time = time.time()

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

prime_numbers = []
ans = 0


def sum_of_primes(n):
    ans = 0
    for x in xrange(2,n):
        if isprime(x):
            ans += x
            #prime_numbers.append(x)
    return ans

print sum_of_primes(2000000)

print'completed in', time.time()-start_time, 'seconds'