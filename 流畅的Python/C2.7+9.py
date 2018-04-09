"""
Created on Mon Apr  9 15:32:14 2018
<流畅的Python2.7+8+9>
@author: Ethan
"""

#1-list.sort和sorted方法区别
fruits = ['grape', 'raspberry', 'apple', 'banana']
#列表自身sort方法返回新对象
fruits.sort()
#高阶函数sorted方法不返回新对象
sorted(fruits,key=len,reverse=True)
sorted(fruits,reverse=True)

#2-bisect和insort函数均利用二分查找算法在有序序列中查找或删除元素

#3-使用array操作只包含数字的列表
from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))

fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()

#4-使用双向队列
from collections import deque
dq = deque(range(10),maxlen=10)
#旋转操作差异
dq.rotate(-4)
dq.rotate(3)
dq.appendleft(-1)
dq.extend([11,22,33])
#左侧加入后是倒序操作
dq.extendleft([10,20,30,40])

