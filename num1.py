import numpy as np  
arr =np.array([5,6,7,8,9])
# Use a tuple to create a NumPy array:
# arr=np.array(())
# arr = np.array((1, 2, 3, 4, 5))

# Dimensions in Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr=np.array(42)

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr = np.array([1, 2, 3, 4, 5])

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) 

# Higher Dimensional Arrays
# When the array is created, you can define the number of dimensions by using the ndmin argument.
arr = np.array([1, 2, 3, 4], ndmin=5)
print('number of dimensions :', arr.ndim) 
print(arr)
print(type(arr))