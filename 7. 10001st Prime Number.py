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

#These are two ways of doing it that are typed below
def ith_prime(n):
    x = 2
    while len(prime_numbers)<=n:
        if isprime(x):
            prime_numbers.append(x)
        x+=1
    return prime_numbers[n-1]

def prime_number(n):
    x = 2
    i = 0
    while i<10001:
        if isprime(x):
            i+=1
        x+=1
    return x-1


#print ith_prime(10001)
print prime_number(10001)
print("--- %s seconds ---" % (time.time() - start_time))
