"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""

"""
commands
Incremental Mode --> python Init.py TrainingData.txt 1 0.00001 TestingData.txt
Batch Mode --> python Init.py TrainingData.txt 2 0.00001 TestingData.txt
"""

import sys
import os.path
import FileReader
import GradDescInc
import GradDescBat
import PredictorForTests
def main():
    #checking arguments
    if len(sys.argv)!=5:
        print "<python Init.py TrainingData.txt OPTION LEARNINGRATE TestingData.txt>"
        print "OPTION --> 1 if Gradient Descent Incremental Mode"
        print "OPTION --> 2 if Gradient Descent Batch Mode"
        sys.exit()

    if not os.path.isfile(sys.argv[1]):
        print "File does not exist"
        print "<python Init.py TrainingData.txt OPTION LEARNINGRATE TestingData.txt>"
        print "OPTION --> 1 if Gradient Descent Incremental Mode"
        print "OPTION --> 2 if Gradient Descent Batch Mode"
        sys.exit()

    if not os.path.isfile(sys.argv[4]):
        print "File does not exist"
        print "<python Init.py TrainingData.txt OPTION LEARNINGRATE TestingData.txt>"
        print "OPTION --> 1 if Gradient Descent Incremental Mode"
        print "OPTION --> 2 if Gradient Descent Batch Mode"
        sys.exit()

    if(sys.argv[2]!='1' and sys.argv[2]!='2'):
        print "OPTION does not exist"
        print "<python Init.py TrainingData.txt OPTION LEARNINGRATE TestingData.txt>"
        print "OPTION --> 1 if Gradient Descent Incremental Mode"
        print "OPTION --> 2 if Gradient Descent Batch Mode"
        sys.exit()

    #calculating number of features
    firstline = open(sys.argv[1]).readline()
    first_example=[numbers for numbers in firstline.split("\t") if numbers is not ""]
    if len(first_example)<2:
        print "All lines in the file must be of the format <x1    x2  x3  y>"
    else:
        num_features=len(first_example)-1
    #reading from training file
    examples_features,examples_answers=FileReader.readfile(sys.argv[1],num_features,1)

    if sys.argv[2]=='1':
        weights=GradDescInc.GradientDescentIncremental(list(examples_features),list(examples_answers),float(sys.argv[3]))
    elif sys.argv[2]=='2':
        weights=GradDescBat.GradientDescentBatch(list(examples_features),list(examples_answers),float(sys.argv[3]))

    #reading from testing file
    testing_features=FileReader.readfile(sys.argv[4],num_features,2)
    PredictorForTests.PredictTests(list(weights),list(testing_features),"TestingDataPredictions.txt")
    print "Predictions can be found in TestingDataPredictions.txt"
    return 0
