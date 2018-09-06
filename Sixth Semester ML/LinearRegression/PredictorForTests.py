"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
def PredictTests(weights,testing_features,outputfilename):
    num_features=len(weights)
    num_tests=len(testing_features[0])
    predictions=[]
    for i in range(0,num_tests):
        predictions.append(0)

    for i in range(0,num_tests):
        for j in range(0,num_features):
            predictions[i]+=weights[j]*testing_features[j][i]

    ofile=open(outputfilename,'w')
    for i in range(0,len(predictions)):
        ofile.write(str(predictions[i])+"\n")
    ofile.close()
