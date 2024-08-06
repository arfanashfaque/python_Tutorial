matrix = [
    [1,0,2],
    [5,7,9],
    [3,4,6]
]
print(matrix[1][2])  # the output is 9 . 1 means 2nd row and 2 mean 3rd column
matrix[1][2] = 20
print(matrix[1][2]) # the output now changes from 9 to 20

for row in matrix:
    for column in row:
        print(column)
# to get all thing in a matrix
