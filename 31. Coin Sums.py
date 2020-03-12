from itertools import product

for y, x in product(range(3), repeat=2):
  print 'yes'
  for y1, x1 in product(range(2), repeat=2):
    print 'no'
answers = []
for x in xrange(0,3):
    for y in xrange(0,5):
        for z in xrange(0, 11):
            if (100*x + 50*y + 20*z)==200:
                answers.append((x,y,z))

print answers

list = [200,100,50,20,10,5,2,1]
