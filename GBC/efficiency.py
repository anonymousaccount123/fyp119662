#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


import numpy as np
from sklearn.ensemble import GradientBoostingClassifier as GBC
import time
import matplotlib.pyplot as plt

data_train = np.loadtxt( "/home/XXXX/Desktop/XXX/raw data/training.csv", delimiter=",")

np.random.seed(9001)

#Assigning a random split
r=np.random.rand(data_train.shape[0])
#cent is the cutoff, so 0.9 will use 90% of th data for training, last 10% for validation
cent=0.75


"""
Splitting the dataset into 4, 25% testing, 75% training in different arrangments for cross validation.
"""
Y_TRAIN = data_train[int(round(len(data_train)/4)):,21]
X_TRAIN = data_train[int(round(len(data_train)/4)):,0:12]
Y_VALID = data_train[:int(round(len(data_train)/4)),21]
X_VALID = data_train[:int(round(len(data_train)/4)),0:12]

Y2_TRAIN = np.concatenate((data_train[:int(round(len(data_train)/4)),21],data_train[int(round(len(data_train)/2)):,21])) 
X2_TRAIN = np.concatenate((data_train[:int(round(len(data_train)/4)),0:12],data_train[int(round(len(data_train)/2)):,0:12])) 
Y2_VALID = data_train[int(round(len(data_train)/4)):int(round(len(data_train)/2)),21]
X2_VALID = data_train[int(round(len(data_train)/4)):int(round(len(data_train)/2)),0:12]

Y3_TRAIN = np.concatenate((data_train[:int(round(len(data_train)/2)),21],data_train[int(round(len(data_train)*0.75)):,21])) 
X3_TRAIN = np.concatenate((data_train[:int(round(len(data_train)/2)),0:12],data_train[int(round(len(data_train)*0.75)):,0:12]))
Y3_VALID = data_train[int(round(len(data_train)/2)):int(round(len(data_train)*0.75)),21]
X3_VALID = data_train[int(round(len(data_train)/2)):int(round(len(data_train)*0.75)),0:12]

Y4_TRAIN = data_train[:int(round(len(data_train)/4)),21]
X4_TRAIN = data_train[:int(round(len(data_train)/4)),0:12]
Y4_VALID = data_train[int(round(len(data_train)/4)):,21]
X4_VALID = data_train[int(round(len(data_train)/4)):,0:12]
print ("Dataset separated")

"""
Defining the funciton which calculates efficiency and purity.
"""
def efficiencycalc(test_data,out_data):
    truesig=0
    trueback=0
    falsesig=0
    falseback=0
    sig=0
    for n,i in enumerate(test_data):
        if i == 1 and out_data[n] == True:
            truesig=truesig+1
            sig=sig+1
        elif i == 0 and out_data[n]==True:
            falsesig=falsesig+1
        elif i == 0 and out_data[n]==False:
            trueback=trueback+1
        else:
            falseback=falseback+1
            sig=sig+1
    efficiency=truesig/(sig)
    purity=truesig/(truesig+falsesig)
    return (efficiency,purity)





data_test = np.loadtxt( "/home/XXX/Desktop/XXX/raw data/test.csv", delimiter=",")

X_TEST = data_test[:,0:12]

print ("Starting Grid-search")
"""
Original iteration:
    estimators 40, 60 , 5
    maxdepth 3 , 6 , 1
    minsamples 450, 500, 50
    pcuts 70,95,5

"""
estimators=np.arange(55,71,5)
maxdepth=np.arange(4,5,1)
minsamples=np.arange(450,451,1)
pcuts=np.arange(40,75,5)
efficiency=[]
purity=[]
length=len(estimators)*len(maxdepth)*len(minsamples)*len(pcuts)
number=0
start = time.time()
for estimator in estimators:
    for depth in maxdepth:
        for sample in minsamples:
            for percentile in pcuts:
                number=number+1
                gbc = GBC(n_estimators=estimator , max_depth = depth, min_samples_leaf=sample,max_features=12)
                gbc.fit(X_TRAIN,Y_TRAIN)
                prediction_TRAIN= gbc.predict_proba(X_TRAIN)
                prediction_TEST= gbc.predict_proba(X_VALID)[:,1]
                pcut= np.percentile(prediction_TRAIN,percentile)
                out_data      = list(prediction_TEST > pcut)
                test_data= Y_VALID
                eff1,pur1=efficiencycalc(test_data,out_data)
                print ("run 1 of 4")
                gbc = GBC(n_estimators=estimator , max_depth = depth, min_samples_leaf=sample,max_features=12)
                gbc.fit(X2_TRAIN,Y2_TRAIN)
                prediction_TRAIN= gbc.predict_proba(X2_TRAIN)
                prediction_TEST= gbc.predict_proba(X2_VALID)[:,1]
                pcut= np.percentile(prediction_TRAIN,percentile)
                out_data      = list(prediction_TEST > pcut)
                test_data= Y2_VALID
                eff2,pur2=efficiencycalc(test_data,out_data)
                print ("run 2 of 4")
                gbc = GBC(n_estimators=estimator , max_depth = depth, min_samples_leaf=sample,max_features=12)
                gbc.fit(X3_TRAIN,Y3_TRAIN)
                prediction_TRAIN= gbc.predict_proba(X3_TRAIN)
                prediction_TEST= gbc.predict_proba(X3_VALID)[:,1]
                pcut= np.percentile(prediction_TRAIN,percentile)
                out_data      = list(prediction_TEST > pcut)
                test_data= Y3_VALID
                eff3,pur3=efficiencycalc(test_data,out_data)
                print ("run 3 of 4")
                gbc = GBC(n_estimators=estimator , max_depth = depth, min_samples_leaf=sample,max_features=12)
                gbc.fit(X4_TRAIN,Y4_TRAIN)
                prediction_TRAIN= gbc.predict_proba(X4_TRAIN)
                prediction_TEST= gbc.predict_proba(X4_VALID)[:,1]   
                pcut= np.percentile(prediction_TRAIN,percentile)
                out_data      = list(prediction_TEST > pcut)
                test_data= Y4_VALID
                eff4,pur4=efficiencycalc(test_data,out_data)
                print ("run 4 of 4")
                feff=(eff1+eff2+eff3+eff4)/4
                fpur=(pur1+pur2+pur3+pur4)/4
                fcsv=open("Efficiency_scatter.csv","a")
                fcsv.write(str(feff)+","+str(fpur)+","+str(estimator)+","+str(depth)+","+str(sample)+","+str(percentile)+"\n")
                fcsv.close()
        print ("Run "+str(number) +" out of " +str(length))
        end=time.time()
        eta=length*((end-start)/number)-(end-start)
        print ("Time remaining lower estimate: " + str(eta))
plt.scatter(efficiency,purity)
plt.show()
