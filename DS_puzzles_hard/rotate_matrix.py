'''
Rotate n*n matrix
clock wise
90 degree
matrix is list(list(int))
'''

# create a matrix
# using python list

'''
Create a matrix
matrix = []
n = 3
for i in range(n):
    row = []
    sum = 0
    for j in range(3):
        sum = sum +1
        row.append(sum)
    matrix.append(row)
'''

matrix = [[0,1,2],
          [3,4,5],
          [6,7,8]]

# swap func in python
def swap(i,j):
    i, j = j, i

    return i , j


