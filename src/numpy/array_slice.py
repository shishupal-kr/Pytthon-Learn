import numpy as np

arr = np.array([1,2,3,4,5,6,7])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1:5]) #this result include start idx but exclude end idx
print(arr[:4]) #from 1st idx to 4th idx
print(arr[2:]) # till last idx
print(arr[-2:-1])
print(arr[1:6:2])
print(arr[::2])
print(arr2[1,1:4])
