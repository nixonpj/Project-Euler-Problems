import time, itertools


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

list_of_primes = get_primes(10000)
list_of_4digit_primes = []
for prime in list_of_primes:
    if prime > 1000:
        list_of_4digit_primes.append(prime)
print (list_of_4digit_primes)

def check_permutations(n):
    lst = set([])
    for item in itertools.permutations(str(n)):
        temp_str = ''
        for digit in item:
            temp_str += digit
        if int(temp_str) in list_of_4digit_primes:
            lst.add(int(temp_str))
    if len(lst)>=3:
        temp_list = [list(sorted(lst))[i+1]- list(sorted(lst))[i] for i in xrange(len(lst)-1)]
        for item in temp_list:
            if temp_list.count(item)>1:
                return sorted(lst), temp_list
    return False

i = 0
for prime in list_of_4digit_primes:
    if check_permutations(prime):
        print check_permutations(prime)
        i+=1

print i

print 'time taken is', time.time()-start_time, 'seconds'
