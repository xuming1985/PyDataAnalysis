import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def load_data(filename):
    data = []
    labels = []
    datafile = open(filename)
    for line in datafile:
        fields = line.split('\t')
        for field in fields[:-1]:
            try:
                if field != "":
                    data.append(float(field))
            except:
                print("error:"+ field)

        labels.append(float(fields[-1].replace("\n","")))
    data = np.array(data)
    labels = np.array(labels)
    data = data.reshape(labels.shape[0], -1)
    return data, labels

def testLR(features, labels):
    lr_model = LogisticRegression()
    lr_model.fit(features, labels)
    predict = lr_model.predict_proba()

features, labels = load_data('seeds_dataset.txt')
print(features)
print(labels)

print('LogisticRegression: \r')
