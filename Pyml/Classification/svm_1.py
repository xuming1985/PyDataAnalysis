import matplotlib.pyplot as plt
import numpy as np

def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append([float(lineArr[2])])
    return dataMat, labelMat


def showDataSet(dataMat, labelMat):
    data_plus = []
    data_minus = []



if __name__ == '__main__':
    dataMat, labelMat = loadDataSet('svm_1_data.txt')
    showDataSet(dataMat, labelMat)
    print(dataMat)
    print(labelMat)