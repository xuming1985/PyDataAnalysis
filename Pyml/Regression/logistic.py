import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model, datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1 加载数据库 ，包括数据清洗
iris = datasets.load_iris()
x = iris.data[:,:2]
y = iris.target

# 2 数据集分割，训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)

# 3 标准化特征值
sc = StandardScaler()
sc.fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

# 4 训练模型
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(x_train_std, y_train)

# 5 预测
predict = logreg.predict_proba(x_test_std)
acc = logreg.score(x_test_std, y_test)

print(predict)
print(acc)