#!/bin/usr/python
'''
Author: SaiKumar Immadi
Basic DBSCAN clustering algorithm written in python
5th Semester @ IIIT Guwahati
'''

# You can use this code for free. Just don't plagiarise it for your lab assignments

import sys
from math import sqrt
from random import randint
import matplotlib.pyplot as plt

def main(argv):
    global e,mainList,minPts,clusters,outliers
    mainList=[]
    clusters=[]
    outliers=[]
    if(len(argv)!=3):
        print "The Format is <dbscan.py minPts e data.txt>"
        return 0
    minPts=int(argv[0])
    e=float(argv[1])
    if(minPts<2 or e<=0):
        print "minPts should be greater than or equal to 2"
        print "e should be greater than 0"
        return 0
    filename=argv[2]
    file=open(filename,"r")
    for line in file:
        lineStripped=line.strip().split('\t')
        mainList.append((float(lineStripped[0]),float(lineStripped[1])))
    file.close()
    while(len(mainList)>0):
        point=mainList.pop(0)
        mainEneigh=calcEneigh(point,1,[])
        outEneigh=calcEneigh(point,2,[])
        if(len(mainEneigh+outEneigh)>=minPts):
            cluster=calcCluster(point)
            clusters.append(cluster)
        else:
            outliers.append(point)
    fig=plt.figure()
    cluster_count=0
    for cluster in clusters:
        cluster_count+=1
        x_coordinates=[]
        y_coordinates=[]
        for point in cluster:
            x_coordinates.append(point[0])
            y_coordinates.append(point[1])
        label_name="Cluster : %.d" % (cluster_count)
        plt.scatter(x_coordinates,y_coordinates,s=5,label=label_name)
    x_out_coordinates=[]
    y_out_coordinates=[]
    for outlier in outliers:
        x_out_coordinates.append(outlier[0])
        y_out_coordinates.append(outlier[1])
    plt.scatter(x_out_coordinates,y_out_coordinates,s=5,label='outliers')
    plt.title('DBSCAN Clustering')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    fig.savefig('output.jpg')
    print len(clusters),"clusters"
    plt.show()
    return 0

def calcEneigh(p,opt,optList):
    global e,mainList,minPts,clusters,outliers
    if(opt==1):
        list=mainList
    elif(opt==2):
        list=outliers
    elif(opt==3):
    	list=optList
    eneigh=[]
    for point in list:
        x1=p[0]
        y1=p[1]
        x2=point[0]
        y2=point[1]
        dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if(dist<=e):
            eneigh.append(point)
    return eneigh

def calcCluster(p):
    global e,mainList,minPts,clusters,outliers
    cluster=[]
    tempList=[]
    tempList.append(p)
    while(len(tempList)>0):
        point=tempList.pop(0)
        mainEneigh=calcEneigh(point,1,[])
        outEneigh=calcEneigh(point,2,[])
        clusterEneigh=calcEneigh(point,3,cluster+tempList)
        cluster.append(point)
        for x in mainEneigh:
            mainList.remove(x)
        for x in outEneigh:
            outliers.remove(x)
        if(len(mainEneigh+outEneigh+clusterEneigh)>=minPts):
            tempList=tempList+mainEneigh+outEneigh
        else:
            cluster=cluster+mainEneigh+outEneigh
    return cluster

if __name__ == "__main__":
    main(sys.argv[1:])
