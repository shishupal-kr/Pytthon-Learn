import numpy as np

arr = np.array([1,2,3,4,5,6])

arr2 = np.array_split(arr,3)
print(arr2)

print(arr2[0])
print(arr2[1])
print(arr2[2])

arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new = np.array_split(arr3,3)
print(new)

new2 =np.array_split(arr3,3,axis=1)
print('along column:',new2)

#hsplit() is used spli 2d array into 2 or more  2d array along column
new3 = np.hsplit(arr3,2)
print(new3)