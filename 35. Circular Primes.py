import math, time, itertools

start_time = time.time()

def combinations(n):
    """
    returns all different combinations of a number as needed by this question
    """
    temp_list = [x for x in str(n)]
    answer = []
    for x in itertools.permutations(temp_list,len(temp_list)):
        answer.append(x)
    new_answer = []
    for y in answer:
        temp_str = ''
        for z in y:
            temp_str+=z
        new_answer.append(int(temp_str))
    return new_answer

print combinations(1)

def get_primes(n):
    global numbers
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(1000000)

def check_combs(n):
    all_combs = combinations(n)
    for comb in all_combs:
        print comb
        if comb not in primes:
            print comb, 'no'
            return False
    return True

print check_combs(197)

