# -*- coding: utf-8 -*-


import numpy as np
data = np.array(np.genfromtxt("/home/michal/Desktop/michalproject/raw data/datasetH.csv",delimiter=","))
data=data[0::10]
np.savetxt("datasetHss.csv",data,delimiter=",",fmt="%1.3f") 