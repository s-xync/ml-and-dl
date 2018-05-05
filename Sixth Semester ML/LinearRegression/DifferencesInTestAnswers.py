"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
answersfile=open('TestingDataAnswers.txt','r')
predictionsfile=open('TestingDataPredictions.txt','r')
differencesfile=open('TestingDataResultDifferences.txt','w')
answers=[]
predictions=[]
accuracy=0
for line in answersfile:
    answers.append(float(line.strip()))
for line in predictionsfile:
    predictions.append(float(line.strip()))
if len(predictions)==len(answers):
    differencesfile.write("Answers - Predictions = Differences\n")
    for i in range(0,len(predictions)):
        if answers[i]>=predictions[i]:
            accuracy=accuracy+(answers[i]-predictions[i])/answers[i]
        elif answers[i]<predictions[i]:
            accuracy=accuracy-(answers[i]-predictions[i])/answers[i]
        differencesfile.write(str(answers[i])+" - "+str(predictions[i])+" = "+str(answers[i]-predictions[i])+"\n")
accuracy=1-accuracy/len(answers)
answersfile.close()
predictionsfile.close()
differencesfile.close()
print "Differences Calculated!"
print "The accuracy is",accuracy
