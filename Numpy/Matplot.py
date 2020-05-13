import numpy as np 
from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

plt.subplot(5,2,8)
plt.plot(x,y,"g-.")
#plt.plot(x,x,"or")
z=x    #z=[15,7,17,8,9]
plt.subplot(2,2,4)
plt.plot(z,x)

#plt.bar(x,y)  # bar graph
#plt.scatter(x, y)   # scatter graph/plot
#plt.hist(x,bins=[1,2,3,4,5])   # histogram plot ---->in range of 2 to3 u are getting only one occurence
#x = np.arange(1,11) 
#z = 2*x
    #plt.plot(x,y,'k-.')  #line graph
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
#plt.plot(z,x,"og") 
plt.show() 

              
