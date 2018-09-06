"""
**  Author : SaiKumar Immadi
**  MultiLayer Perceptron Learning
"""
# Uses Python 2
# Uses covtypeclean.csv file to create data files and target files
# python BigDataGenerator.py

# To run the original program
# python Init.py TrainingData.txt TrainingTarget.txt TestingData.txt TestingTarget.txt
# optimal inputs for the given dataset 0.001, 10000, 1, 8
import random
import sys
random.seed(1)
datafile=open('covtypeclean.csv','r')
trdf=open('TrainingData.txt','w')
trtf=open('TrainingTarget.txt','w')
tedf=open('TestingData.txt','w')
tetf=open('TestingTarget.txt','w')
fulldatalist=[]
for line in datafile:
    fulldatalist.append(line.strip().split(','))
    assert len(fulldatalist[-1])==11
datafile.close()
# datasetsize=len(fulldatalist)
datasetsize=500
fulldatalist=random.sample(fulldatalist,datasetsize) #shuffling
features=[]
targets=[]
for i in range(0,(len(fulldatalist[-1])-1)):
    features.append([])
for i in range(0,len(fulldatalist)):
    for j in range(0,(len(fulldatalist[-1])-1)):
        features[j].append(float(fulldatalist[i][j]))
    targets.append(int(fulldatalist[i][-1]))
# for i in range(0,len(features)):
#     print len(features[i])
# print len(targets)
# sys.exit()
for i in range(0,len(features)):
    meanvalue=sum(features[i])/float(len(features[i]))
    maxvalue=max(features[i])
    minvalue=min(features[i])
    rangevalue=maxvalue-minvalue
    for j in range(0,len(features[i])):
        features[i][j]=(features[i][j]-rangevalue)/meanvalue #normalising

training_sample_size=len(fulldatalist)*90//100
test_sample_size=len(fulldatalist)-training_sample_size

for i in range(0,training_sample_size):
    for j in range(0,len(features)):
        if j==0 and i==0:
            trdf.write(str(features[j][i]))
        elif j==0 and i>0:
            trdf.write("\n"+str(features[j][i]))
        else:
            trdf.write("\t"+str(features[j][i]))
    trtf.write(str(targets[i])+"\n")

for i in range(training_sample_size,training_sample_size+test_sample_size):
    for j in range(0,len(features)):
        if j==0 and i==training_sample_size:
            tedf.write(str(features[j][i]))
        elif j==0 and i>training_sample_size:
            tedf.write("\n"+str(features[j][i]))
        else:
            tedf.write("\t"+str(features[j][i]))
    tetf.write(str(targets[i])+"\n")

trdf.close()
trtf.close()
tedf.close()
tetf.close()
print "All operations done!"
