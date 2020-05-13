import numpy as np 

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] 
print(y)             #[1  4  5]



x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print 'Our array is:' 
print(x)
print("\n")    #same matrix 
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]             #corner elements


# slicing 
z = x[1:4,1:3]    #x[[1,2,3],[1,2]]
print 'After slicing, our array becomes:' 
print(z)              

# using advanced index for column 
y = x[1:4,[1,2]] 
print 'Slicing using advanced index for column:' 
print(y)                      # gives same result as above



# Boolean indexing
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

# Now we will print the items greater than 5 
print 'The items greater than 5 are:' 
print x[x > 5]

#COmplementing nan
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print(a[~np.isnan(a)])

#filter out the non-complex elements from an array.
a = np.array([1, 2+6j, 5, 3.5+5j])    
print(a[np.iscomplex(a)])


#broadcasting an array
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])
print(a + b)

#iterating over array
a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a):
    print(x)

b=a.T  #TRANSPOSE of a

c = b.copy(order = 'C')
print(c)

#c = b.copy(order = 'F')
for x in np.nditer(c):
   print(x)
