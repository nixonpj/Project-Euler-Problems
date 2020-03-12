import math, time

start_time = time.time()

all_numbers = set(x for x in xrange(28124))

def sum_of_divisors(n):
    divisors_list = set()
    for x in xrange(1,int(math.sqrt(n)+1)):
        if n%x==0:
            divisors_list.add(x)
            divisors_list.add(n/x)
    ans=0
    for x in divisors_list:
        ans+=x
    return ans-n

abundant_numbers = []
for x in all_numbers.copy():
    if sum_of_divisors(x)>x:
        abundant_numbers.append(x)
        all_numbers.difference_update(set(range(x*2, len(all_numbers), x)))

print len(all_numbers)
print abundant_numbers

for x in abundant_numbers:
    for y in abundant_numbers[abundant_numbers.index(x):]:
        if x+y in all_numbers:
            all_numbers.remove(x+y)

print sum(all_numbers)

print 'completed in', time.time()-start_time, 'seconds'



