"""
function:特征创建
@author: Ethan
"""
from collections import defaultdict
import pandas as pd
import numpy as np

#1-加载数据，数据格式处理
#将字符串转换为数值型
def convert_number(x):
    try:
        return float(x)
    except ValueError:
        return np.nan

#创建字典存储所有特征及其转换结果，把所有特征值转换为浮点型
converters = defaultdict(convert_number)

#将最后一列值转换为类别
converters[1558] = lambda x: 1 if x.strip() == 'ad.' else 0
        
ads = pd.read_csv(open('F:\lzw\data\\advertisement.data.csv','r'),
                  header=None,converters=converters,low_memory=False)

X = ads.drop(1558,axis=1).values
y = ads[1558]

#2-主成分分析:特征的方差和整体的方差没有太大的区别
#pca得到的主成分往往是其他几个特征的复杂组合
from sklearn.decomposition import PCA
pca = PCA(n_components=5)
Xd = pca.fit_transform(X)

print(pca.explained_variance_ratio_)

#3-自定义转换器
#接受一种形式的数据，输出另外一种形式的数据
