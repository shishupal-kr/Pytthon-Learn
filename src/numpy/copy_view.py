import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()  # copy array - The copy SHOULD NOT be affected by the changes made to the original array.
arr[0] = 42
y = arr.view() # view array- Change the original array, and display both arrays:

print(arr)
print(x)
print(y)

# Print the value of the base attribute to check if an array owns it's data or not:
print(x.base)
print(y.base)