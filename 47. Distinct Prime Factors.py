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

prime_nos = get_primes(1000000)

def get_prime_factors(n):
    i = 0
    temp = set([])
    while i<100000:
        if n == 1:
            return temp
        if n%prime_nos[i]==0:
            n = n/prime_nos[i]
            temp.add(prime_nos[i])
        else:
            i+=1

print (get_prime_factors(37960))
print (get_prime_factors(37961))
print (get_prime_factors(37962))

i = 1
while i<1000000:
    if len(get_prime_factors(i))==4 and len(get_prime_factors(i+1))==4 and len(get_prime_factors(i+2))==4 and len(get_prime_factors(i+3))==4:
        print i
        break
    i+=1


print 'time taken is', time.time() - start_time, 'seconds'
