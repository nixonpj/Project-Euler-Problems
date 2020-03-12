import math, time

start_time = time.time()

list_of_powers = {x:2**x for x in xrange(21)}
print list_of_powers

def decimal_to_binary(n):
    answer = ''
    for x in list_of_powers:
        if n/list_of_powers[x]==1:
            answer+='1'
            n=n%list_of_powers[x]
            break
    for idx in xrange(x-1,-1,-1):
        if n/list_of_powers[idx]==1:
            answer+='1'
            n=n%list_of_powers[idx]
        else:
            answer+='0'
    return answer


def check_palindrome(n):
    if str(n)!=str(n)[::-1]:
        return False
    if decimal_to_binary(n)!=decimal_to_binary(n)[::-1]:
        return False
    return True


total1 = 0
for idy in xrange(1000000):
    if check_palindrome(idy):
        total1 += idy
print total1
print "time taken is:", time.time()-start_time, "seconds"