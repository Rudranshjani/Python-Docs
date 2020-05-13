import numpy as np 
a = np.array([1,2,3]) 
print(a)
print("\n")

b=np.array([[1,3,6],[2,4,8]])
print(b)
print(b.shape)
#b.shape=(3,2)
#a=b.reshape(3,1)
#print(b)
print(b.size)
print("\n")

c= np.array([1,2,3,4,5], dtype = int)
print(c)
print( c.itemsize)
print(c.dtype.name)
print("\n")

a = np.array([1, 2, 3], dtype = complex) 
print(a)

d = np.arange(15).reshape(3, 5)
print(d)
print(type(d))

# length of each element in bytes
x = np.array([1,25,3,4,5], dtype = np.int32)
print (x.itemsize)

#x = np.array([1,2,3,4,5], dtype = np.float32) 
#print(x.itemsize)

#empty array
#x = np.empty([3,2], dtype = int) 
#print(x)

# array of five zeros. Default dtype is float 
'''x = np.zeros(5)
'''
#x = np.zeros((5,), dtype = np.int)
print(x)

x = np.ones([2,2], dtype = int) 
print(x)'''

x = [1,2,3] 
a = np.asarray(x)
#a = np.asarray(x, dtype = float) 
print(a)


# ndarray from tuple
'''x = (1,2,3) 
a = np.asarray(x) 
print(a)

#ndarray from list of tuples
x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print a


# list = range(5)
it = iter(list)
x = np.fromiter(it, dtype = float) 
print (x)




#making array from numerical ranges
x = np.arange(5)
#x = np.arange(10,20,2)

#x = np.linspace(10,20,5)
#x = np.linspace(10,20, 5, endpoint = False) 
#x = np.linspace(1,2,5, retstep = True) 
print(x)

a = np.logspace(1.0, 2.0, num = 10) 
print(a)

#set base of log space to 2
a = np.logspace(1,10,num = 10, base = 2) 
print(a)'''

