import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([[4,5,6],[7,8,9]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[2])
print(arr2[0,1])
print(arr2[1,1])
print(arr3[1,0,2])