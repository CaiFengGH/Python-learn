"""
Created on Mon Apr  9 14:46:18 2018
<流畅的Python2.4+5>
@author: Ethan
"""

#1-切片和区间忽略最后一个元素：；
# 快速返回元素个数
range(3)
# 后一个坐标减去前一个坐标即为切片长度
len = stop - start
# 利用任意一个坐标将序列分为两个不相重叠的两部分
my_list[:x]
my_list[x:]

#2-对切片进行赋值
l = list(range(10))
l[2:5] = [20]
del l[5:7]
#报出异常，此处仅可以赋值可迭代对象
l[2:5] = 100
l[2:5] = [100]

#3-对列表使用+和*
#当操作对象的引用时，引起注意，以嵌套列表为例
#正常使用
board=[['_'] * 3 for i in range(3)]
board[1][2]='X'
#三个列表的最后一个元素均为'X'
weird_board = [['_']*3] * 3
weird_board[1][2] = 'X'
