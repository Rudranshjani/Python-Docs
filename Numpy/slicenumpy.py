import numpy as np 
a = np.arange(10) 
s = slice(2,7,2)  # same as b= [2:7:2]
print(a[s])


# slice single item 
a = np.arange(10) 
b = a[5] 
print(b)

#slice items starting from index 
a = np.arange(10) 
print(a[2:])


# slice items between indexes 
a = np.arange(10) 
print( a[2:5])

'''Multidimensional array'''
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:])
print(a[...,1])   # print items in 2nd column
print(a[1,...])   # items in the second row
print(a[...,1:])   #to fetch items column 1 onwards 


