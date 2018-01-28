"""
function:特征选择
@author: Ethan
"""
import pandas as pd
import numpy as np

#1-加载数据
adult = pd.read_csv(open('F:\lzw\data\\adult.data.csv','r'),header=None,
                    names=['Age','Work-Class','fnlwgt','Education','Education-Num',
                           'Marital-Status','Occupation','Relationship','Race','Sex',
                           'Capital-gain','Capital-loss','Hours-per-week','Native-Country','Earing-Raw'])
# print(adult)

#2-特征抽取环节：模型简化现实的表述
# 数值/类别 连续/离散 序数等
adult['LongHours'] = adult['Hours-per-week'] > 40

#3-特征测试，删除特征值的方差达不到最低标准的特征,不包含具有区别意义的信息
arr = np.arange(30).reshape((10,3))
arr[:,1] = 1

from sklearn.feature_selection import VarianceThreshold
vt = VarianceThreshold()
arrt = vt.fit_transform(arr)
# print(arrt)

#4-选择最佳特征：卡方
X = adult[['Age','Education-Num','Capital-gain','Capital-loss','Hours-per-week']].values
#注意此处为' >50K',注意前面的空格
y = adult['Earing-Raw'] == ' >50K'
#Series转化为一维数组
y = y.values

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
transform = SelectKBest(score_func=chi2,k=3)

Xt_chi2 = transform.fit_transform(X,y)

#4-选择最佳特征：皮尔逊
from scipy.stats import pearsonr

#注意pearsonr中第一个参数是一维数组
def multivariate_pearsonr(X,y):
    scores,pvalues = [],[]
    for column in range(X.shape[1]):
        cur_score,cur_p = pearsonr(X[:,column],y)
        scores.append(abs(cur_score))
        pvalues.append(cur_p)
        
    return (np.array(scores),np.array(pvalues))

transform = SelectKBest(score_func=multivariate_pearsonr,k=3)   
Xt_pearsonr = transform.fit_transform(X,y)

#不同的计算方法，特征和类别的关系是不同的
