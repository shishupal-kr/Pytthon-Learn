import numpy as np

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate((arr,arr2))
print(arr3)

#Stacking is same as concatenation,the only difference is that stacking is done along a new axis.
arr4 = np.stack((arr,arr2), axis=1)
print(arr4)

#along Row
arr5 = np.hstack((arr,arr2))
print('along row:',arr5)

#along column
arr6 = np.vstack((arr,arr2))
print('along column:',arr6)

#depth
arr7 = np.dstack((arr,arr2))
print('depth:',arr7)