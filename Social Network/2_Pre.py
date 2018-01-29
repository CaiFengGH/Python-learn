"""
function:将不连通图转换为连通图，且更改节点的标号
@author: Ethan
"""

import networkx as nx
import xlrd
import xlwt

# 读取excel表
edges = xlrd.open_workbook("D:\PaperDemo\ASD\data6_physics.xlsx")
table = edges.sheets()[0]
nrows = table.nrows
print(nrows)

# 创建excel表
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('netscience', cell_overwrite_ok=True)

# 生成有向图
graph = nx.DiGraph()
for i in range(nrows):
    [sou,des] = [table.cell(i,0).value,table.cell(i,1).value]
    sou = int(sou)
    des = int(des)
    graph.add_edge(sou,des)
    
# 转换为无向图
graph = graph.to_undirected()

# 最大联通子图
subgraph = sorted(nx.connected_components(graph),key=len,reverse=True)
maxSubGraph = subgraph[0]

# 删除非联通子图部分
newGraph = nx.DiGraph()
for i in range(nrows):
    [sou,des] = [table.cell(i,0).value,table.cell(i,1).value]
    if sou in maxSubGraph and des in maxSubGraph:
        sou = int(sou)
        des = int(des)
        newGraph.add_edge(sou,des)
        
newGraph = newGraph.to_undirected()
numEdges = newGraph.number_of_edges()
numNodes = newGraph.number_of_nodes()

print(numEdges,numNodes)

# 将节点标号不规格的转换为规格的
nodes = newGraph.nodes()
nodeDic = {}
order = 1
for i in range(0,len(nodes)):
    nodeDic[nodes[i]] = order
    order = order + 1
    
# 将图的边的标号进行更改
links = newGraph.edges()
for i in range(0,len(links)):
    s,d = links[i]
    news = nodeDic[s]
    newd = nodeDic[d]
    sheet.write(i, 0, news) 
    sheet.write(i, 1, newd) 
book.save(r"D:\PaperDemo\ASD\physics.xls")
