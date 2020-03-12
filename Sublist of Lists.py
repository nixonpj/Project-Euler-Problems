def sublists(list1):
    list_of_sublists = []
    if len(list1)==1:
        list_of_sublists.append(list1)
        list_of_sublists.append([])
        return list_of_sublists
    else:
        list_of_sublists.append(list1)
        for i in xrange(len(list1)):
            temp = list1[0:i]+list1[i+1:]
            for item in sublists(temp):
                if item not in list_of_sublists:
                    list_of_sublists.append(item)
        return list(list_of_sublists)

#print len(sublists([1,1,3,4,5,6,9,8]))

def subsets(a):
    master_list = []
    subsets_helper_shorter(a, 0, [], master_list)
    return master_list

def subsets_helper(a, curr, answer, master_list):
    if curr >= len(a):
        master_list.append(answer)
    else:
        # first option in which you 'take'
        # a[curr]
        one = answer + [a[curr]]

        # second in which you don't
        two = answer

        subsets_helper(a, curr + 1, one, master_list)
        subsets_helper(a, curr + 1, two , master_list)

def subsets_helper_shorter(a, curr, answer, master_list):
    if curr >= len(a):
        master_list.append(answer)
    else:
        subsets_helper_shorter(a, curr + 1, answer, master_list)
        subsets_helper_shorter(a, curr + 1, answer + [a[curr]], master_list)

print subsets([1,2,3,4])
