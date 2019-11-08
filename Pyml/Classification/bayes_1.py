import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

print(twenty_train.target)
print(twenty_train.target_names)
print(len(twenty_train.data))  # 训练集中数据的长度
print(len(twenty_train.filenames))  # 训练集文件名长度

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts)
print(X_train_counts.shape)