"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8

import numpy as np
def convertListsToArrs(listoflists):
    vectorlength=len(listoflists[0])
    listofvectors=[]
    for onelist in listoflists:
        listofvectors.append(np.array(onelist).reshape(vectorlength,1))
    return listofvectors

def convertIntsToArrs(targetInts):
    """
    0 --> [1,0,0]
    1 --> [0,1,0]
    2 --> [0,0,1]
    input parameters
    targetInts --> list of class levels as integers
    output
    targetArrs --> list of class levels converted into arrays of 1s and 0s
    """
    targetArrs=[]
    numNeurons=max(targetInts)+1
    for targetInt in targetInts:
        targetArr=[]
        for i in range(0,numNeurons):
            if i==targetInt:
                targetArr.append(1)
            else:
                targetArr.append(0)
        targetArrs.append(targetArr)
    return targetArrs

def convertArrsToInts(targetArrs):
    """
    [x,y,z] --> 0 if max([x,y,z])=x
    [x,y,z] --> 1 if max([x,y,z])=y
    [x,y,z] --> 2 if max([x,y,z])=z
    input parameters
    targetArrs --> list of class levels in probabilities
    output
    targetInts --> list of class levels as integers
    """
    targetInts=[]
    for i in range(0,len(targetArrs)):
        targetLists=targetArrs[i].tolist()
        targetFlatList=[]
        for targetList in targetLists:
            targetFlatList.extend(targetList)
        targetInts.append(targetFlatList.index(max(targetFlatList)))
    return targetInts
