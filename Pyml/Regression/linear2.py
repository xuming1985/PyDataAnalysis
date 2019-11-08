from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import time
import numpy as np

xx = np.linspace(30,400,100)
print(xx)
print(xx.shape[0])
print(xx.reshape(xx.shape[0],1))


boston = load_boston()
X = boston.data
y = boston.target

print("X.shape:{}. y.shape:{}".format(X.shape, y.shape))
print('boston.feature_name:{}'.format(boston.feature_names))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)
model = LinearRegression()

start = time.time()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('time used:{0:.6f}; train_score:{1:.6f}, sv_score:{2:.6f}'.format((time.time()-start),train_score, cv_score))

def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)

    linear_regression = LinearRegression(normalize=True)
    pipeline = Pipeline([('polynomial_features', polynomial_features),
                         ('linear_regression', linear_regression)])
    return pipeline
