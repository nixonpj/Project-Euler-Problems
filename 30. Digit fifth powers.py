def f(n):
    sum = 0
    for x in str(n):
        sum+=int(x)**5
    return n==sum

answer = 0
for x in xrange(2,1000000):
    if f(x):
        answer+=x

print answer