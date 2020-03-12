import time, math, csv

start_time = time.time()

f = open("42. triangle words.txt", "r")
words = f.readlines()[0].split(',')

list_of_words = []
list_of_names_num_value = []
list_of_name_scores = []

for word in words:
    ''' This process is to isolate the name by removing the quotes '''
    word = word[1:-1]
    list_of_words.append(word)

print (list_of_words)

for name in list_of_words:
    '''it finds the sum of the alphabetical ordinals and saves it in a new list'''
    alphabetical_value = 0
    for alphabet in name:
        alphabetical_value += ord(alphabet)-64
    list_of_names_num_value.append(alphabetical_value)

print (list_of_names_num_value)

triangle_numbers = [n*(n+1)/2 for n in xrange(21)]

total = 0
for value in list_of_names_num_value:
    if value in triangle_numbers:
        total+=1

print total

print 'time taken is', time.time() - start_time, 'seconds'
