"""
**  Author : SaiKumar Immadi
**  Linear Regression Using Gradient Descent
"""
import random
x1=[]
random.seed(5000)
for i in range(0,5000):
    x1.append(random.randint(1,20))
x2=[]
random.seed(5001)
for i in range(0,5000):
    x2.append(random.randint(1,20))
x3=[]
random.seed(5002)
for i in range(0,5000):
    x3.append(random.randint(1,20))
x4=[]
random.seed(5003)
for i in range(0,5000):
    x4.append(random.randint(1,20))
y=[]
for i in range(0,5000):
    #equation
    # y = 3 * x1 + 5 * x2 - 2 * x3
    # y.append(5 * x1[i])
    y.append(0.3 * x1[i] + 0.5 * x2[i] + 0.9 * x3[i])
    # y.append(0 * x1[i] + 0.4 * x2[i] + 0.3 * x3[i] + 0.2 * x4[i])

f=open('TrainingData.txt','w')
for i in range(0,2000):
    # f.write(str(x1[i])+"\t"+str(y[i])+"\n")
    f.write(str(x1[i])+"\t"+str(x2[i])+"\t"+str(x3[i])+"\t"+str(y[i])+"\n")
    # f.write(str(x1[i])+"\t"+str(x2[i])+"\t"+str(x3[i])+"\t"+str(x4[i])+"\t"+str(y[i])+"\n")
f.close()

f=open('TestingData.txt','w')
for i in range(2000,2200):
    # f.write(str(x1[i])+"\n")
    f.write(str(x1[i])+"\t"+str(x2[i])+"\t"+str(x3[i])+"\n")
    # f.write(str(x1[i])+"\t"+str(x2[i])+"\t"+str(x3[i])+"\t"+str(x4[i])+"\n")
f.close()

f=open('TestingDataAnswers.txt','w')
for i in range(2000,2200):
    f.write(str(y[i])+"\n")
f.close()

print "All operations done!"
