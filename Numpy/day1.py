1# '''install numpy'''
2# '''import numpy'''
import numpy as np
3# '''creating arrays'''
# 1d array
array = np.array([1,2,3,4,5])
print(array)
# 2d array
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
# array filled with zero and ones
zeros =np.zeros((3,3))
ones=np.ones((2,4))
print(ones)
print(zeros)
# array with a range of numbers
array_range = np.arange(0,10,2)
print(array_range)
# array with random numbers
random_arr = np.random.rand(3,3)
print(random_arr)
4# '''array operations'''
#  1 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
sum1= arr1 + arr2   # addition
sum2= arr1 - arr2   # substract
sum3= arr1 * arr2   # multiply
sum4= arr1 / arr2   # division
print("sum:",sum1)
print("sum:",sum2)
print("sum:",sum3)
print("sum:",sum4)
#  2
matrix1= np.array([[1,2],[3,4]])
matrix2= np.array([[5,6],[7,8]])
matrix_product = np.dot(matrix1,matrix2)
print(matrix_product)
#  3
arr = np.arange(1,10)
reshaped_arr = arr.reshape(3,3)
print(reshaped_arr)
#  4
transposed_matrix = reshaped_arr.T
print(transposed_matrix)