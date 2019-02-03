# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:57:13 2019

@author: HP
"""
# no ckd = 0, ckd = 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import median
import pickle
#### Load the model
filename = "logistic.sav"
loaded_model = pickle.load(open(filename, 'rb'))

### Input a row
inn = pd.read_csv("input.csv")

X_in = inn.iloc[:, 0:24].values
y = inn.iloc[:, 24].values

voterlist = []
### Preprocess
from pre_pros import *
XX = pre_process(X_in, y)
## Predict the input
y_pred = loaded_model.predict(XX)
voterlist.append(int(y_pred))

print("Actual output: " +str(y))
print("Predict output: " +str(y_pred))

#### Load the model
filename = "naive_bayes.sav"
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(XX)
print("Actual output: " +str(int(y)))
print("Predict output: " +str(int(y_pred)))
voterlist.append(int(y_pred))

#### Load the model
filename = "decision_tree.sav"
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(XX)
print("Actual output: " +str(int(y)))
print("Predict output: " +str(int(y_pred)))
voterlist.append(int(y_pred))

#### Load the model
filename = "random_forest.sav"
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(XX)
print("Actual output: " +str(int(y)))
print("Predict output: " +str(int(y_pred)))
voterlist.append(int(y_pred))

#### Load the model
filename = "svm.sav"
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(XX)
print("Actual output: " +str(int(y)))
print("Predict output: " +str(int(y_pred)))
voterlist.append(int(y_pred))


print("\nVoterList : ", voterlist)
print("\nMajority voting result : ")
if(voterlist.count(1)>voterlist.count(0)):
    print("CKD")
else:
    print("not_CKD")
