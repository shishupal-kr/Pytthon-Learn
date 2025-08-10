import numpy as np

# filter return only true value
arr = np.array([41,42,43,44])
x = [True,False,True,True]
new = arr[x]
print(new)

#creating filter array
farr = []
for x in arr:
    if x > 42:
        farr.append(True)
    else:
        farr.append(False)
new2 = arr[farr]
print(farr)
print(new2)

#or
arrf = arr > 43
new3 = arr[arrf]
print(new3)