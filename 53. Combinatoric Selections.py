import time, math

start_time = time.time()

def combination(n,r):
    """Function return nCr(combinations) possible."""
    return math.factorial(n)/(math.factorial(n-r) * math.factorial(r))

def million_comb(n):
    """Returns the lists of distinct nCr combinations that have a value
    of above 1,000,000"""
    answer = 0
    i=23
    list_of_r = xrange(i)

    while i<=n:
        for x in :
            if combination(i,x)>1000000:
                answer+=1
        i+=1
    return len(answer)


#print combination(23,10)
print million_comb(1000)

print 'time taken is', time.time() - start_time, 'seconds'