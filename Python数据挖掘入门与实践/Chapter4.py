"""
function:Apriori
@author: Ethan
"""
import pandas as pd

#1-加载数据
all_ratings = pd.read_csv(open('F:\lzw\data\m100k.data.csv','r'),delimiter='\t',header=None,names=['UserId','MovieId','Rating','DateTime'])
#时间戳数据转换为日期形式

#2-确定用户是否喜欢某一部电影
all_ratings['Favorable'] = all_ratings['Rating'] > 3

#3-选取部分数据，有效减少搜索空间
ratings = all_ratings[all_ratings['UserId'].isin(range(200))]

#4-新建数据集，仅保留用户喜欢电影的数据行
favorable_ratings = ratings[ratings['Favorable']]   

#5-确定每个用户喜欢哪些电影
favorable_reviews_by_users = {}
for k,v in favorable_ratings.groupby('UserId')['MovieId']:
    favorable_reviews_by_users[k] = frozenset(v.values)

#6-确定每部电影的影迷数量
num_favorable_by_movie = ratings[['MovieId','Favorable']].groupby('MovieId').sum()
num_favorable_by_movie.sort('Favorable',ascending=False)
print(num_favorable_by_movie)

#以上为数据预处里环节
#阶段一:确定频繁项集所需的最小支持度
#阶段二:根据置信度选择关联规则

