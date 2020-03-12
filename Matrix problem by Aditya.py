import time

start_time = time.time()


def matrix_output(matrix):
    m, n, matrix = matrix_flip(matrix)
    list2=[[]]
    for row in matrix:
        for item in list2:
            list1=[]
            for number in row:
                temp = item+[number]
                list1.append(temp)
            list2 = list2+[item for item in list1]
    return [item for item in list2 if len(item)==(n)]


def matrix_flip(matrix):
    """Returns the transpose of the matrix"""
    m, n = len(matrix), len(matrix[0])
    list1 = []
    for col in range(n):
        list2 = []
        for row in range(m):
            list2.append(matrix[row][col])
        list1.append(list2)
    return m,n, list1



print matrix_output([[3,2,1,7],[6,1,4,9],[9,3,0,1]])

print 'time taken is', time.time() - start_time, 'seconds'