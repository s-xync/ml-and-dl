"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
def readfile(filename,num_features,option):
    ifile=open(filename,'r')
    if option==1:#training file
        examples_features=[]
        examples_answers=[]
        #if num_features is 3, then examples_features has 3 lists inside
        for i in range(0,num_features+1):
            examples_features.append([])
        #reading the training data
        for example_line in ifile:
            example=[numbers for numbers in example_line.split("\t") if numbers is not ""]
            example.insert(0,1)
            for i in range(0,num_features+1):
                examples_features[i].append(float(example[i]))
            examples_answers.append(float(example[num_features]))
        ifile.close()
        return examples_features,examples_answers
    elif option==2:#testing file
        testing_features=[]
        #if num_features is 3, then testing_features has 3 lists inside
        for i in range(0,num_features+1):
            testing_features.append([])
        #reading the training data
        for test_line in ifile:
            test=[numbers for numbers in test_line.split("\t") if numbers is not ""]
            test.insert(0,1)
            for i in range(0,num_features+1):
                testing_features[i].append(float(test[i]))
        ifile.close()
        return testing_features
