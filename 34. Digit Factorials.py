import math, time

start_time = time.time()

list_of_values = {x:math.factorial(x) for x in xrange(10)}

print list_of_values

for x in xrange(3,1000000):
    x = str(x)
    total = 0
    for digit in x:
        total += list_of_values[int(digit)]
    if total == int(x):
        print x

print("--- %s seconds ---" % (time.time() - start_time))