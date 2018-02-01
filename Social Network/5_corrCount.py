"""
function:用于计算两者的Kendall Rank相关系数
@author: Ethan
"""

import xlrd

# rankEc2和rankFt均是由排列顺序构成
def correlation(nodeNum,rankC,rankFt):
    
    nc = 0
    nd = 0
    for i in range(1,nodeNum+1):
        for j in range(i+1,nodeNum+1):
            iRankC = rankC.index(i)
            iRankFt = rankFt.index(i)
            jRankC = rankC.index(j)
            jRankFt = rankFt.index(j)
            #打印出两者比较的节点
            print(str(iRankC)+":"+str(iRankFt)+"-"+str(jRankC)+":"+str(jRankFt))
            if (iRankC > jRankC and iRankFt > jRankFt) or (iRankC < jRankC and iRankFt < jRankFt):
                nc = nc + 1
            if (iRankC > jRankC and iRankFt < jRankFt) or (iRankC < jRankC and iRankFt > jRankFt):
                nd = nd + 1
    #此处系数计算的1/2是否应该省略？            
    correlation = (nc - nd) /((nodeNum * (nodeNum - 1)))

    return correlation,nc,nd

# 用于生成节点数量，Ec2排名，Ft的排名
def generateData(path):
     
    # 读取数据
    rawData = xlrd.open_workbook(path)
    data = rawData.sheets()[3]
    nodeNum = data.nrows
    print(nodeNum)
    
    # 生成rankEc2和rankFt
    rankC = []
    rankFt = []
    
    for i in range(nodeNum):
        [c,ft] = [data.cell(i,0).value,data.cell(i,10).value]
        c = int(c)
        ft = int(ft)
        rankC.append(c)
        rankFt.append(ft)
    
    return nodeNum,rankC,rankFt

path = "F:\lzw\EC\data\data4_celegant_corr.xlsx"
nodeNum,rankC,rankFt = generateData(path)
correlation,nc,nd = correlation(nodeNum,rankC,rankFt)
