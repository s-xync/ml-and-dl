"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
def Predict(weights,examples_features):
    num_features=len(weights)
    num_examples=len(examples_features[0])
    predictions=[]
    for i in range(0,num_examples):
        predictions.append(0)

    for i in range(0,num_examples):
        for j in range(0,num_features):
            predictions[i]=predictions[i]+(weights[j]*examples_features[j][i])
    return predictions
