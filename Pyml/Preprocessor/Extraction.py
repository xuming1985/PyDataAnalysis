from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler

x = [{'city': '北京', 'temperature': 100},
     {'city': '上海', 'temperature': 60},
     {'city': '深圳', 'temperature': 30}]

doc = {
    'The MissingIndicator transformer is useful',
    'to transform a dataset into corresponding binary matrix',
    'The MissingIndicator transformer is very very useful'
}

vec = CountVectorizer()

d1 = vec.fit_transform(doc)
print(vec.get_feature_names())
print(d1)
print(d1.toarray())


