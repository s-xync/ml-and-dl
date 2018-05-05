"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8

import Conversions
def readFile(trainingdatafile,trainingtargetfile,testingdatafile,testingtargetfile,num_features):
    training_features=[]
    training_targets=[]
    testing_features=[]
    testing_targets=[]

    trainingdatafilep=open(trainingdatafile,'r')
    for line in trainingdatafilep:
        if line.strip():
            exampleString=[number for number in line.split("\t") if number is not ""]
            example=[]
            for exampleStringUnit in exampleString:
                example.append(float(exampleStringUnit))
            assert len(example)==num_features
            training_features.append(example);
    trainingdatafilep.close()

    trainingtargetfilep=open(trainingtargetfile,'r')
    for line in trainingtargetfilep:
        if line.strip():
            training_targets.append(int(line))
    trainingtargetfilep.close()
    training_targets=Conversions.convertIntsToArrs(training_targets)

    testingdatafilep=open(testingdatafile,'r')
    for line in testingdatafilep:
        if line.strip():
            exampleString=[number for number in line.split("\t") if number is not ""]
            example=[]
            for exampleStringUnit in exampleString:
                example.append(float(exampleStringUnit))
            assert len(example)==num_features
            testing_features.append(example);
    testingdatafilep.close()

    testingtargetfilep=open(testingtargetfile,'r')
    for line in testingtargetfilep:
        if line.strip():
            testing_targets.append(int(line))
    testingtargetfilep.close()
    testing_targets=Conversions.convertIntsToArrs(testing_targets)

    training_features=Conversions.convertListsToArrs(training_features)
    training_targets=Conversions.convertListsToArrs(training_targets)
    testing_features=Conversions.convertListsToArrs(testing_features)
    testing_targets=Conversions.convertListsToArrs(testing_targets)
    return training_features,training_targets,testing_features,testing_targets
