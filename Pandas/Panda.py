import pandas as pd
import numpy as np

'''series'''

s = pd.Series()            #Create an Empty Series
print(s)

data = np.array(['a','b','c','d'])    #Create a Series from ndarray
#s = pd.Series(data,index=[100,101,102,103]) # assigning indexes
s = pd.Series(data)
print(s)


data = {'a' : 0., 'b' : 1., 'c' : 2.}  # creating  a Series from dict
#s = pd.Series(data,index=['b','c','d','a'])  # assigning list indexes
s = pd.Series(data)              
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])         # Create a Series from Scalar
print s


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print s[0]         #Accessing Data from Series with Position
print s[:3]                #retrieve the first three element
print s[-3:]           #retrieve the last three element

print s['a']           #Retrieve Data Using Label 
print s[['a','c','d']]       #Retrieve multiple elements using a list of index label values.
print s['f']          # If a label is not contained, an exception is raised



''' Dataframes'''
df = pd.DataFrame()              #Empty DataFrame
print(df)

data = [1,2,3,4,5]             #DataFrame from Lists
df = pd.DataFrame(data)
print (df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
#df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
df = pd.DataFrame(data)     #DataFrame from Dict of ndarrays / Lists
print df


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)             #DataFrame from List of Dicts
#df = pd.DataFrame(data, index=['first', 'second'])        #passing row indices
print df

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df1)

'''Column operations'''

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}   #DataFrame from Dict of Series

df = pd.DataFrame(d)
print df

print df ['one']          #Column Selection

df['three']=pd.Series([10,20,30],index=['a','b','c'])         #Adding a new column 
print df



del df['one']          # deleting column
df.pop('two')
print(df)

'''Row operations'''

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.loc['b']               #row selection using loc

print df.iloc[2]                  #row selection using iloc

print df[2:4]      #selecting multipe rows/ slice operation



df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)              # addition of new row using append
print df

df = df.drop(0)             # deletion of row
print df




