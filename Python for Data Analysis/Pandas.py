"""
referrence:利用Python进行数据分析
@author: Ethan
"""

from pandas import DataFrame,Series
import pandas as pd
import numpy as np

#构建DataFrame,可以指定列和索引
data = {'state':['good','bad','good'],'year':[1994,1995,1996]}
DataFrame(data,columns=['year','state'])
df = DataFrame(data,columns=['year','state','date'],index=['one','two','three'])

#访问DataFrame的索引对象、列信息
df.index
df.columns
df['year']
df.year
df.ix['one']

#对DataFrame的列赋值时,长度需要匹配
df['date'] = np.arange(5)#长度为5，不匹配发生错误
df['date'] = np.arange(3)

#删除指定列信息
del df['date']

#索引对象
obj = Series(np.arange(3),index=['a','b','c'])
index = obj.index
index[1:]
#索引对象的不可更改性质
index[1] = 'd'

index = pd.Index(np.arange(3))
obj2 = Series([1,2,3],index = index)
obj2.index is index

#重新索引
frame = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Ohio','Texas','California'])
frame2 = frame.reindex(['a','b','c','d'])
states = ['Texas','Utah','California']
frame2.reindex(columns = states)
#插值只适合于行
frame.reindex(index=['a','b','c','d'],method='ffill',columns=states)
#重新索引任务变得简洁
frame.ix[['a','b','c','d'],states]

#Series对象的切片和访问
obj = Series(np.arange(4.0),index=['a','b','c','d'])
obj[2:4]
obj['b':'d']
obj[[1,3]]
obj[obj < 2]
obj['b':'c'] = 5

#DataFrame的切片和访问,注意行和列的不同，及切片范围的差异
data = np.arange(16).reshape((4,4))
df = DataFrame(data,index=['a','b','c','d'],columns=['one','two','three','four'])
df['two']
df.ix['a']
df[:2]
df[df['three']>5]
df < 5
df[df < 5] = 0
df.ix[['a','d'],[3,0,1]]
df.ix[2]
df.ix[2:3]
df.ix[:'c','two']









