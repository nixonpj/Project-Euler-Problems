import time

start_time = time.time()

ans = dict()
def collatz_sequence1(n):
    if n in ans:
        return ans[n]
    y=n
    i=1
    temp_list = []
    while n!=1:
        if n in ans:
            ans[y]=i+ans[n]
            i = i+ ans[n] - 1
            break
        if n%2==0:   n=n/2
        else:        n=(3*n)+1
        i+=1
        temp_list.append(n)
    ans[y]= i
    for item in temp_list:
        ans[item]= i - temp_list.index(item)-1
    return i

maximum, answer= 0, 0
for x in xrange(1000000,1,-1):
    if collatz_sequence1(x)>maximum:
        maximum, answer = collatz_sequence1(x), x

print answer, maximum

print 'completed in', time.time() - start_time, 'seconds'