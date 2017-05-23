# -*- coding: utf-8 -*-
"""

This script combines all the data files from each run of Pythia. It is important
to rename the runs as simply Hn with no file extension, with n being intergers from 1
to N , the total number of files to combine.
"""
import numpy as np

#lcmbr listcombiner opens a file, reads each line into a list and appends it to oldlist
def lcmbr(filename,oldlist):
    newfilename = "H"+str(filename)
    file = open(newfilename,"r")
    dataset=file.readlines()
    file.close()
    dataset=dataset[143:]
    return (oldlist+dataset)

#initializing variables
data =[] 
data1=[] 
n    =1

#for loop to add all the files to the data list
while n < 2:
    data=lcmbr(n,data)
    n=n+1


#This removes any rows that are not data but artifacts of pythia
for i in data:
    j=np.fromstring(i,sep="\t")
    if len(j) ==21:
        data1.append(j)
    
#converting into a numpy array and saving
data2=np.array(data1)
np.savetxt("datasetH.csv",data2,delimiter=",",fmt="%1.3f") 
"""
IMPORTANT

The data is saved in a np.array of dimensions 21xN where N is the amount of data
the columns represent the following
eta pT phi px py pz E
that makes 7 variables for b, bbar and the parent H in order. 
"""