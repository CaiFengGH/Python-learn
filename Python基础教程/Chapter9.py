"""
function:魔法方法
@author: Ethan
"""

#1-魔法方法
#__init__:构造方法
#旧式类可以使用未绑定方法
class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No,thanks')
            
class SongBird(Bird):
    def __init__(self):
        #通过将当前的实例作为self参数提供给未绑定方法，可以提供超类构造参数的实现
        #Bird.__init__(self)
        #直接调用super方法，__init__方法不能写self，因为super方法已经传入，无需隐式传递
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

#__del__:析构方法
#垃圾回收之前调用

#基本序列和映射规则
#定义一个无穷序列,此序列没有__len__方法，为无穷序列：

def checkIndex(key):
    if not isinstance(key,(int,)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence(object):
    
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}
        
    def __getitem__(self,key):
        
        checkIndex(key)
        
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step
        
    def __sefitem__(self,key,value):
 
        checkIndex(key)
        
        self.changed[key] = value

#子类化序列
#继承子类化超类，利用其行为
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.count = 0

    def __getitem__(self,index):
        super(CounterList,self).__getitem__(index)                    
    
#2-属性
#property函数,可以直接访问和使用
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)

#静态方法和类成员方法
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
        
    @classmethod
    def cmeth(cls):
        print('This is a class method of ',cls)

#3-迭代器
#列表会占用太多内存，使用迭代器更加通用、更简单和更优雅
class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
    
#从迭代器得到序列
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
    
    def __iter__(self):
        return self

l = TestIterator()
#此处返回列表1-10
list(l)    

