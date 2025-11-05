# Arrays 

# array_one = [1,2,3,4,5]
# print(array_one[0])  # Accessing elements at index 0 and 2, 4


#Two dimensional arraysarray_two = [[1,2,3],[4,5,6],[7,8,7]]
# 2D array using numpy

# import numpy as np
# arr =np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print( arr.ndim)

# Lists

#Create a list of colors
list = ['red', 'blue', 'green']
print(list)


#Append another color to the list
list.append('yellow')
print(list)


#Remove a color from the list
list.pop(1)
print(list)

#Insert a color at index 1
list.insert(1, 'black')
print(list)

#Using del to remove an item at a specific index
del list[2]
print(list)

#Using extend to add multiple items to the list
list.extend(['white', 'purple'])