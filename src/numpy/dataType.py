import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#The astype() function creates a copy of the array,
# and allows you to specify the data type as a parameter.
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(arr.dtype)
print(newarr)
print(newarr.dtype)

newarr2 = arr.astype(int)
print(newarr2.dtype)