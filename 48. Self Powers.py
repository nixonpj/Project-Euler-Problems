import time, math

start_time = time.time()

total = 0

for x in xrange(1,1001):
    total+= x**x

print str(total)[-10:]

print 1.0/(1+math.e**100)
print 1.0/(1+math.e**-100)
print 'time taken is', time.time()-start_time, 'seconds'