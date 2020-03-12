import time

start_time = time.time()

f = open("22. Names scores.txt", "r")

names = f.readlines()[0].split(',')

list_of_names = []
list_of_names_num_value = []
list_of_name_scores = []

for name in names:
    ''' This process is to isolate the name by removing the quotes '''
    name = name[1:-1]
    list_of_names.append(name)

#print list_of_names
list_of_names.sort()
'''this sorts the whole list alphabetically'''
#print list_of_names

for name in list_of_names:
    '''it finds the sum of the alphabetical ordinals and saves it in a new list'''
    alphabetical_value = 0
    for alphabet in name:
        alphabetical_value += ord(alphabet)-64
    list_of_names_num_value.append(alphabetical_value)

#print list_of_names_num_value

i=1
for num_value in list_of_names_num_value:
    name_score = num_value*i
    list_of_name_scores.append(name_score)
    i+=1

print sum(list_of_name_scores)

print 'completed in', time.time()-start_time, 'seconds'

