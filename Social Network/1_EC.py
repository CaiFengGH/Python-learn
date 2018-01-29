"""
function:由平均最短路径排序
@author: Ethan
"""

import networkx as nx
import xlrd
import numpy as np

# 1-读取文件
edges = xlrd.open_workbook("F:\lzw\EC\data\data1_usAir_332_2126.xlsx")
table = edges.sheets()[0]
nrows = table.nrows
print(nrows)

# 2-生成有向图
graph = nx.DiGraph()
for i in range(nrows):
    [sou,des] = [table.cell(i,0).value,table.cell(i,1).value]
    sou = int(sou)
    des = int(des)
    graph.add_edge(sou,des)
    
# 3-转换为无向图
graph = graph.to_undirected()
numEdges = graph.number_of_edges()
numNodes = graph.number_of_nodes()
print(numEdges,numNodes)

# 4-按照节点度排序
degree = graph.degree()
sortDegree = sorted(degree.items(), key=lambda x : x[1], reverse=True)

# 5-度中心性
degree_centrality = nx.degree_centrality(graph)

# 6-介数中心性排序
betweenness_centrality = nx.betweenness_centrality(graph)

# 7-紧密度中心性排序
closeness_centrality = nx.closeness_centrality(graph)

# 8-EC和EC2排序,EC：论文方法 EC2:创新方法
# 网络直径
diameter = nx.diameter(graph)

# 生成最短路径二维数组
# 原始方法
oldShortest = np.zeros([numNodes,numNodes])
# 改进方法
oldShortest2 = np.zeros([numNodes,numNodes])

# 初始化shortest
for i in range(0,numNodes):
    for j in range(0,numNodes):
        if i == j:
            continue
        oldDistance=nx.shortest_path_length(graph,source=i+1,target=j+1)
        oldShortest[i][j] = 1/oldDistance
        oldShortest2[i][j] = oldDistance
        
oldAveShortest = sum(map(sum,oldShortest))/(numNodes*(numNodes-1))
oldAveShortest2 = sum(map(sum,oldShortest2))/(numNodes*(numNodes-1))

# 最后的排序结果，按照度降序的顺序
res = []
res2 = []
time = 0
 
# 节点在网络中以数字1开始表示，矩阵中是以0开始表示，注意节点标签问题
for i in range(0,numNodes):
    
    time = time + 1
    
    # 删除某个节点，按照度的大小顺序一次删除
    removeNode = sortDegree[i][0]
    print(removeNode);print(time)
   
    # 删除边
    neighbors=graph.neighbors(removeNode) 
    for j in range(0,len(neighbors)):
        graph.remove_edge(removeNode,neighbors[j])
        
    # 查找所有的孤立节点
    isolateNodes = []
    for k in range(1,numNodes+1):
        if len(graph.neighbors(k)) == 0:
            isolateNodes.append(k)
        
    # 删除节点后的最短路径    
    newShortest = np.zeros([numNodes,numNodes])
    newShortest2 = np.zeros([numNodes,numNodes])
    
    for m in range(0,numNodes):
        
        # 孤立节点赋值为直径
        if (m+1) in isolateNodes:
            
            newShortest[m,:] = 0
            newShortest2[m,:] = diameter
            #注意自己到自己的距离始终为0
            newShortest2[m,m] = 0
            continue
        
        for n in range(0,numNodes):
            if m == n:
                continue
            try:
                newDistance=nx.shortest_path_length(graph,source=m+1,target=n+1)
                newShortest[m][n] = 1/newDistance
                newShortest2[m][n] = newDistance
            except nx.exception.NetworkXNoPath:
                newShortest[m][n] = 0
                newShortest2[m][n] = diameter
    
    newAveShortest = sum(map(sum,newShortest))/(numNodes*(numNodes-1))
    newAveShortest2 = sum(map(sum,newShortest2))/(numNodes*(numNodes-1))
    
    # 原始方法：节点删除后newAveShortest值小 改进方法：节点删除后newAveShortest值大                    
    change = (oldAveShortest - newAveShortest)/oldAveShortest
    change2 = (newAveShortest2 - oldAveShortest2)/oldAveShortest2
    
    res.append(change)
    res2.append(change2)
    
    # 重新将删除的边进行添加
    for l in range(0,len(neighbors)):
        graph.add_edge(removeNode,neighbors[l])
        
