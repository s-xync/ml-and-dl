"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""

# python Init.py TrainingData.txt 1 0.00001 TestingData.txt
# abs(present_error-previous_error)>0.001

import Predictor
import MeanSquaredErrorFunction
def GradientDescentIncremental(examples_features,examples_answers,learning_rate):
    num_features=len(examples_features)
    #initialising weights
    weights=[]
    for i in range(0,num_features):
        weights.append(0.1)

    previous_error=0
    examples_predictions=Predictor.Predict(weights,list(examples_features))
    present_error=MeanSquaredErrorFunction.calculateError(examples_answers,examples_predictions)

    while abs(present_error-previous_error)>0.001:
        for i in range(0,len(examples_answers)):
            for j in range(0,num_features):
                weights[j]=weights[j]-learning_rate*(examples_predictions[i]-examples_answers[i])*examples_features[j][i]
            examples_predictions=Predictor.Predict(weights,list(examples_features))
        previous_error=present_error
        examples_predictions=Predictor.Predict(weights,list(examples_features))
        present_error=MeanSquaredErrorFunction.calculateError(examples_answers,examples_predictions)
    print weights
    return weights
