"""
referrence:字典
@author: Ethan
"""

#1-浅复制与深复制
#清除方法
x = {}
y = x
x['key'] = 'value'
#此时y不变，{'key','value'}
y
#x指向新的字典
x = {}
y

#此时x清除，y也相对清除
x = {}
y = x
x['key'] = 'value'
y
x.clear()
y

#浅复制中，替换值和修改值的区别，
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
#替换值：x和y的username不同
y
x
#x和y的username不同，machines相同
y['machines'].remove('bar')
y
x

#深复制完全相同
from copy import deepcopy
x = {'username':'admin','machines':['foo','bar','baz']}
y = deepcopy(x)
y['username'] = 'mlh'
y['machines'].remove('bar')
y
x

#2-get访问和索引访问
d = {}
#索引访问异常错误
d['username']
#get访问返回None
d.get('username')

#3-列表和迭代器
d = {'1':'a','2':'b','3':'c'}
#此处返回迭代器
d.items()
#python3.6中无此方法
d.iteritems()
