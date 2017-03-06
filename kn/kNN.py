# KNN

import numpy as np
import operator
import random

def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
    

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

def createFile(filename):
    fr = open(filename, 'w')
    for index in range(0, 1000):
        dist = random.uniform(1000, 99999)
        time = random.uniform(0, 30)
        ice = random.uniform(0, 2)
        datetype = random.randint(1, 3)
        line = '{dist}\t{time}\t{ice}\t{datetype}\n'.\
               format(dist = dist, time = time, ice = ice, datetype = datetype)
        fr.write(line)
    fr.close()

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = in(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], \
                                     datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" \
              % (classifierResult, datingLabels[i]))
        if classifierResult != datingLables[i]:  errorCount += 1.0

    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPersion():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input(\
        'percentage of time spend playing video games?'))
    
