import numpy as np

#Shape -The example returns (2, 4), which means that the array has 2 dimensions,
# where the first dimension has 2 elements and the second has 4
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('shape:',array.shape)

array2 = np.array([1, 2, 3, 4], ndmin=5)
print(array2)
print('shape of array :', array2.shape)

# Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print('1D to 2D:',newarr)

newarr2 = arr.reshape(2,3,2)
print('1D to 3D:',newarr2)
print(arr.reshape(4,2).base)