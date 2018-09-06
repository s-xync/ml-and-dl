"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8

import sys
import os.path
import numpy as np
import FileReader
import PerceptronLearning
import Conversions
import time

def main():
    if len(sys.argv)!=5:
        print "<python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt>"
        sys.exit()

    if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]) or not os.path.isfile(sys.argv[3]) or not os.path.isfile(sys.argv[4]):
        print "File does not exist"
        print "<python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt>"
        sys.exit()

    #calculating number of features
    firstline = open(sys.argv[1]).readline()
    first_example=[numbers for numbers in firstline.split("\t") if numbers is not ""]
    if len(first_example)<1:
        print "There must be more than one feature in the data."
    else:
        num_features=len(first_example)
    #reading from training file
    training_features,training_targets,testing_features,testing_targets=FileReader.readFile(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],num_features)
    assert len(training_features)==len(training_targets)
    assert len(testing_features)==len(testing_targets)
    learning_rate=float(raw_input("What is the learning rate? "))
    assert learning_rate>0 and learning_rate<1
    num_iterations=input("How many iterations? ")
    assert num_iterations>0
    numHidLayers=input("How many HIDDEN LAYERS? ")
    assert isinstance(numHidLayers,int)
    numNeuronsInLayer=num_features
    numNeuronsOutLayer=len(testing_targets[0])
    numNeuronsHidLayers=[]
    for i in range(0,numHidLayers):
        numNeuronsHidLayers.append(input("How many Neurons Hidden Layer "+str(i+1)+" : "))
        assert isinstance(numNeuronsHidLayers[i],int)
    tic=time.time()
    numNeurons=[]
    numNeurons.append(numNeuronsInLayer)
    numNeurons.extend(numNeuronsHidLayers)
    numNeurons.append(numNeuronsOutLayer)
    allWeights=PerceptronLearning.initializeWeights(numNeurons)
    allBiases=PerceptronLearning.initializeBiases(numNeurons)

    for i in range(0,num_iterations):
        predicted_targets=[]
        for j in range(0,len(training_features)):
            allOutputs=PerceptronLearning.forwardProp(training_features[j],allWeights,allBiases)
            predicted_targets.append(allOutputs[-1])
            allDeltas=PerceptronLearning.backwardProp(training_targets[j],predicted_targets[j],allWeights)
            allBiases=PerceptronLearning.updateBiases(allDeltas,allBiases,learning_rate,len(training_features))
            allWeights=PerceptronLearning.updateWeights(allOutputs,allDeltas,allWeights,learning_rate,len(training_features))
        if i%100==99:
            error=PerceptronLearning.calculateError(training_targets,predicted_targets)
            print "Error at iteration",i,"is",np.squeeze(error)

    predicted_test_targets_arrs=[]
    for i in range(0,len(testing_features)):
        allOutputs=PerceptronLearning.forwardProp(testing_features[i],allWeights,allBiases)
        predicted_test_targets_arrs.append(allOutputs[-1])
    testing_targets=Conversions.convertArrsToInts(testing_targets)
    predicted_test_targets=Conversions.convertArrsToInts(predicted_test_targets_arrs)
    # print "original"
    # print testing_targets
    # print "predicted"
    # print predicted_test_targets

    assert len(testing_targets)==len(predicted_test_targets)
    correct=0
    total=0
    for i in range(0,len(testing_targets)):
        total+=1
        if testing_targets[i]==predicted_test_targets[i]:
            correct+=1
    print "The accuracy is",correct/float(total)
    toc=time.time()
    print "Running Time :",(toc-tic)
    return 0
