#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt

datag = np.array(np.genfromtxt("Efficiency_scatter.csv",delimiter=","))
"""
file = open(str("Efficiency_scatter.csv"),"r")
dataset=file.readlines()
file.close()
data1=[]
for i in dataset:
    j=np.fromstring(i,sep=",")
    data1.append(j)
"""
plt.figure(1)
plt.scatter(datag[:,0],datag[:,1])
plt.xlim(0.1,0.8)
plt.ylim(0.997,0.999)
plt.xlabel("Purity")
plt.ylabel("Efficiency")
#plt.show(1)
plt.savefig("effpurityplot.png" , dpi=175, bbox_inches="tight")
plt.close(1)
print (datag[:,[1]])

"""
Finding the parameters of the optimal point
"""
index=[0,0]

for n,i in enumerate(datag):
    etapur=i[0]+i[1]
    if etapur > index[1]:
        index=[n,etapur]
print (index)
print (datag[(index[0])])
