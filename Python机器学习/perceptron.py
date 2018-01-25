# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:37:29 2018
function:perceptron,简单分类器
@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Perceptron(object):

    # constructor
    def __init__(self,eta=0.01,n_iter=10):    
        self.eta = eta
        self.n_iter = n_iter
    
    # fit
    def fit(self,X,y):
        self.w = np.zeros(X.shape[1] + 1)
        self.errors = []
        
        for i in range(self.n_iter):
            errors = 0
            for xi,target in zip(X,y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                errors += int(update != 0)
            self.errors.append(errors)
        
        return self
        
    # net_input
    def net_input(self,X):
        return np.dot(X,self.w[1:])+self.w[0]
        
    # predict
    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0,1,-1)
    
# read data    
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None)
# label y
y = df.iloc[0:100,4].values
y = np.where(y == "Iris-setosa",-1,1)

X = df.iloc[0:100,[0,2]].values
'''
plt.scatter(X[:50,0],X[:50,1],color ='red',marker='o',label='setosa')
plt.scatter(X[50:100,0],X[50:100,1],color ='blue',marker='*',label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()
'''
# initial Perception
ppn = Perceptron(eta=0.1,n_iter=10)
ppn.fit(X,y)

plt.plot(range(1,len(ppn.errors)+1),ppn.errors,marker='o')
plt.xlabel('Epoches')
plt.ylabel('Number of misclassification')
plt.show()