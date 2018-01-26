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

#算数运算和数据对齐:Series
s1 = Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
#不是共有的索引取NaN
s1 + s2

#算数运算和数据对齐:DataFrame
data1 = np.arange(9.0).reshape((3,3))
data2 = np.arange(12.0).reshape((4,3))
df1 = DataFrame(data1,columns=['b','c','d'],index=['Ohio','Texas','Colorado'])
df2 = DataFrame(data2,columns=['b','d','e'],index=['Utah','Ohio','Texas','Oregon'])
#不是共有的取并集
df1 + df2
df2.add(df1,fill_value=0)

#DataFrame和Series间运算
data3 = np.arange(12).reshape((4,3))
df3 = DataFrame(data3,columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
s = df3.ix[0]
#进行广播运算
df3 - s

#重新索引形成并集
s1 = Series(np.arange(3),index=list('bef'))
df3 + s1

#函数应用及映射
df4 = DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
#元素级取绝对值
np.abs(df4)
func = lambda x:x.max() - x.min()
#对列进行计算
df4.apply(func)
#对行进行计算
df4.apply(func,axis=1)
#返回每列的最大值和最小值
def f(x):
    return Series([x.min(),x.max()],index=['min','max'])
df4.apply(f)

#排序，排名存在疑问
obj = Series(np.arange(4),index=['d','a','b','c'])
obj.sort_index()
obj.sort_index(axis=1)
#按照值进行排序
obj.order()

data5 = np.arange(8).reshape((2,4))
df5 = DataFrame(data5,index=['three','one'],columns=['d','a','b','c'])
df5.sort_index()
#按照行进行排序
df5.sort_index(axis=1)
df6 = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
#按照a b进行排序
df6.sort_index(by=['a','b'])

#基础统计功能
df7 = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
df7.sum()
df7.sum(axis=1)
#包含NaN的值,不进行平均值计算
df7.mean(axis=1,skipna=False)
#最大值所在的索引
df7.idxmax()
#返回累加和
df7.cumsum()
#返回多种统计集合的结果
df7.describe()

#唯一值和值计数
obj = Series(['c','a','d','a','a','b','b','c','c'])
unique = obj.unique()
obj.value_counts()
pd.value_counts(obj.values,sort=True)
mask = obj.isin(['b','c'])
obj[mask]

#缺失数据判断
data8 = Series(['a','b',np.nan,'d'])
data8.isnull()
data8[2] = None
data8.isnull()
data9 = Series([1,np.nan,2,np.nan])
#DataFrame中dropna的功能扩展
data9.dropna()
