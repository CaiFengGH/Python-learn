"""
function:条件/循环/其他语句
@author: Ethan
"""

#1-基础
#序列解包,注意左右两边数量应该一致
x,y,z = [1,2,3]
#python3.0后print是一个函数
print(x,y,z)
#返回元组
dic = {'name':'xiaolv','age':22}
key,value = dic.popitem()
print(key,value)
#链式赋值
x = y = max(1,2)
#增量赋值
y *=2

#2-其他语句
#断言:与其让程序在晚些时候崩溃，不如在错误条件出现时让它崩溃
age = 10
assert 0 < age < 100
age = -1
assert 0 < age < 100,'The age must be realistic'

#并行迭代
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for name,age in zip(names,ages):
    print(name+' is '+str(age))
    
#获取元素索引
for index,age in enumerate(ages):
    print(index+''+age)
    
#pass
#测试时部分代码块未填充，类似于占位符
if name == 'lzw':
    print(name)
elif name == 'lsj':
    pass
else:
    print('None')
    
#del语句，删除引用
x = ['hello','world']
y = x
y[1] = 'python'
x
#此处删除的是引用，并不影响y的值
del x
y
