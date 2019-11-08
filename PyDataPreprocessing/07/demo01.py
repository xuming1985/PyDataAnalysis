'''
Pandas的两种常见数据结构
'''
from pandas import Series,DataFrame

s = Series([1,2,3.0,'abc','def'])
print(s)

s1 = Series([1,2,3.0,'abc','def'],index=[10,20,30,60,80])
print(s1)

print('***********************************************************')

data = {'id':[100,101,102,103,104],'name':['aa','bb','cc','dd','ee'],'age':[18,19,20,19,18]}
data1 = DataFrame(data)
print(data1)

data2 = DataFrame(data,index=['one','two','three','four','five'])
print(data2)