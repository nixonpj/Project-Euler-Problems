import time

start_time = time.time()

list_of_fibonacci_numbers = []

i, j = 1, 1
while len(str(j))<1000:
    list_of_fibonacci_numbers.append(i)
    list_of_fibonacci_numbers.append(j)
    i+=j
    j+=i

print len(list_of_fibonacci_numbers)+2