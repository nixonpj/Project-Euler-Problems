import time, math

start_time = time.time()

def is_prime(n):
    if n%2==0:
        return False
    if n%3==0:
        return False
    a = 5
    while a<=(n/a):
        if n%a==0:
            return False
        a+=2
    return True

#print is_prime(982451653)


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


#print isprime(982451653)

s = 0
for x in xrange(4,1299827):
    if isprime(x):
        s+=1
print s

print 'time taken is', time.time()-start_time, 'seconds'