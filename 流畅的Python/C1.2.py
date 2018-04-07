"""
Created on Sat Apr  7 16:46:12 2018
<流畅的Python1.2>
@author: Ethan
"""
from math import hypot 

#实现一个二维向量基本操作操作
class Vector:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)
    
    def __abs__(self):
        return hypot(self.x,self.y)
    
    def __bool__(self):
        #return bool(self.x or self.y)
        return bool(abs(self))
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
        
    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y * scalar)
        
#运算符的基本原则就是不改变操作对象，产生一个新值
#内置函数bool调用__bool__方法，如果没有实现__bool__方法，则调用__len__方法，0：False
#Python解释器调用特殊方法实现对象的基本操作
