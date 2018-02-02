"""
function:绘制传播有效图
@author: Ethan
"""

import matplotlib.pyplot as plt
import xlrd
import random

def effectiveDraw(YRank,nodeNum):
    
    # 生成x轴数据
    x = [x*nodeNum for x in range(0,len(YRank))]
    # 以参数作为Y轴数据
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.loglog(x,YRank,linewidth=1,color='m',linestyle='--')
    ax.set_yticks([10,20,30,40])
    ax.set_yticklabels([10,20,30,40])
    # plt.ylim(5, 40)
    ax.legend()
    
def effectiveDraw2(YRankDc,YRankBc,YRankCc,YRankEc,nodeNum):
    
    # 生成x轴数据
    X = [x*nodeNum for x in range(0,len(YRankDc))]
    
    # 画图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xscale("log")
    ax.set_yscale("log")
    plt.xlabel('Rank')
    plt.ylabel('<F(t)>')
    ax.plot(X,YRankDc,label='DC',linewidth=2,color='m',linestyle='--')
    ax.plot(X,YRankBc,label='BC',linewidth=2,color='g',linestyle='-.')
    ax.plot(X,YRankCc,label='CC',linewidth=2,color='r',linestyle=':')
    ax.plot(X,YRankEc,label='EC',linewidth=2,color='b')
    plt.text(300, 300, "Celegant",fontsize=16)
    #plt.xlim(50,150)
    #plt.ylim(10,200)
    plt.legend(loc=4,ncol=1,bbox_to_anchor=(0.3,0.1),fontsize=10)
    plt.show()
    
# c:dc bc cc ec ftMap:字典
def generateYrank(c,ftMap):
    
    YRank = []
    length = len(c)
    for i in range(length):
        temp = ftMap.get(c[i])
        YRank.append(temp)

    return YRank
    
    
# 将ft的排序和值融合成字典
def generateFtMap(ftRank,ftValue):
    
    ftMap = {}
    length = len(ftRank)
    # 将两个链表
    for i in range(length):
        ftMap[ftRank[i]] = ftValue[i]
    
    return ftMap

# 直接读取excel表中的值
def readData(path):
    # 打开excel表
    excelData = xlrd.open_workbook(path)
    table = excelData.sheets()[0]
    nrows = table.nrows
    
    # dc bc cc ec ft数据
    dc = []
    bc = []
    cc = []
    ec = []
    ftRank = []
    ftValue = []
    
    for i in range(nrows):
        [dv,bv,cv,ev,ftR,ftV] = [table.cell(i,0).value,table.cell(i,1).value,
                                    table.cell(i,2).value,table.cell(i,3).value,
                                        table.cell(i,4).value,table.cell(i,5).value]
        dc.append(int(dv))
        bc.append(int(bv))
        cc.append(int(cv))
        ec.append(int(ev))
        ftRank.append(int(ftR))
        ftValue.append(ftV)
        
    return dc,bc,cc,ec,ftRank,ftValue

# 读取excel中的值并且作处理
def readAndShuffle(path):
    
    # 读取数据
    excelData = xlrd.open_workbook(path)
    table = excelData.sheets()[1]
    nrows = table.nrows
    
    # 处理相应内容
    ftRank = []
    ftValue = []
    for i in range(nrows):
        [ftR,ftV] = [table.cell(i,4).value,table.cell(i,5).value]
        ftRank.append(int(ftR))
        ftValue.append(ftV)
    
    # 计算余数和被除数
    blocks = int(nrows / 20)
    res = int(nrows % 20)
    #print(blocks,res)
    temp = []
    c = []
    
    
    for i in range(0,blocks):
        begin = 20 * i 
        end = 20 * (i + 1) - 1
        temp = ftRank[begin:(end+1)]
        #print(len(temp))
        rand = random.randint(0,19)
        for j in range(0,20):
            c.append(temp[rand])
            rand = rand + 1
            if rand == 20:
                rand = 0
    
    temp1 = ftRank[(blocks*20):nrows]
    #print(len(temp1))
    rand1 = random.randint(0,res-1)
    for k in range(0,res):
        #print(rand1)
        c.append(temp1[rand1])
        rand1 = rand1 + 1
        if rand1 == res:
            rand1 = 0
                   
    # 返回相应值
    return c,ftRank,ftValue
   
# 对数据进行拟合,flag 0:ave 1:max
def fit(YRank,nodeNum,flag):
    
    length = len(YRank)
    blocks = int(length / nodeNum)
    YRankFit = []
    for i in range(0,blocks):
        begin = nodeNum * i
        end = nodeNum * (i + 1) - 1
        temp = YRank[begin:(end+1)]
        if flag == 0:
            YRankFit.append(sum(temp)/nodeNum)                
        elif flag == 1:
            YRankFit.append(max(temp))
    
    temp = YRank[blocks*nodeNum:length]
    
    if flag == 0:
        YRankFit.append(sum(temp)/nodeNum)                
    elif flag == 1:
        YRankFit.append(max(temp))
    
    # 此处可以考虑进一步填充点，进一步丰富信息
    return YRankFit

'''
用于对数据进行shuffle 
c,ftRank,ftValue = readAndShuffle("D:\PaperDemo\ASD\pic\eDrawData.xlsx")
'''    
# 开始进行测试
# 0 参数配置
nodeNum = 10
flag = 0
# 1 读取数据
dc,bc,cc,ec,ftRank,ftValue = readData("F:\lzw\EC\data\data4_celegant_effc_0.1_10_100.xlsx")
# 2 生成字典
ftMap = generateFtMap(ftRank,ftValue)
# 3 生成YRank,以dc为例
YRankDc = generateYrank(dc,ftMap)
YRankDcFit = fit(YRankDc,nodeNum,flag)
YRankBc = generateYrank(bc,ftMap)
YRankBcFit = fit(YRankBc,nodeNum,flag)
YRankCc = generateYrank(cc,ftMap)
YRankCcFit = fit(YRankCc,nodeNum,flag)
YRankEc = generateYrank(ec,ftMap)
YRankEcFit = fit(YRankEc,nodeNum,flag)
# 4 effectiveDraw画图
'''
effectiveDraw(YRankDcFit,20)
'''
effectiveDraw2(YRankDcFit,YRankBcFit,YRankCcFit,YRankEcFit,nodeNum)
