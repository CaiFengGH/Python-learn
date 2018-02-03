"""
function:绘制散点图
@author: Ethan
"""
import matplotlib.pyplot as plt
import xlrd

# 绘制一个散点图，进一步升级为对数坐标的图
def cScatterDraw(x_cV,y_ftV):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    '''
    ax.set_xticks([0,5,10,25,40])
    ax.set_xticklabels([0,5,10,25,40])
    ax.set_yticks([0,10,20,30,40])
    ax.set_yticklabels([0,10,20,30,40])
    '''
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.scatter(x_cV,y_ftV,c='b',s=25,alpha=0.4,marker='o')
    ax.legend()
    
    
# 绘制多个散点图，便于相互之间进行比较
def cScatterDraw1(x_dcV,x_bcV,x_ccV,x_ecV,y_dc_ftV,y_bc_ftV,y_cc_ftV,y_ec_ftV):
    
    figure = plt.figure(4,(20,5))
    
    ax = figure.add_subplot(141)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylabel('F(t)')
    ax.set_xlabel('Degree centrality')
    plt.text(40, 0.2, "Celegant",fontsize=15)
    #plt.ylim(0, 200)
    ax.scatter(x_dcV,y_dc_ftV,c='b',s=30,alpha=0.4,marker='o')
    
    
    ax1 = figure.add_subplot(142)
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_ylabel('F(t)')
    ax1.set_xlabel('Betweenness centrality')
    plt.text(0.006, 1.7, "Celegant",fontsize=15)
    #plt.xlim(0.1, 10000)
    #plt.ylim(0, 200)
    ax1.scatter(x_bcV,y_bc_ftV,c='b',s=30,alpha=0.4,marker='o')
    
    ax2 = figure.add_subplot(143)
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_ylabel('F(t)')
    ax2.set_xlabel('Closeness centrality')
    plt.text(0.4, 0.2, "Celegant",fontsize=15)
    #plt.xlim(0.05, 0.5)
    #plt.ylim(0, 200)
    ax2.scatter(x_ccV,y_cc_ftV,c='b',s=30,alpha=0.4,marker='o')
    
    ax3 = figure.add_subplot(144)
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    ax3.set_ylabel('F(t)')
    ax3.set_xlabel('Effectivity centrality')
    plt.text(0.007, 0.2, "Celegant",fontsize=15)
    plt.xlim(0.004, 0.01)
    #plt.ylim(0, 200)
    ax3.scatter(x_ecV,y_ec_ftV,c='b',s=30,alpha=0.4,marker='o')
    

# 生成绘图数据x_dcV:x轴的度值，y_dcV:y轴的ft值
def generateData(path,tableIndex):
    
    # 读excel中的表
    cScatterDrawData = xlrd.open_workbook(path)
    table = cScatterDrawData.sheets()[tableIndex]
    nrows = table.nrows
    
    # 处理相应内容,生成一个列表dcList和一个字典ftDic
    dcList = []
    ftDic = {}
    for i in range(nrows):
        [nId,cV,ftId,ftV] = [table.cell(i,0).value,table.cell(i,1).value,table.cell(i,2).value,table.cell(i,3).value]
        if tableIndex == 0:
            dcList.append((int(nId),cV))
            ftDic[int(ftId)] = ftV
        elif tableIndex == 1:
            # 注意处理bc中诸多的0值
            if cV != 0:
                # 此处接近中心性较小，考虑乘以一个系数
                dcList.append((int(nId),cV))
            ftDic[int(ftId)] = ftV
        else :
            dcList.append((int(nId),cV))
            ftDic[int(ftId)] = ftV
    
    # 生成横纵坐标轴x_dcV,y_ftV
    x_cV = []
    # bc的长度不同
    length = len(dcList)
    y_ftV = []
    for j in range(1,length+1):
        (dId,dcV) = dcList[-j]
        x_cV.append(dcV)
        ftV = ftDic.get(dId)
        y_ftV.append(ftV)
    
    # print(x_cV)
    return x_cV,y_ftV

x_dcV,y_dc_ftV = generateData("F:\lzw\EC\data\data4_celegant_corrScatter.xlsx",0)
# 此处介数计算存在很多的0值
x_bcV,y_bc_ftV = generateData("F:\lzw\EC\data\data4_celegant_corrScatter.xlsx",1)
x_ccV,y_cc_ftV = generateData("F:\lzw\EC\data\data4_celegant_corrScatter.xlsx",2)
x_ecV,y_ec_ftV = generateData("F:\lzw\EC\data\data4_celegant_corrScatter.xlsx",3)
cScatterDraw1(x_dcV,x_bcV,x_ccV,x_ecV,y_dc_ftV,y_bc_ftV,y_cc_ftV,y_ec_ftV)
