import math

def isprime(n):
    """Returns True if n is prime"""
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
      if n % i == 0:
         return False
      i += w
      w = 6 - w
    return True


def check_duplicate(n):
    """
    Checks if the number has 0 or any digits repeated.
    If not it returns True
    """
    abc=''
    for item in n:
        abc+=str(item)
    digits = []
    for individual_digit in abc:
        if individual_digit in digits or individual_digit=='0':
            return False
        digits.append(individual_digit)
    return True

def proc(n):
    numbers = []
    for number in xrange(1,n):
        if check_duplicate([number]):
            numbers.append(number)
    return numbers

list_of_products = proc(10000)
#print list_of_products
answers = []
for product in list_of_products:
    for divisor in xrange(1,int(math.sqrt(product))+1):
        if product%divisor==0:
            if len(str(product)+str(divisor)+str(product/divisor))==9:
                if check_duplicate([product,divisor,product/divisor]):
                    answers.append((divisor,product/divisor,product))

print len(answers), answers
ans = set()
for x in answers:
    ans.add(x[2])
print sum(ans)