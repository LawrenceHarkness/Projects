import numpy as np

import pandas as pd

# Creating a Series by passing a list of values, letting pandas create a default integer index

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=10, freq='D') # H-Hours, M-Months, W-Weeks, Y-Years, s-seconds
print(dates)

df = pd.DataFrame(np.random.randn(10, 5), index=dates, columns=list('ABCDE'))
print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': pd.Series('foo',index=list(range(4)), dtype='str'),
                    'G': pd.date_range('20130101', periods=4, freq='M')
                    })
print(df2)
print(df2.dtypes)

# Here is how to view the top and bottom rows of the frame:

print(df.head())
print(df.tail())


# Display the index, columns:

print(df.index)
print(df.columns)

# Quick
print(df2.describe())

# Sorting columns
print(df.sort_index(axis=1, ascending=True))

# Sorting by specfic columns
print(df.sort_values(by='B'))

# Marks Test DF

dfMarks = pd.DataFrame({'Names': ['Tom', 'John', 'Lawrence', 'Thabo', 'Jack', 'Jill'],
                    'Points': np.random.randn(6)
                    })

print(dfMarks)
print('')
print(dfMarks.sort_values(by='Names'))
print('')
print(dfMarks.sort_values(by='Points', ascending=False))


print('-------------------seperator----------------------')
print(df[0:3]) # firnt three rows
print('-------------------seperator1----------------------')
print(df['20130102':'20130104']) # only theese two rows
print('-------------------seperator2----------------------')
print(df.loc[dates[0]]) # first row
print('-------------------seperator-3---------------------')
print(df.loc[:, ['A', 'B', 'C']])
print('-------------------seperator--4--------------------')
print(df.loc['20130102':'20130104', ['A', 'B']])
print('-------------------seperator---5-------------------')
print(df.loc[dates[0], 'A'])
print('-------------------seperator---6-------------------')
print(df.at[dates[0], 'A'])
print('-------------------seperator--7--------------------')
print(df.iloc[[3],[3]])
print('-----------------------------separator---------------------------')
# MERGE

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

pieces = [df[7:], df[3:7], df[:3]]

print(pd.concat(pieces))

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(left)

print(right)

print(pd.merge(left, right, on='key'))#



#ploting
ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()
ts.plot()