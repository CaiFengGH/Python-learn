"""
referrence:利用Python进行数据分析
@author: Ethan
"""
import numpy as np

#数组生成
data1 = [1,2,3,4]
arr1 = np.array(data1)

#数组的大小和类型
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2.shape
arr2.dtype

#其他类型的数组
arr3 = np.zeros([2,3])
arr4 = np.empty([2,2])

#数组类型的转换
arr5 = np.arange(5)
arr5_1 =arr5.astype(np.float64)
arr6 = np.array([1,2,3],dtype=np.string_)
arr6_1 = arr6.astype(np.float32)

#数组与数组及标量运算，针对元素级别
arr7 = np.array([[1,2,3],[4,5,6]])
arr7_1 = arr7 * arr7
arr7_2 = arr7_1 + 1

#数组切片书原始数组的视图，数据不会被复制，视图的修改都会直接反应到原数组上
arr8 = np.arange(10)
arr8[5:8] = 12
arr8_1 = arr8[5:8]
arr8_1[0] = 11

#多维数组的使用,copy和视图进行比较
arr9 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
old_value1 = arr9[1].copy()
arr9[1] = 22
arr9[1] = old_value1

#花式索引,将数据复制到新数组
arr_0 = np.arange(32).reshape((8,4))
#取出对应行列的数组
arr_0[[1,5,7,2],[0,3,1,2]]
#取出对应行的数据,并按照顺序进行排列
arr_0[[1,5,7,2]][:,[0,3,1,2]]
arr_0[np.ix_([1,5,7,2],[0,3,1,2])]

#数组的转置与內积
arr_1 = np.random.rand(6,3)
np.dot(arr_1.T,arr_1)

#数组的常永刚函数
arr_2 = np.arange(10)
np.sqrt(arr_2)
np.exp(arr_2)
x = np.random.rand(8)
y = np.random.rand(8)
np.maximum(x,y)

#np.where的使用方法
arr_3 = np.random.rand(4,4)
np.where(arr_3 > 0.5,1,arr_3)

#基本的统计函数
arr_4 = np.random.randn(5,4)
arr_4.mean(axis=1)

