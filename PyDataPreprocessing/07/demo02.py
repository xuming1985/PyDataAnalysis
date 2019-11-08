'''
数据缺失处理函数
'''
from pandas import Series,DataFrame
from numpy import nan as NA
from scipy.interpolate import  lagrange
import numpy as np
#
#data = Series([12,None,34,NA,68])
#print(data)
#print(data.isnull())
#dropna 过滤删除
#print(data.dropna())

data1 = DataFrame(np.random.randn(5,4))
data1.loc[:2,1] = NA
data1.loc[:3,2] = NA
data1.loc[0,0] = NA
# print(data1)
# print(data1.dropna(axis=1))
# print(data1.dropna(thresh=2))

# fillna 数据填充
data = DataFrame(np.random.randn(5,4))
data.loc[:2,1] = NA
data.loc[:3,2] = NA
# print(data)
# print(data.fillna(0))
# print(data.fillna({1:11,2:22}))
# print(data.fillna({1:data[1].mean(),2:data[2].mean()}))

# 拉格朗日插值法

# from pandas import *
# df = DataFrame(np.random.randn(20,2),columns=['first','second'])
# df['first'][(df['first']<-1.5)|(df['first']>1.5)] = None
# print(df)
#
#
# #插值函数
# def ployinterp_column(s,n,k=5):                                 # s列向量，n为被插值的位置，k为取前后的数据个数
#     y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]            #取值
#     y = y[y.notnull()]                                          #剔除空值
#     return lagrange(y.index,list(y))(n)                         #插值并返回插值结果
#
# # 逐个元素判断
# for i in df.columns:
#     for j in range(len(df)):
#         if (df[i].isnull())[j]:
#             df[i][j] = ployinterp_column(df[i],j)
#
# print(df)



'''
检测和过滤异常值
'''
# from pandas import *
# import numpy as np
#
# data = DataFrame(np.random.randn(10,4))
# print(data)
# print(data.describe())
#
# print('\n找出第3列绝对值大于1的项\n')
# data1 = data[2]
# print(data1[np.abs(data1)>1])
# data1[np.abs(data1)>1] = 100
# print(data)

'''
移除重复数据
'''
# from pandas import *
# import numpy as np
#
# data = DataFrame({'name':['zhangsan']*3+['wang']*4,'age':[18,18,19,19,20,20,21]})
# print(data)
# print(data.duplicated())
# print(data.drop_duplicates())

'''
数据规范化
'''
# import pandas as pd
# import numpy as np
#
# datafile = './ori_data.xlsx'
# data = pd.read_excel(datafile,header=None)
# print(data)
# min = (data-data.min())/(data.max()-data.min())
# zero = (data-data.mean())/data.std()
# float = data/10**np.ceil(np.log10(data.abs().max()))
# print(min)
# print(zero)
# print(float)

'''
汇总和描述等统计计量的计算
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),index=list('abcd'),columns=['first','sencond','third'])
print(df)
print(df.describe())

print(df.sum())
print(df.sum(axis=1))

print(df.idxmin())
print(df.idxmin(axis=1))

print(df.idxmax())
print(df.idxmax(axis=1))

print(df.var())
print(df.std())
print(df.cumsum())

print(df.pct_change())