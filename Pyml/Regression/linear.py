from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]

model = linear_model.LinearRegression()
model.fit(X,y)
print(model.intercept_) # 截距
print(model.coef_) # 系数
a = model.predict([[12]])

X2 = [[0], [10], [14], [25]]
y2 = model.predict(X2)

plt.figure()
plt.title('匹萨价格与直径数据')
plt.xlabel('直径（英寸）')
plt.ylabel('价格（美元）')
plt.plot(X, y, 'k.')
plt.plot(X2,y2,'g-')

yr = model.predict(X)
for idx, x in enumerate(X):
    plt.plot([x,x],[y[idx],yr[idx]],'r-')
plt.show()






