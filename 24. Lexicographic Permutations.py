import itertools, time

start_time = time.time()

numbers = [0,1,2,3,4,5,6,7,8,9]

print list(itertools.permutations(numbers))[999999]
#print len(list(itertools.permutations(numbers)))
print 'completed in', time.time() - start_time, 'seconds'