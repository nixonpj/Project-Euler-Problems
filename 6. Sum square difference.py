import time

start_time = time.time()

def sum_of_squares(n):
    ans = 0
    for x in xrange(n+1):
        ans += x**2
    return ans

x = sum_of_squares(100)

def square_of_sums(n):
    ans = 0
    for x in xrange(n+1):
        ans += x
    return ans**2

y = square_of_sums(100)

print y - x

print 'completed in', time.time()-start_time, 'seconds'