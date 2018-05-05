"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8

import numpy as np
def initializeWeights(numNeurons):
    allWeights=[]
    for i in range(0,len(numNeurons)-1):
        weights=np.random.random((numNeurons[i+1],numNeurons[i]))*2-1
        allWeights.append(weights)
    return allWeights

def initializeBiases(numNeurons):
    allBiases=[]
    for i in range(0,len(numNeurons)-1):
        biases=np.random.random((numNeurons[i+1],1))*2-1
        allBiases.append(biases)
    return allBiases

def forwardProp(features,allWeights,allBiases):
    """
    input parameters
    features --> (numNeuronsInLayer x 1)
    allWeights --> all weights at each layer except output layer
    allBiases --> all biases at each layer except output layer
    output
    allOutputs --> list of outputs at each layer
    """
    allOutputs=[]
    allOutputs.append(features)
    for i in range(0,len(allWeights)):
        allOutputs.append(sigmoid(np.dot(allWeights[i],allOutputs[i])+allBiases[i]))
    return allOutputs

def backwardProp(original_target,predicted_target,allWeights):
    """
    target --> (numNeuronsOutLayer x 1)
    input parameters
    original_target --> original target given for one example
    predicted_target --> target predicted by the algorithm for one example
    allWeights --> all weights at each layer except output layer
    output
    allDeltas --> list of local gradients at each layer except input layer
    """
    allDeltas=[]
    allDeltas.insert(0,(original_target-predicted_target)*predicted_target*(1-predicted_target))
    for i in range(0,len(allWeights)-1):
        allDeltas.insert(0,np.dot(allWeights[-1-i].T,allDeltas[0]))
    return allDeltas

def sigmoid(x):
    return 1/(1+np.exp(-x))

def updateWeights(allOutputs,allDeltas,allWeights,learning_rate,training_features_size):
    """
    input parameters
    allOutputs --> all outputs at each layer calculated in forward propagation
    allDeltas --> list of local gradients calculated in backward propagation
    allWeights --> all weights at each layer except output layer
    learning_rate --> parameter to specify how fast to learn
    output
    allWeights --> all updated weights at each layer except output layer
    """
    for i in range(0,len(allWeights)):
        allWeights[i]=allWeights[i]+learning_rate*np.dot(allDeltas[i],allOutputs[i].T)
        # allWeights[i]=allWeights[i]+learning_rate*np.dot(allDeltas[i],allOutputs[i].T)/training_features_size
    return allWeights

def updateBiases(allDeltas,allBiases,learning_rate,training_features_size):
    """
    input parameters
    allDeltas --> list of local gradients calculated in backward propagation
    allBiases --> all biases at each layer except output layer
    learning_rate --> parameter to specify how fast to learn
    output
    allBiases --> all updated biases at each layer except output layer
    """
    for i in range(0,len(allBiases)):
        allBiases[i]=allBiases[i]+learning_rate*np.sum(allDeltas[i],axis=0,keepdims=True)
        # allBiases[i]=allBiases[i]+learning_rate*np.sum(allDeltas[i],axis=0,keepdims=True)/training_features_size
    return allBiases

def calculateError(original_targets,predicted_targets):
    """
    input parameters
    original_targets --> original targets given for each example
    predicted_targets --> targets predicted by the algorithm for each example
    output
    error --> mean squared error
    """
    assert len(original_targets)==len(predicted_targets)
    error=0
    for i in range(0,len(original_targets)):
        error=error+np.sum((original_targets[i]-predicted_targets[i])**2,axis=0,keepdims=True)/len(original_targets[i])
    error=error/len(original_targets)
    return error
