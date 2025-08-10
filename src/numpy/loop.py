import numpy as np

#2d
arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
for x in arr:
         print(x)

#3d
arr2 = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
for x in arr2:
    print(x)

#nditer()
arr3 =np.array([[[1,2],[3,4],[5,6],[7,8]]])
for x in np.nditer(arr3):
    print(x)