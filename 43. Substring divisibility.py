import time, math, itertools

start_time = time.time()

def pandigital_numbers():
    '''returns a list of pandigital numbers'''
    list_of_pandigital_nos = []
    for y in itertools.permutations([idx for idx in xrange(10)],10):
        temp = ''
        for digit in y:
            temp+=str(digit)
        list_of_pandigital_nos.append(int(temp))
    return list_of_pandigital_nos

pans = pandigital_numbers()
print len(pans)

def divisibility(n):
    '''Returns True if the number satisfies the problems divisibility conditions'''
    if int(str(n)[1:4])%2!=0 or int(str(n)[2:5])%3!=0:
        return False
    if int(str(n)[3:6])%5!=0 or int(str(n)[4:7])%7!=0:
        return False
    if int(str(n)[5:8])%11!=0 or int(str(n)[6:9])%13!=0:
        return False
    if int(str(n)[7:10])%17!=0:
        return False
    return True

print sum(filter(divisibility, pans))
q = 1647283951

#print 1406357289 in pans
#print str(q)[1:4]

print 'time taken is', time.time()-start_time, 'seconds'

