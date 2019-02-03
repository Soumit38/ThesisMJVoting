# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:34:46 2019

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import median


def pre_process(X, y):
    def is_float(input):
      try:
        num = float(input)
      except ValueError:
        return False
      return True
    
    for i in range(0,X.shape[0]):
        if y[i] == 'ckd':
            y[i] = 1
        else:
            y[i] = 0
    y = y.astype(int)
    
    for a in range(0, X.shape[0]):
        if X[a][5] == 'normal':
            X[a][5] = 0
        if X[a][5] == 'abnormal':
            X[a][5] = 1
            
    for a in range(0, X.shape[0]):
        if X[a][6] == 'normal':
            X[a][6] = 0
        if X[a][6] == 'abnormal':
            X[a][6] = 1
            
    for a in range(0, X.shape[0]):
        if X[a][7] == 'notpresent':
            X[a][7] = 0
        if X[a][7] == 'present':
            X[a][7] = 1
            
    for a in range(0, X.shape[0]):
        if X[a][8] == 'notpresent':
            X[a][8] = 0
        if X[a][8] == 'present':
            X[a][8] = 1
            
    for a in range(0, X.shape[0]):
        for b in range(18, 24):
            if X[a][b] == 'yes' or X[a][b] == 'good':
                X[a][b] = 0
            if X[a][b] == 'no' or X[a][b] == 'poor':
                X[a][b] = 1
        
    for a in range(0,X.shape[0]):
        for b in range(0, 24):
            if(isinstance(X[a][b], int)):
                X[a][b] = float(X[a][b])
            elif(isinstance(X[a][b], str)):
                if(is_float(X[a][b])):
                    X[a][b] = float(X[a][b])
                    
    totals = [0] * 24
    added = [0] * 24           
    for a in range(0, X.shape[0]):
        for b in range(0, 24):
            if(isinstance(X[a][b], float)):
                totals[b] += X[a][b]
                added[b] += 1
                
    averages = [0] * 24          
    for a in range(0, 24):
        averages[a] = totals[a] / added[a]
     
    c = 0
    for a in range(0, X.shape[0]):
        for b in range(0, 24):
            if(isinstance(X[a][b], float) == 0):
                X[a][b] = averages[b]
                c += 1
        
    X = X.astype(float)
    
    return X
