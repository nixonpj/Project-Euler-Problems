import time, math

start_time = time.time()

list1 = [n*(n+1)/2 for n in xrange(285,100000)]


for number in list1:
    m = (1+math.sqrt(1+(24*number)))/6
    q = (1+math.sqrt(1+(8*number)))/4
    if m%1==0 and q%1==0:
        print list1.index(number)+285, m, q, number

print 'time taken is', time.time()-start_time, 'seconds'