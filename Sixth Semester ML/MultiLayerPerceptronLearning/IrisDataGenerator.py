"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# Uses sklearn to create iris data and target files
# python IrisdataGenerator.py

# To run the original program
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8


from sklearn import datasets
examples=datasets.load_iris()
# size of iris dataset is 150 and contains three classes of each 50 examples in an order
trdf=open('TrainingData.txt','w')
trtf=open('TrainingTarget.txt','w')
tedf=open('TestingData.txt','w')
tetf=open('TestingTarget.txt','w')

for i in range(0,45):
    trdf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    trtf.write(str(examples.target[i])+"\n")

for i in range(45,50):
    tedf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    tetf.write(str(examples.target[i])+"\n")

for i in range(50,95):
    trdf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    trtf.write(str(examples.target[i])+"\n")

for i in range(95,100):
    tedf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    tetf.write(str(examples.target[i])+"\n")

for i in range(100,145):
    trdf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    trtf.write(str(examples.target[i])+"\n")

for i in range(145,150):
    tedf.write(str(examples.data[i][0])+"\t"+str(examples.data[i][1])+"\t"+str(examples.data[i][2])+"\t"+str(examples.data[i][3])+"\n")
    tetf.write(str(examples.target[i])+"\n")

trdf.close()
trtf.close()
tedf.close()
tetf.close()

print "All operations done!"
