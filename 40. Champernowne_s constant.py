import time, math

start_time = time.time()

def string(n):
    answer = '0'
    i = 1
    while len(answer)<n:
        answer+=str(i)
        i+=1
    return answer

big_string = string(2000000)

print len(big_string)
print int(big_string[1])*int(big_string[10])*int(big_string[100])*int(big_string[1000])*int(big_string[10000])*int(big_string[100000])*int(big_string[1000000])


print 'time taken is', time.time()-start_time, 'seconds'