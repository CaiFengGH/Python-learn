"""
function:实现相关系数的折线图
@author: Ethan
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def correlationDraw(Ydc,Ybc,Ycc,Yec):

    # 传递数据
    #X = [x/100 for x in range(1,11)]
    X = np.linspace(0.01, 0.10, 10, endpoint=True)
    
    # 画图
    # markerfacecolor='white',
    plt.plot(X,Ydc,label='DC',linewidth=2,color='m',marker='o',markerfacecolor='white',markersize=6)
    plt.plot(X,Ybc,label='BC',linewidth=2,color='g',marker='^',markerfacecolor='white',markersize=6)
    plt.plot(X,Ycc,label='CC',linewidth=2,color='r',marker='s',markerfacecolor='white',markersize=6)
    plt.plot(X,Yec,label='EC',linewidth=2,color='b',marker='*',markerfacecolor='white',markersize=8)
    
    # 设置横纵坐标的刻度方向
    matplotlib.rcParams['xtick.direction'] = 'in'
    matplotlib.rcParams['ytick.direction'] = 'in'
    # 横纵坐标及图示
    plt.xlabel('infection probability(α)')
    plt.ylabel('rank correlation(\τ)')
    # 标示图形类别
    plt.text(0.01, 0.36, "Celegant",fontsize=16)
    # 横纵坐标范围
    plt.xlim(X.min() * 0.1, X.max() * 1.1)
    plt.ylim(0.1, 0.4)
    # 调整图例的位置
    plt.legend(loc=4,ncol=4,bbox_to_anchor=(0.95,0.01))
    plt.show() 
    
Ydc = [0.2711129344195042,0.28461192834398014,0.27366231026197035,0.27482466936255834,0.2865361698802477,
		0.2928949579011116,0.3107112856277716,0.32102600168004847,0.33461290511633357,0.33358729414522653]
Ybc = [0.21987145675828793,0.21721463595694387,0.21191076207779014,0.20266072789075779,0.2136689523139737,
		0.2150462013323175,0.22893590419816756,0.23141690597589326,0.24428099787063626,0.23651565766082558]
Ycc = [0.23336068295922952,0.26477368184570904,0.27593818984547464,0.2794838734884448,0.26941335052452675,
		0.26799703061204555,0.2811443864892848,0.27311531774404657,26751841215886224,0.26403133485709823]
Yec = [0.2263083865674266,0.24709410224852996,0.2563441364355623,0.26227314462091467,0.24825646134911797,
		0.24965324581453047,0.25875676414854754,0.2510402625564086,0.2470452636308582,0.24598058176561372]
correlationDraw(Ydc,Ybc,Ycc,Yec)

