"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""

# python Init.py TrainingData.txt 2 0.00001 TestingData.txt
# convergence condition is abs(present_error-previous_error)>0.0001

import Predictor
import MeanSquaredErrorFunction
def GradientDescentBatch(examples_features,examples_answers,learning_rate):
    num_features=len(examples_features)
    #initialising weights
    weights=[]
    for i in range(0,num_features):
        weights.append(0.1)
    previous_error=0
    examples_predictions=Predictor.Predict(weights,list(examples_features))
    present_error=MeanSquaredErrorFunction.calculateError(examples_answers,examples_predictions)

    differences=[]
    for i in range(0,len(examples_answers)):
        differences.append(0)

    while abs(present_error-previous_error)>0.0001:
    # while present_error-previous_error>0.01:
        for i in range(0,len(examples_answers)):
            differences[i]=(examples_predictions[i]-examples_answers[i])
        for i in range(0,len(examples_features)):
            differential=0
            for j in range(0,len(examples_answers)):
                differential=differential+(differences[j]*examples_features[i][j])
            differential=differential/len(examples_answers)
            weights[i]=weights[i]-learning_rate*differential
        previous_error=present_error
        examples_predictions=Predictor.Predict(weights,list(examples_features))
        present_error=MeanSquaredErrorFunction.calculateError(examples_answers,examples_predictions)
    print weights
    return weights
