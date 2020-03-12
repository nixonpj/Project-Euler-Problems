import time, math

start_time = time.time()

def is_prime(n):
    """returns True if a number is prime"""
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def check_conjecture():
    """loops through all odd numbers skipping every prime number. Creates a
    list b with all probable values of x-2y^2 giving us a list which should have atleast
    one prime number. If we dont get a prime in list return that number"""
    for x in xrange(3,1000000,2):
        if is_prime(x):
            continue
        b = [x-(2*(y**2)) for y in xrange(1,int(math.ceil(math.sqrt(x))))]
        if not filter(is_prime, b):
            print 'yes'
            return x


print check_conjecture()

print 'time taken is', time.time() - start_time, 'seconds'