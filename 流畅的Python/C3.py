"""
Created on Tue Apr 10 10:17:12 2018
<流畅的Python3>
@author: Ethan
"""

#1-setdefault：更新键值时的高效操作
my_dict.setdefault(key,[]).append(new_value)
#上下两者等效，下面会进行两次或者三次查询，上面一次完成
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(new_value)

#2-defaultdict：处理找不到键的一个选择
#在__getitem__找不到键时被调用，即dd[k]而非get(k)，返回构造时的可调用对象
dd = defaultdict(list)

#3-特殊方法__missing__：一个类继承dict，且提供__missing_方法，在__getitem__找不到
#   键时自动调用
class StrKeyDict0(dict):
    
    def __missing__(self):
        #此处无判断，则会发生循环调用
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
                    
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default
            
    def __contains__(self,key):    
        return key in self.keys or str(key) in self.keys()
        
#4-Collection的变种
#collections.OrderedDict:添加时保持顺序，键的迭代次序是一致的；
#collections.Counter:映射类型给键准备一个计数器
import collections
ct = collections.Counter('abracadabra')
ct.update('aaaaazzz')
#按照次序返回映射里最常见的n个键和计数
ct.most_common(2)

#5-不可变的映射类型
#types MappingProxyType:返回只读映射视图，且是动态的；
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
d_proxy
#报出异常，d_proxy不具备更改功能
d_proxy[2] = 'x'
d[2] = 'x'
d_proxy

#6-集合
#frozenset:不可变的集合，本身可以散列当作集合的元素
#集合包括中缀运算符，a|b a&b a-b实现集合的操作
#创建一个空集，使用不带参数的构造方法set()，写成{}:空字典
#{1，2，3}比构造方法set([1,2,3])要更快且更易读
#frozenset本身没有字面量语法，只能采用构造方法