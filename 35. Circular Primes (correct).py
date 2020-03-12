import time, math

start_time = time.time()

def circular(number):
    number = str(number)
    list_of_numbers = []
    for idx in xrange(len(number)):
        number = number[1:]+number[0]
        list_of_numbers.append(int(number))
    return list_of_numbers

def get_primes(n):
    global numbers
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(100000)
#print circular(197)

def circular_primes(n):
    for every_number in circular(n):
        if every_number not in primes:
            return False
    return True

#print circular_primes(1997)

print len(filter(circular_primes ,primes))

print "time taken is:", time.time()-start_time