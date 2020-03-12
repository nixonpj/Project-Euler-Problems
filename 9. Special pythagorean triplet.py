import math, time

start_time = time.time()

#ans = {x: x**2for x in xrange(100)}
#print ans

for x in range(1,501,2):
    for y in range(1,501):
        if x+y+(math.sqrt(x**2+y**2))==1000:
            print x, y, math.sqrt(x**2+y**2)
            print x*y*math.sqrt(x**2+y**2)

print 'completed in', time.time()-start_time, 'seconds'