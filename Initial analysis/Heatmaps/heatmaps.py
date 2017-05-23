#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


import numpy as np
import matplotlib.pyplot as plt


datag = np.array(np.genfromtxt("/home/XXX/Desktop/XXX/raw data/dataset.csv",delimiter=","))
datah = np.array(np.genfromtxt("/home/XXX/Desktop/XXX/raw data/datasetHs.csv",delimiter=","))
print ("Data imported succesfully")

plt.figure(1)

x=datag[:,[0]]
y=datag[:,[2]]
heatmap, xedges, yedges = np.histogram2d(x[:,0],y[:,0],bins=50)
extent=[xedges[0],xedges[-1],yedges[0],yedges[-1]]
plt.clf()
plt.imshow(heatmap.T,extent=extent, origin='lower')
plt.title(r"$\eta$ and $\phi$ heatmap plot of b for $g\rightarrow b\bar b")
plt.xlabel(r"$\eta$")
plt.ylabel(r"$\phi$")
#plt.show()
plt.savefig("Gbb etaphi plot.png" , dpi=175, bbox_inches="tight")
plt.close(1)
         
print (len(x))

plt.figure(2)
x=datah[:,[0]]
y=datah[:,[2]]
heatmap, xedges, yedges = np.histogram2d(x[:,0],y[:,0],bins=50)
extent=[xedges[0],xedges[-1],yedges[0],yedges[-1]]
plt.clf()
plt.imshow(heatmap.T,extent=extent, origin='lower')
plt.title(r"$\eta$ and $\phi$ heatmap plot of b for $H\rightarrow b\bar b")
plt.xlabel(r"$\eta$")
plt.ylabel(r"$\phi$")
#plt.show()
plt.savefig("Hbb etaphi plot.png" , dpi=175, bbox_inches="tight")
plt.close(2)
print (len(x))
