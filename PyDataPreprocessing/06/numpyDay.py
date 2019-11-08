import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())
print(df.tail())
print(df.columns)
print(df.index)
print(df.ix[10:20,0:3])
print(df.iloc[[1,3,5],[2,4]])
print(df[df.tip>8])

# print(df[(df.tip>7)|(df.total_bill>50)])
# print(df.T)
print(df.sort_values(by='tip'))
