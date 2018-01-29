"""
function:介绍函数的一些基本功能
@author: Ethan
"""

#1-关键字参数：用于解决参数位置的问题
#同时默认参数
#2-收集参数：参数前的星号将所有值放置在同一个元组中

#3-global:声明为全局变量
x = 1
def change_global():
    global x
    x = x + 1
# 此时全局变量x为2
change_global()


