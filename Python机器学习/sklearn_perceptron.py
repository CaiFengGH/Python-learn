# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:30:35 2018

@author: acer
"""
import numpy as np
from sklearn import datasets

# 加载数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
np.unique(y)

# 训练集和测试集
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

# 特征标准化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
# 使用训练集的标准化参数标准化测试集
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

#训练感知机
from sklearn.linear_model import Perceptron
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
y_pred = ppn.predict(X_test_std)

# 计算感知机模型的准确度
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f' % accuracy_score(y_test,y_pred))
