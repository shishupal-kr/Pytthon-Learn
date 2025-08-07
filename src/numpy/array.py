import numpy as np

#The array object in NumPy is called ndarray.
arr = np.array([1,2,3,4,5])

#1-Dimensional array
print(arr)
print(type(arr))
print('dimension: ',arr.ndim)

# O-Dimensional array
arr2 = np.array(42)
print(arr2)
print('dimension: ',arr2.ndim)

# 2-Dimensional array
arr3 = np.array([[1,2,3], [4,5,6]])
print (arr3)
print('dimension: ',arr3.ndim)

# 3-Dimensional array
arr4 = np.array([[[1,2,3],[4,5,10]], [[7,8,9],[4,5,6]]])
print(arr4)
print('dimension: ',arr4.ndim)