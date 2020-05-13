import numpy as np 
print 'Binary equivalents of 13 and 17:' 
a,b = 13,17 
print bin(a), bin(b) 
print np.bitwise_and(13, 17)
print np.bitwise_or(13, 17)
print np.left_shift(10,2)

#String functions
print np.char.add(['hello'],[' xyz'])
print np.char.add(['hello', 'hi'],[' abc', ' xyz'])

print np.char.multiply('Hello ',3)
print np.char.center('hello', 20,fillchar = '*')
print np.char.capitalize('hello world')
print np.char.title('hello how are you?')
print np.char.lower('HELLO')
print np.char.replace ('He is a good boy', 'is', 'was')
a = np.char.encode('hello', 'cp500')

#trignometroc functions
a = np.array([0,30,45,60,90])
c=np.sin(a*np.pi/180)
print np.sin(a*np.pi/180)

inv = np.arcsin(a)
print inv
print np.degrees(inv)

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print np.floor(a)
print np.ceil(a)

print np.around(a) 
print np.around(a, decimals = 1) 
print np.around(a, decimals = -1)

#arithmetic operations
a = np.arange(9, dtype = np.float_).reshape(3,3)
b = np.array([10,10,10])
print np.add(a,b)
print np.subtract(a,b)
print np.multiply(a,b)
a = np.array([0.25, 1.33, 1, 0, 100])
print np.reciprocal(a)
a = np.array([10,100,1000])
print np.power(a,2)

a = np.array([-5.6j, 0.2j, 11. , 1+1j])
print np.real(a)
print np.imag(a)
print np.conj(a)
print np.angle(a)
print np.angle(a, deg = True)

# Statistical operations
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print np.amin(a,1)
print np.amin(a,0)
print np.amax(a)
print np.amax(a, axis = 0)
print np.ptp(a)
print np.ptp(a, axis = 1)
print np.ptp(a, axis = 0)
print np.median(a)
print np.median(a, axis = 0)
print np.median(a, axis = 1)
print np.mean(a)
print np.mean(a, axis = 0)
print np.mean(a, axis = 1)
print np.std([1,2,3,4])   # std. deviation , std = sqrt(mean(abs(x - x.mean())**2))
print np.var([1,2,3,4])  #mean(abs(x - x.mean())**2)   

# sorting examples:
a = np.array([[3,7],[9,1]]) 
print np.sort(a)
print np.sort(a, axis = 0)

#Order parameter in sort function 
dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt)
print np.sort(a, order = 'name')

nm = ('raju','anil','ravi','amar') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 
ind = np.lexsort((dv,nm))
print [nm[i] + ", " + dv[i] for i in ind]

a= np.array([[ 2, 0, 1], [ 5, 4, 3]])
y = np.argsort(a)
print(Y)


print(x)
w= np.argsort(a, kind ='mergesort', axis = 1)
print(w)
a = np.array([[30,40,70],[80,20,10],[50,90,60]])

print np.argmax(a)
maxindex = np.argmax(a, axis = 0)
maxindex = np.argmax(a, axis = 1)
print maxindex

a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print np.nonzero (a)
0=a[np,nonzero(a)]
print (o)

x = np.arange(9.).reshape(3, 3)
print np.extract(condition, x)


# linear algebra
import numpy.matlib 
import numpy as np
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
np.dot(a,b)                 #[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]

print np.vdot(a,b)   #1*11 + 2*12 + 3*13 + 4*14 = 130

a = np.array([[1,2], [3,4]]
b = np.array([[11, 12], [13, 14]])         
print np.inner(a,b)                 #[1*11+2*12, 1*13+2*14 3*11+4*12, 3*13+4*14 ]

a = np.array([[1,2], [3,4]]) 
print np.linalg.det(a)
y = np.linalg.inv(x) 

