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

def isprime(n):
    """Returns True if n is prime"""
    if n<2: return False
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

list_of_b = get_primes(1000)
temp_list = []
for item in list_of_b:
    temp_list.append(-item)

max_n, max_a, max_b = 0,0,0
ans = ()

for b in list_of_b:
    for a in xrange(-1001,1000,2):
        n = 0
        while isprime((n**2) + (a*n) + b):
            n+=1
        if n > max_n:
            max_n, max_a, max_b = n, a, b
            ans = (max_n, max_a, max_b)

print max_a, max_b, max_n, ans
print max_a*max_b
print 'completed in', time.time()- start_time, 'seconds'





