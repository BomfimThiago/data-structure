# Arrays 2D são matrizes 
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos
print(array_2d[0][1])

# initialize an array 2D in python 
# not indicated tough because each matrix has the same reference
rows, cols = (5, 5)

arr = [[0] * cols] * rows

print(arr)

# or we can do 
arr2 = [[0 for i in range(cols)] for j in range(rows)]
print(arr2)


# transpose a matrix
# in the same matrix
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

n = len(matrix)
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)

# generating another matrix
n = len(matrix)
matrix_transposed = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        matrix_transposed[i][j] = matrix[i][j]

print(matrix_transposed)


# for matrix 3D the best would be use numpy, actually all matrix problems should be solved with numpy
# so list numpy commands here ...