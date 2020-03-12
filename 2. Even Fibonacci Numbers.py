import time
start_time = time.time()



fibonacci_series = [1,2]
def fib(n):
    while fibonacci_series[-1]+fibonacci_series[-2]<n:
        fibonacci_series.append(fibonacci_series[-2]+fibonacci_series[-1])
    return fibonacci_series

fib(4000001)
ans = 0
for x in fibonacci_series:
    if x%2==0:
        ans+=x


print ans
print("--- %s seconds ---" % (time.time() - start_time))