"""
function:单次实验验证sir仿真性能
@author: Ethan
"""
import xlrd
import numpy as np
import random 

# 0传递节点数和感染概率,及设置初始值
nodeNum = 379
a = 0.5
step = 30

# 1读图
edges = xlrd.open_workbook("D:\PaperDemo\ASD\data\data7_netscience_379_914.xlsx")
table = edges.sheets()[0]
nrows = table.nrows
print(nrows)

# 2构建连接矩阵
p = np.zeros((nodeNum,nodeNum),dtype=np.int)
for i in range(nrows):
    [sou,des] = [table.cell(i,0).value,table.cell(i,1).value]
    p[int(sou-1)][int(des-1)] = 1
    p[int(des-1)][int(sou-1)] = 1
     
# 3初始化状态
state = np.zeros((nodeNum,3),dtype=np.int)
stateList = np.zeros((step,nodeNum,3),dtype=np.int)

for i in range(nodeNum):
    state[i,0] = 1

# 4初始化种子节点
seed = 108

state[seed-1,0] = 0
state[seed-1,1] = 1

oldSeedList = []
newSeedList = []

oldSeedList.append(seed-1)

num = 0
res = 0
resList = []

# 5sir传播 
for i in range(step):
    num = num + 1
    print("num--------"+str(num))
    
    oldLen = len(oldSeedList)
    
    for j in range(0,oldLen):
        oldSeed = oldSeedList[j]
        for m in range(nodeNum):
                if p[oldSeed,m] == 1:
                    if state[m,0] == 1:
                        if random.random() < a:
                            print(str(oldSeed)+":"+str(m))
                            newSeedList.append(m)
        
    # 种子节点的状态进行更新
    for k in range(0,oldLen):
        oldSeed = oldSeedList[k]
        state[oldSeed][1] = 0
        state[oldSeed][2] = 1
             
    newLen = len(newSeedList)
    for l in range(0,newLen):
        newSeed = newSeedList[l]
        state[newSeed][0] = 0
        state[newSeed][1] = 1
             
    oldSeedList = newSeedList
    newSeedList = []
    stateList[i] = state
       
for n in range(step):
    res = nodeNum - sum(stateList[n][:,0])
    resList.append(res)

