#encoding:utf-8
import numpy as np
import pydotplus
from sklearn import tree
from sklearn.model_selection import train_test_split


def outlook_type(s):
    it = {'sunny': 1, 'overcast': 2, 'rainy': 3}
    return it[s.decode('utf-8')]


def temperature(s):
    it = {'hot': 1, 'mild': 2, 'cool': 3}
    return it[s.decode('utf-8')]


def humidity(s):
    it = {'high': 1, 'normal': 0}
    return it[s.decode('utf-8')]


def windy(s):
    it = {'TRUE': 1, 'FALSE': 0}
    return it[s.decode('utf-8')]


def play_type(s):
    it = {'yes': 1, 'no': 0}
    return it[s.decode('utf-8')]


play_feature_E = ('outlook', 'temperature', 'humidity', 'windy')
play_class = ('yes', 'no')

data = np.loadtxt("play.tennies.txt", delimiter=" ", dtype=str, skiprows=1,  converters={0:outlook_type, 1:temperature, 2:humidity, 3:windy,4:play_type})
x, y = np.split(data,(4,),axis=1)

#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=2)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf = tree.DecisionTreeClassifier(criterion='entropy')
print(clf)
clf.fit(x_train, y_train)
print(clf.feature_importances_)

answer = clf.predict(x_train)
y_train = y_train.reshape(-1)
print(answer)
print(y_train)
print(np.mean(answer == y_train))

answer = clf.predict(x_test)
y_test = y_test.reshape(-1)
print(answer)
print(y_test)
print(np.mean(answer == y_test))

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=play_feature_E, class_names=play_class,
                                filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('play1.pdf')

graph.get_nodes()[7].set_fillcolor("#FFF2DD")
from IPython.display import Image
Image(graph.create_png())
