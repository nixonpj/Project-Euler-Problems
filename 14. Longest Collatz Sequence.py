import time

start_time = time.time()

def collatz_sequence(n):
    collatz_sequence=[n]
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=(3*n)+1
        collatz_sequence.append(n)
    return len(collatz_sequence)

answer = dict()
def collatz_sequence1(n):
    y = n
    i=0
    while n!=1:
        if n in answer:
            answer[y]=i+answer[n]
            return i+answer[n]
        if n%2==0:   n=n/2
        else:        n=(3*n)+1
        i+=1
    answer[y]= i+1

    return i


maximum, ans= 0, 0
for x in xrange(1000000,500000,-1):
    if collatz_sequence1(x)>maximum:
        maximum, ans = collatz_sequence1(x), x

print ans, maximum

print 'completed in', time.time() - start_time, 'seconds'

