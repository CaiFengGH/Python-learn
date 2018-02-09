"""
function:计算网络的基本参数
@author: Ethan
"""
import networkx as nx
import xlrd

# 1-读取文件
edges = xlrd.open_workbook("D:\PaperDone\EC\data\data4_celegant_453_4596.xlsx")
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
m = graph.number_of_edges()
n = graph.number_of_nodes()
print(n,m)

# 4-按照节点度排序
degree = graph.degree()
sortDegree = sorted(degree.items(), key=lambda x : x[1], reverse=True)

sumDegree = 0

for i in range(0,n):
    node,degree = sortDegree[i]
    sumDegree += degree
    
arg_degree = sumDegree / n
    
cluster_C = nx.average_clustering(graph)

assortative_r = nx.degree_assortativity_coefficient(graph)
