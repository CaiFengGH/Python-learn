"""
function:基于梯度下降的优化方法
@author: Ethan
"""
import numpy as np

class AdalineGD(object):
    
    # 初始化函数
    def __init__(self,eta=0.01,n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        
    # 拟合函数
    def fit(self,X,y):
        # 初始化权重和损失函数
        self.w = np.zeros(X.shape[1] + 1)
        self.cost = []
        
        # n_iter次迭代
        for x in range(0,self.n_iter):
            # 输出函数
            output = self.predict(self,X)
            errors = y - output
            # 更新权重,矩阵与向量的乘积
            self.w[1:] += self.eta * X.T.dot(errors)
            self.w[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2
            self.cost.append(cost)
        
        return self
            
    # 预测函数
    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0,1,-1)
    
    # 激活函数
    def net_input(self,X):
        return np.dot(X,self.w[1:]) + self.w[0]
    
'''
# 注意点
1-特征标准化
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
2-大规模训练集
由于单个样本得到的损失函数相对于整个样本集合得到的损失函数更具有随机性，反而有助于随机梯度下降算法
避免陷入局部最小点，通常以随机方式选择样本计算梯度，每一轮迭代后将训练集打乱重排
3-自适应学习速率
不断减小的自适应学习速率替代固定的学习速率，不能保证到达全局最优，但是会接近全局最优
'''


