import time

start_time = time.time()

def factorial(n):
    ans = 1
    for x in xrange(n,1,-1):
        ans *= x
    return ans

s = factorial(100)
answer = 0
for x in str(s):
    answer += int(x)

print answer
print 'completed in', time.time()-start_time, 'seconds'