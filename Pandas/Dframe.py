
import numpy as np
import pandas as pd
'''dates = pd.date_range('20130101', periods=6)  #Creating a DataFrame by passing a NumPy array
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
'''
#by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({'A': 1.,'B': pd.Timestamp('20130102'),
                       'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                       'E': pd.Categorical(["test", "train", "test", "train"]),
                       'F': 'foo'})
print(df2) 


print(df2.head(2))
print(df2.tail(2))
