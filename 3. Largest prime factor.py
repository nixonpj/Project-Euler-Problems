import math
def find_divisors(n):
    divisors = set()
    for x in xrange(1,int(math.sqrt(n))+1):
        if n%x==0:
            divisors.add(x)
            divisors.add(n/x)
    return divisors

a = find_divisors(600851475143)

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

ans = [x for x in a if isprime(x)]

print max(ans)

print isprime(2801)

