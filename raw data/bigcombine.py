#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
"""
This program takes both gluon and higgs datasets and
generates an overall set to be used for machine learning
whilst labelling them
"""
import numpy as np

gluons=np.loadtxt("dataset.csv",delimiter=",")
higgs =np.loadtxt("datasetHss.csv",delimiter=",")
for i in higgs:
    if i[1]<75:
        np.delete(higgs,i,0)
newhiggs=np.ones((len(higgs),len(higgs[1])+1))
newhiggs[:,:-1] = higgs
newgluons=np.zeros((len(gluons),len(gluons[1])+1))
newgluons[:,:-1] = gluons
finalmatrix=np.concatenate((newgluons,newhiggs))



for i in finalmatrix[:,:-1]:
    for j,n in enumerate(i):
        j=(j-min(i[:,[n]]) )/ (max(i[:,[n]]) - min(i[:,[n]]) )
        
        
        
np.random.shuffle(finalmatrix)

np.savetxt("training.csv",finalmatrix[int(round(len(finalmatrix)/5)):],delimiter=",",fmt="%1.3f")
np.savetxt("test.csv",finalmatrix[:int(round(len(finalmatrix)/5))],delimiter=",",fmt="%1.3f")
