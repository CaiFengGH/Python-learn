"""
function:
@author: Ethan
"""
import matplotlib.pyplot as plt
import xlrd

# 稳定状态的画图
def sDraw(xRank,yFtValue1,yFtValue2):
    
    res = 10
    
    plt.errorbar(xRank, yFtValue1,label='EC',yerr=res,fmt='-o',color='b',markersize=5)
    plt.errorbar(xRank, yFtValue2,label='CC',yerr=res,fmt='-o',color='r',markersize=5)
    plt.xlabel('t')
    plt.ylabel('infected node F(t)')
    plt.ylim(0, 200)
    plt.plot(xRank,yFtValue1)    
    plt.plot(xRank,yFtValue2)    
    plt.legend(loc=4,ncol=4,bbox_to_anchor=(0.95,0.1))
    plt.show() 
    
# 处理基本数据
def generateData(steps,path,row):
    
    xRank = [x for x in range(0,steps)]
    yFtValue = []
    
    # 读取excel中的基础数据
    sDrawData = xlrd.open_workbook(path)
    table = sDrawData.sheets()[5]
    cols = table.ncols
    print(cols)
    
    for i in range(1,cols):
        temp = table.cell(row,i).value
        yFtValue.append(temp)
                 
    # 按照steps进行扩展
    yFtValue.insert(0,0) 
    length = steps - len(yFtValue)
    sFtV = yFtValue[-1]
    for j in range(0,length):
        yFtValue.append(sFtV)
    # 返回数据
    return xRank,yFtValue

xRank,yFtValue1 = generateData(40,"F:\lzw\EC\data\data4_celegant_stableError.xlsx",6)
xRank,yFtValue2 = generateData(40,"F:\lzw\EC\data\data4_celegant_stableError.xlsx",16)
sDraw(xRank,yFtValue1,yFtValue2)
