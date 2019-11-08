import numpy as np
import pandas as pd

index = pd.date_range('1/1/2019', periods=8, freq='M')

r = np.random.randn(5)
print(r)
print(pd.Series(r, index=['a', 'b', 'c', 'd', 'e']))

df =pd.DataFrame(np.random.randn(8,3),index=index, columns=['A','B','C'])
print(df)

print(df.index.array)