"""
Machine Learn Study
liu.z

"""

import numpy as np
import random
import math

# SA,Simulated Annealing
#

def createData(row, column):
    dataSet = np.arange(row * column)
    for i in range(row * column):
        dataSet[i] = random.randint(1000, 10000)
    dataSet.resize((row, column))
    return dataSet

def getMax(dataSet, row, column):
    r = 0.98
    T = 100.0
    T_Min = 12.0
    index0 = [random.randint(0, row - 1), random.randint(0, column - 1)]

    while T > T_Min:
        print(index0, T, dataSet[index0[0]][index0[1]])

        listPos = []
        if index0[0] > 0:
            listPos.append([index0[0] - 1, index0[1]])
        elif index0[0] + 1 < row:
            listPos.append([index0[0] + 1, index0[1]])
        if index0[1] > 0:
            listPos.append([index0[0], index0[1] - 1])
        elif index0[1] + 1 < column:
            listPos.append([index0[0], index0[1] + 1])

        index = -1
        for i in range(len(listPos)):
            if dataSet[index0[0]][index0[1]] < dataSet[listPos[i][0], listPos[i][1]]:
                index = i
        if index != -1:
            index0 = listPos[index]
            continue
        
        index = random.randint(0, len(listPos) - 1)
        de = np.float(dataSet[index0[0]][index0[1]] - dataSet[listPos[index][0], listPos[index][1]])
        if math.exp(de / T) > random.uniform(0, 1):
            index0 = listPos[index]

        T = T * r


    return dataSet[index0[0]][index0[1]]
