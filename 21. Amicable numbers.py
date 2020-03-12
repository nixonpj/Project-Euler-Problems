import math, time

start_time = time.time()

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

list_of_amicable_numbers=[]

for x in xrange(10000):
    a = sum_of_divisors(x)
    if sum_of_divisors(a)==x and a!=x and a not in list_of_amicable_numbers:
        list_of_amicable_numbers.append(x)
        list_of_amicable_numbers.append(a)

print list_of_amicable_numbers

ans=0

for x in list_of_amicable_numbers:
    ans+=x

print ans
print 'completed in', time.time()-start_time, 'seconds'