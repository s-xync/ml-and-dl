#!/bin/usr/python
'''
Author: SaiKumar Immadi
Basic K-Means clustering algorithm written in python
5th Semester @ IIIT Guwahati
'''

# You can use this code for free. Just don't plagiarise it for your lab assignments

import sys
from math import sqrt
from random import randint
import matplotlib.pyplot as plt

def main(argv):
	global mainList,klists,kmeans
	if len(argv)!=2:
		print "The Format is <kmeans.py K data.txt>"
		return 0
	k=int(argv[0])
	if(k<1):
		print "The Format is <kmeans.py K data.txt>"
		print "K value should be greater than 0"
		return 0
	filename=argv[1]
	file=open(filename,"r")
	mainList=[]
	for line in file:
		lineStripped=line.strip().split('\t')
		mainList.append((float(lineStripped[0]),float(lineStripped[1])))
	file.close()
	oldKlists=[]
	klists=[]
	kmeans=[]
	oldKmeans=[]

# intialising methods

# donot comment
	for i in range(0,k):
		klists.append([])

# make one method active and comment out remaining

# 1st method
	# tempMainMeanFindingList=list(mainList)
	# for i in range(0,k):
	# 	rand=randint(0,(len(tempMainMeanFindingList)-1))
	# 	randPoint=tempMainMeanFindingList[rand]
	# 	kmeans.append(randPoint)
	# 	tempMainMeanFindingList[:] = (value for value in tempMainMeanFindingList if value != randPoint)

# 2nd method
	# tempK=0
	# for i in range(0,len(mainList)):
	# 	klists[tempK%k].append(mainList[i])
	# 	tempK+=1;
	# kmeans=calculateKmeans()

# 3rd method
	# tempK=0
	# for i in range(0,len(mainList)):
	# 	klists[tempK%k].append(mainList[i])
	# 	tempK+=2;
	# kmeans=calculateKmeans()

# 4th method
	tempListSize=len(mainList)/k
	for i in range(0,k-1):
		klists[i]=mainList[(i)*tempListSize:(i+1)*tempListSize]
	klists[k-1]=mainList[(k-1)*tempListSize:]
	kmeans=calculateKmeans()

#end

	iterations=0
	maxIterations=100000 #cannot run while loop more than this
	while((cmp(oldKmeans,kmeans)!=0 or cmp(oldKlists,klists)!=0) and iterations<maxIterations):
		flag=0
		oldKmeans=list(kmeans)
		oldKlists=list(klists)
		#calculating clusters
		klists=[]
		for i in range(0,k):
			klists.append([])
		klists=calculateKlists()
		for i in range(0,k):
			if(len(klists[i])<1):
				flag=1
				break
		if(flag==1):
			break
		#calculating means of clusters
		kmeans=[]
		kmeans=calculateKmeans()

		iterations+=1

	kmeans=oldKmeans
	klists=oldKlists

	outputFile=open("output.txt","w")
	outputFile.write("No of iterations are %.d\n" % iterations)
	outputFile.write("The K-means are :\n")
	outputFile.write(str(kmeans))
	outputFile.write("\n\n\n")
	outputFile.write("The cluster sets are :\n")
	for i in range(0,k):
		outputFile.write("Cluster %.d :\n" % (i+1))
		outputFile.write(str(klists[i]))
		outputFile.write("\n\n\n")
	outputFile.write("\n\n")
	outputFile.write("The Main Input data is :\n")
	outputFile.write(str(mainList))
	outputFile.write("\n")
	outputFile.close()
	x_mean_coordinates=[]
	y_mean_coordinates=[]
	fig=plt.figure()
	for i in range(0,k):
		x_coordinates=[]
		y_coordinates=[]
		x_mean_coordinates.append(kmeans[i][0])
		y_mean_coordinates.append(kmeans[i][1])
		for j in range(0,len(klists[i])):
			x_coordinates.append(klists[i][j][0])
			y_coordinates.append(klists[i][j][1])
		label_name="Cluster : %.d" % (i+1)
		plt.scatter(x_coordinates,y_coordinates,s=5,label=label_name)
	plt.scatter(x_mean_coordinates,y_mean_coordinates,marker='*',color='#000000',s=30,label='K-Means')
	print "The K-means are"
	for i in range(0,k):
		print "( %.4f," % kmeans[i][0], "%.4f" % kmeans[i][1],")"
	print "Check output.txt file for further information"
	print "Saved a copy of the figure in local machine"
	plt.title('K-Means Clustering')
	plt.xlabel('x-axis')
	plt.ylabel('y-axis')
	# plt.xlim(0,250)
	# plt.ylim(0,250)
	plt.legend()
	fig.savefig('output.jpg')
	plt.show()
	return 0



def calculateKmeans():
	#Empty kmeans set is passed to this function
	#kmeans is [] for any k
	global mainList,klists,kmeans
	for i in range(0,len(klists)):
		xtotal=0.0
		ytotal=0.0
		for j in range(0,len(klists[i])):
			xtotal+=klists[i][j][0]
			ytotal+=klists[i][j][1]
		kmeans.append((xtotal/(len(klists[i])),ytotal/(len(klists[i]))))
	return kmeans

def calculateKlists():
	#Empty klists set of sets is passed to this function
	#klists is [[],[],[]] for k=3
	global mainList,klists,kmeans
	mainListSize=len(mainList)
	tempMainList=list(mainList)
	for i in range(0,mainListSize):
		tempPoint=tempMainList.pop(-1)
		tempList=[]
		for j in range(0,len(klists)):
			x1=kmeans[j][0]
			y1=kmeans[j][1]
			x2=tempPoint[0]
			y2=tempPoint[1]
			dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
			tempList.append(dist)
		klists[tempList.index(min(tempList))].append(tempPoint)
	return klists

if __name__ == "__main__":
   main(sys.argv[1:])
