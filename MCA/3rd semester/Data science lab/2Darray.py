import numpy as np

array=np.array([[1,2,3,4],[2,4,6,8],[1,3,5,7],[9,8,7,6]])
print(array)

print("Display all element exclude 1st row:")
print(array[1:,:])

print("Display all element exclude last column:")
print(array[:,:3])

print("Display elements of 1st and 2nd column in 2nd & 3rd row:")
print(array[1:3,0:2])

print("Display all element in 2nd & 3rd column:")
print(array[:,1:3])

print("Display all element of 2nd & 3rd element of 1st row:")
print(array[:1,1:3])