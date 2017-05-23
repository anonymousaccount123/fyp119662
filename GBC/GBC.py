# -*- coding: utf-8 -*-
"""

"""

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier as GBC
from matplotlib import pyplot as plt
import pandas as pd

data_train = np.loadtxt( "/home/XXX/Desktop/XXX/raw data/training.csv", delimiter=",")

np.random.seed(9001)

r=np.random.rand(data_train.shape[0])

#cent is the cutoff, so 0.9 will use 90% of th data for training, last 10% for validation
cent=0.9

"""
Y= truth
X= Data
"""
print ("data loaded")
Y_TRAIN = data_train[:,21]
X_TRAIN = data_train[:,0:12]

print ("data loaded")
#Original were 50, 5 , 200 , 10 , 1
gbc = GBC(n_estimators=70 , max_depth = 4, min_samples_leaf=450 ,max_features=12, verbose=1)
print ("data loaded")
gbc.fit(X_TRAIN,Y_TRAIN)
prediction_TRAIN= gbc.predict_proba(X_TRAIN)[:,1]

pcut= np.percentile(prediction_TRAIN,50)

data_test = np.loadtxt( "/home/XXX/Desktop/XXX/raw data/test.csv", delimiter=",")

X_TEST = data_test[:,0:12]
I_TEST = range(0,X_TEST.shape[0])

prediction_TEST= gbc.predict_proba(X_TEST)[:,1]
Label_TEST     = list(prediction_TEST > pcut)
prediction_TEST= list(prediction_TEST)
label_TEST     = list(prediction_TEST > pcut)
label_TRAIN    = list(prediction_TRAIN >pcut)
results=[]

for i in range(len(I_TEST)):
    results.append([int(I_TEST[i]), prediction_TEST[i], "1"*(Label_TEST[i]==1.0)+"0"*(Label_TEST==0.0)])
    
results=sorted(results,key=lambda a_entry:a_entry[1])

for i in range(len(results)):
    results[i][1]=i+1
results=sorted(results,key=lambda a_entry:a_entry[0])

fcsv= open("Prediction_output.csv","w")
fcsv.write("Number,Rank Order,Classification\n")
for line in results:
    theline = str(line[0])+","+str(line[1])+","+line[2]+"\n"
    fcsv.write(theline)
fcsv.close()


#The plotting script is below
Classifier_training_S = gbc.predict_proba(X_TRAIN[Y_TRAIN>0.5])[:,1].ravel()
Classifier_training_B = gbc.predict_proba(X_TRAIN[Y_TRAIN<0.5])[:,1].ravel()
Classifier_testing_A = gbc.predict_proba(X_TEST)[:,1].ravel()
  
c_max = max([Classifier_training_S.max(),Classifier_training_B.max(),Classifier_testing_A.max()])
c_min = min([Classifier_training_S.min(),Classifier_training_B.min(),Classifier_testing_A.min()])
  
Histo_training_S = np.histogram(Classifier_training_S,bins=50,range=(c_min,c_max))
Histo_training_B = np.histogram(Classifier_training_B,bins=50,range=(c_min,c_max))
Histo_testing_A = np.histogram(Classifier_testing_A,bins=50,range=(c_min,c_max))
AllHistos= [Histo_training_S,Histo_training_B]
h_max = max([histo[0].max() for histo in AllHistos])*1.2
h_min = max([histo[0].min() for histo in AllHistos])


bin_edges = Histo_training_S[1]
bin_centers = ( bin_edges[:-1] + bin_edges[1:]  ) /2.
bin_widths = (bin_edges[1:] - bin_edges[:-1])
  
ErrorBar_testing_A = np.sqrt(Histo_testing_A[0])

  

ax1 = plt.subplot(111)
ax1.bar(bin_centers-bin_widths/2.,Histo_training_B[0],facecolor='red',linewidth=0,width=bin_widths,label='B (Train)',alpha=0.5)
ax1.bar(bin_centers-bin_widths/2.,Histo_training_S[0],bottom=Histo_training_B[0],facecolor='blue',linewidth=0,width=bin_widths,label='S (Train)',alpha=0.5)
 
#ff = (1.0*(sum(Histo_training_S[0])+sum(Histo_training_B[0])))/(1.0*sum(Histo_testing_A[0]))
 

ax1.axvspan(pcut, c_max, color='blue',alpha=0.08)
ax1.axvspan(c_min,pcut, color='red',alpha=0.08)
ax1.axis([c_min, c_max, h_min, h_max])

plt.title("Higgs Signal-Background Separation")
plt.xlabel("Probability of classification as Signal")
plt.ylabel("Frequency")
legend = ax1.legend(loc='upper center', shadow=True,ncol=2)
for alabel in legend.get_texts():
            alabel.set_fontsize('small')
plt.savefig("Sklearn_gbc.png",dpi=150)
#plt.close()

test_data = pd.read_csv("/home/XXX/Desktop/XXX/raw data/test.csv")
#out_data  = pd.read_csv("/home/michal/Desktop/michalproject/GBC/Prediction_output.csv")
test_data= test_data.as_matrix()
#out_data = out_data.as_matrix()
test_data=data_train[:,[21]]


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

pcuts=np.arange(40,100,1)
effs=[]
purs=[]
for i in pcuts:
    pcut= np.percentile(prediction_TRAIN,i)
    label_TEST=list(prediction_TEST >pcut)
    eff,pur=efficiencycalc(test_data,label_TEST)
    effs.append(eff)
    purs.append(pur)

plt.close()
plt.figure(2)

plt.plot(effs,purs)
plt.xlabel("Efficiency")
plt.ylabel("Purity")
plt.savefig("effpurityfinal.png" , dpi=175, bbox_inches="tight")

index=[0,0,0]
for n,i in enumerate(effs):
    etapur=i+purs[n]
    if etapur > (index[1]+index[2]):
        index=[n,i,purs[n]]