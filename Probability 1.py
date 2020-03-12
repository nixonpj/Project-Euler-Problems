import math, time, random

DECK = [1,2,3,4,5,6,7,8,9,10,11,12,13,
       1,2,3,4,5,6,7,8,9,10,11,12,13,
       1,2,3,4,5,6,7,8,9,10,11,12,13,
       1,2,3,4,5,6,7,8,9,10,11,12,13]

#This program runs simulations to find the odds of getting a King(or anything else) on the thirteenth draw.
sorted(DECK)
def montecarlo():
    lst = []
    for x in xrange(13):
        q = DECK.pop(random.randrange(len(DECK)))
        lst.append(q)
    for item in lst:
        DECK.append(item)
    return lst[12]

i = 0
for x in xrange(100000):
    if montecarlo() == 1:
        i+=1
print i/100000.0