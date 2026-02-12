import numpy as np

print(dir(np))

# Arrays
# N-Dimensional arrays
#* ndarray will give n dimensional array or matrices which will fill random values
#* array will give 2 dimensional matrices.
# 1D array
x = np.ndarray((5))
print(x)
# 1D array with matrix(row, col)
x1 = np.ndarray([3,5])
print(x1)
# ND array with matrix(dim, row, col)
x2 = np.ndarray([5, 2, 3])
print(x2)
# Index
x2[1][1][1]


# Array
emp = np.array([[1, 22, 44], [2, 33, 66], [ 3, 44, 88]])
print(emp)
# Index
emp[1][1]
emp[0, 2] # - [row, col]
print(emp[:, 2])
# Transpose
emp.T
# Arithmetic Operations
print(emp.mean())
print(emp.max())
print(emp.sum())
# Shape and Size
print(emp.shape)
print(emp.size)
