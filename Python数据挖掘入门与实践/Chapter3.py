"""
function:CART树
@author: Ethan
"""
import pandas as pd
import numpy as np

#1-读取数据集
dataset = pd.read_csv(open('F:\lzw\data\nba2013-2014.data.csv','r'),parse_dates=['Date'],skiprows=[0,])
#原始数据预处理环节
dataset.columns = ['Date','Score Type','Visitor Team','VisitorPts','Home Team','HomePts','OT?','Notes']

#2-确定类别值
dataset['HomeWin'] = dataset['VisitorPts'] < dataset['HomePts']
#pandas将类别转换为numpy数组
y = dataset['HomeWin'].values

#3-抽取特征:球队上一场比赛的胜负
from collections import defaultdict
won_last = defaultdict()

for index,row in dataset.iterrows():
    home_team = row['home_team']
    visitor_team = row['visitor_team']
    row['HomeLastWin'] = won_last[home_team]
    row['VisitorLastWin'] = won_last[visitor_team]
    dataset.ix[index] = row
    #更新won_last,第一行数据中主客队均认为失败
    won_last[home_team] = row['HomeWin']
    won_last[visitor_team] = not row['HomeWin']

#4-特征抽取
X_previouswins = dataset[['HomeLastWin','VisitorLastWin']].values

#5-实例化决策树
from sklearn.tree import DecisionTreeClassifier
cart = DecisionTreeClassifier(random_state=14)

#6-多次训练，避免单词训练失误
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(cart,X_previouswins,y,scoring='accuracy')
avg_scores = np.mean(scores)

#7-提取丰富的特征和提高训练的数据量，有助于提高预测的准确率
#通过13年的数据，确定球队的水平
#通过比较两队上一次相遇时的胜负情况
#增加新的数据量，提高训练的准确度

