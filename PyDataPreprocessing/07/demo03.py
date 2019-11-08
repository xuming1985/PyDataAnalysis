import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

x1, y1 = datasets.make_circles(n_samples=5000, factor=.6, noise=0.05)
x2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
print(x1)
print(y1)

x = np.vstack((x1,x2))
result = KMeans(n_clusters=3, random_state=9).fit_predict(x)

colours = ["red", "green", "blue"]
plt.scatter(x[:, 0], x[:, 1], c=[colours[i] for i in result])
plt.show()
