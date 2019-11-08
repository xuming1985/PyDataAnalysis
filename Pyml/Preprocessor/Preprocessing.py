import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

x1= np.random.randint(1,20,100)
x2 = x1.reshape(10,10)
x3 = pd.DataFrame(x2, columns=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10'])
print(x3)

x4 = x3.apply(lambda x:np.log(x))
#print(x4)

# 0-1 化
# print(MinMaxScaler().fit_transform(x3))

# 标准化
print(StandardScaler().fit_transform(x3))

# 特征统计
print("最小值:", x3.min())
print("最大值:", x3.max())
print("中值:", x3.median())
print("平均值:", x3.mean())
print("0.25分位数:", x3.quantile(0.25))
print("0.5分位数:", x3.quantile(0.5))
print("0.75分位数:", x3.quantile(0.75))