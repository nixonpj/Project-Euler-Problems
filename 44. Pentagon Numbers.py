import time, math

start_time = time.time()

pent_numbers = [n*(3*n - 1)/2 for n in xrange(1,10000)]
print len(pent_numbers)

for pent1 in pent_numbers:
    for pent2 in pent_numbers[pent_numbers.index(pent1)+1:]:
        if pent2-pent1 in pent_numbers:
            if pent1+pent2 in pent_numbers:
                print pent2, pent1


print 'time taken is', time.time()-start_time, 'seconds'