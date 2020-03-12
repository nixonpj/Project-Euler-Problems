import math, time

start_time = time.time()

list_of_triangular_numbers = dict()

#the triangular number function is unnecessary after i used the x plus y method to make the program faster
def triangular_number(n):
    sum = 0
    for x in xrange(n+1):
        sum+=x
        list_of_triangular_numbers[x] = sum
    return sum

def find_divisors(n):
    divisors = set()
    for x in xrange(1,int(math.sqrt(n))+1):
        if n%x==0:
            divisors.add(x)
            divisors.add(n/x)
    return divisors

def proc(n):
    x, y = 1, 0
    while True:
        if len(find_divisors(x+y))>n:return triangular_number(x), x, len(find_divisors(x+y))
        y = x+y
        x+=1

print proc(500)

print 'completed in', time.time()-start_time, 'seconds'

