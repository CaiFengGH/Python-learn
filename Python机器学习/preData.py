"""
function:数据预处理
@author: Ethan
"""

import pandas as pd
from io import StringIO
import numpy as np
from sklearn.preprocessing import Imputer

##1-缺失值处理
# 初始化csv数据
csv_data='''A,B,C,d
1.0,2.0,3.0,4.0
5.0,6.0,,8.0
0.1,11.0,12.0,'''
csv_data = unicode(csv_data)

# pd读取csv数据
df = pd.read_csv(StringIO(csv_data))
# 计算每列的空缺值个数
df.isnull().sum()
# 将DataFrame输出为矩阵形式
df.values
# 去除有空缺值的行，参数为1为列
df.dropna()

# 使用插值法，基于行列的均值进行填充
from sklearn.preprocessing import Imputer
imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr.fit(df)
imputed_data = imr.transform(df.values)
print(imputed_data)

##2- 处理分类数据
df = pd.DataFrame(['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.3,'class1'])
df.columns = ['color','size','price','classlabel']

# 映射有序特征
size_mapping = {'XL':3,'L':2,'M':1}
df['size'] = df['size'].map(size_mapping)

# 对类别进行编码
class_mapping = {label:idx for idx,label in enumerate(np.unique(df['classlabel']))}
df['classlabel'] = df['classlabel'].map(class_mapping)

# 基于LabelEncoder类实现类别编码
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)

# 对离散数据进行one—hot编码,toarray将稀疏矩阵输出为普通矩阵
X = df[['color','size','price']].values
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
ohe.fit_transform(X).toarray()

# 调用pandas的get_dummies方法创建哑特征,对字符串类型进行one-hot编码
pd.get_dummies(df[['price','color','size']])

##3-将数据集拆分成训练集和测试集
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

##4-统一特征值的取值范围
#归一化：分母为最大值和最小值的差，分子为值与最小值的差
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
#标准化：形成均值为0标准为1的分布
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
#两者区别：初始化权重时，标准化学习参数更加容易；标准化对于异常值不太敏感
