import time

start_time = time.time()

def recurring_cycle_size(n):
    n = str(n)
    temp_list = []
    for x in xrange(len(n)):

        if n[x] in temp_list and list(n[x:x+(len(temp_list[temp_list.index(n[x]):]))])==temp_list[temp_list.index(n[x]):]:
            return len(temp_list[temp_list.index(n[x]):])
        temp_list.append(n[x])
        #print list(n[x:x+(len(temp_list[temp_list.index(n[x]):]))]), temp_list[temp_list.index(n[x]):]
    return 0

def unit_fraction(n):
    a = 10**10000/n
    return a

maximum, d = 0, 0
for x in xrange(1,1000):
    #print x, unit_fraction(x), recurring_cycle_size(unit_fraction(x))
    if recurring_cycle_size(unit_fraction(x))>maximum:
        maximum, d = recurring_cycle_size(unit_fraction(x)), x

print maximum, d

print 'completed in', time.time()-start_time, 'seconds'