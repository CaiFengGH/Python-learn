"""
referrence:字符串
@author: Ethan
"""

#1-字符串格式化
#简单化格式化
format = "Hello,%s,%s enough for ya?"
values = ('world','Hot')
print(format % values)

#宽度 精度 和对齐
from math import pi
'Pi:%f...' % pi
#宽度为10
'Pi:%10f...' % pi
#精度为2
'Pi:%.2f...' % pi
#字符串取5个字符
'%.*s' % (5,'hello,world')
#使用0进行填充
'%010.2f' % pi
#-表示左对齐
'%-10.2f' % pi

#2-字符串常用方法
subject = '$$$ Get rich now!!! $$$'
subject.find('$$$')
subject.find('$$$',1)
#开始索引和结束索引，通常结束索引不包含
subject.find('!!!',1,16)

#join方法，
seq = ['1','2','3','4']
sep = '+'
sep.join(seq)
dirs = '','usr','bin','env'
'/'.join(dirs)

#替换字符串中的所有的'is'，注意与translate的区别
'This is a test'.replace('is','aaa')

#不提供分隔符，程序会把空格作为分隔符(空格、制表、换行等)
'1+2+3+4'.split('+')

#去除字符串两端的空格
'   hello xidian   '.strip()

