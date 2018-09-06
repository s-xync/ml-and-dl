"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
def calculateError(examples_answers,examples_predictions):
    if len(examples_answers)!=len(examples_predictions):
        sys.exit()
    else:
        #calculating mean sqaured error
        error=0
        for i in range(0,len(examples_answers)):
            # x=((examples_predictions[i] - examples_answers[i])*(examples_predictions[i] - examples_answers[i]))/(2.0)
            x=((examples_predictions[i] - examples_answers[i])*(examples_predictions[i] - examples_answers[i]))/(2.0*len(examples_answers))
            error += x
        return error
