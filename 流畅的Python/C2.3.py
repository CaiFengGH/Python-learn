"""
Created on Mon Apr  9 12:12:22 2018
<流畅的Python2.3>
@author: Ethan
"""

#元组：记录-字段的集合，字段的数量和位置信息 不可变列表-相似a,b = b,a
#优雅的实现交换
a = 1
b = 2
a,b = b,a

divmod(20,8)
t = (20,8)
# *将可迭代对象元素拆分
divmod(*t)

# *处理剩下元素
a,b,*rest = range(5)
a,b,rest

# 具名元组：这个实例跟普通对象实例要小，因为Python不会用__dict__存放这些实例属性
from collections import namedtuple 
City=namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))
tokyo.population
tokyo[1]

# 具名元组三个属性
City._fields

LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','IN',21.935,LatLong(28.613889,77.208889))

delhi = City._make(delhi_data)
delhi._asdict()
