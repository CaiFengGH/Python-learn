"""
function:sklearn中估计器/转换器/流水线等概念
@author: Ethan
"""

import numpy as np
import csv

#1-读取数据
reader = csv.reader(open('F:\lzw\data\ionosphere.data.csv','r'))
X = np.zeros((351,34),dtype='float')
y = np.zeros((351,),dtype='bool')

#enumerate可以获取行号
for i,row in enumerate(reader):
    row_data = [float(data) for data in row[:-1]]
    X[i] = row_data
    y[i] = row[-1] == 'g'
    
#2-构建训练集和测试集
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.8,random_state=14)

#3-使用KNN进行训练
from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()

#4-进行训练和测试
estimator.fit(X_train,y_train)
y_predict = estimator.predict(X_test)

accuracy = np.mean(y_test == y_predict) * 100

#5-交叉检验解决一次性训练问题
#默认方法切分数据集,避免某些子数据集类别分布失衡问题
from sklearn.cross_validation import cross_val_score
score = cross_val_score(estimator,X,y,scoring='accuracy')
average_accuracy = np.mean(score) * 100

#6-调参之K的选取
avg_scores = []
all_scores = []
k_values = np.arange(1,21)
for k in k_values:
    estimator = KNeighborsClassifier(n_neighbors = k)
    scores = cross_val_score(estimator,X,y,scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)

#7-使用matplotlib画图观看k的影响
import matplotlib.pyplot as plt
plt.plot(k_values,avg_scores,'-o')

