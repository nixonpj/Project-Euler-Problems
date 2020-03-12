import time

start_time = time.time()

f = open("13. large Sum.txt", "r")

nums = f.readlines(50)

sum = 0
for number in nums:
    sum+=int(number[:11])

print str(sum)[:10]

print 'completed in', time.time() - start_time, 'seconds'