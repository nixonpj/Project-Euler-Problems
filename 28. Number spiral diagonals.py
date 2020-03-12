import time
start_time = time.time()

def spiral(n):
    a = 1
    i = 2
    temp_list = [1]
    while a<n:
        for x in xrange(4):
            a+=i
            temp_list.append(a)
        i+=2
    return temp_list

print sum(spiral(1002001))

print 'completed in', time.time() - start_time, 'seconds'
