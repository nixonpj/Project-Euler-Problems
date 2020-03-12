import random, math, time


def partition():
    kids = [x for x in xrange(90)]
    p1,p2,p3 = [], [], []
    for x in xrange(30):
        q = random.randrange(len(kids))
        p1.append(kids.pop(q))
    for x in xrange(30):
        q = random.randrange(len(kids))
        p2.append(kids.pop(q))
    if 1 in kids and 2 in kids:
        return True
    if 1 in p1 and 2 in p1:
        return True
    if 1 in p2 and 2 in p2:
        return True
    return False

def montecarlo(n):
    i=0
    for x in xrange(n):
        if partition():
            i+=1
    return i/float(n)

print montecarlo(100000)
print 29/89.0


