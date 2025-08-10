import numpy as np

arr = np.array([1,4,3,2,4,3,4,2,3])
x = np.where( arr == 3)
print(x)

arr2 = np.array([6,7,8,9])
y = np.searchsorted(arr2,8)
print(y)

z = np.searchsorted(arr2, 8, side='right')
print(z)