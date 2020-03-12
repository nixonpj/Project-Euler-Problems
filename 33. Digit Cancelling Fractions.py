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

def valid_fractions():
    valid_fractions_list = []
    for x in range(10,100):
        for y in range(x+1,100):
            if x%10==0 and y%10==0:
                continue
            #if isprime(x)==True or isprime(y)==True:
            #    continue
            digits_x = []
            for digit_x in str(x):
                digits_x.append(digit_x)
            for digit_y in str(y):
                if digit_y in digits_x:
                    valid_fractions_list.append([x,y])
    return valid_fractions_list


fractions_list = valid_fractions()
print fractions_list

def strip_fraction(fraction):
    value = float(fraction[0])/fraction[1]
    digits_num = [x for x in str(fraction[0])]
    digits_den = [y for y in str(fraction[1])]
    for item_num in digits_num:
        if item_num in digits_den:
            digits_num.remove(item_num)
            digits_den.remove(item_num)
    if digits_den[0] == '0':
        return False
    new_value = float(digits_num[0])/float(digits_den[0])
    if value == new_value:
        return True
    return False

print strip_fraction([10,70])

for fraction in fractions_list:
    if strip_fraction(fraction):
        print fraction



