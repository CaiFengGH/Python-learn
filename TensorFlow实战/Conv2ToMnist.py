"""
function:两个卷积层加上一个全连接层构建简单的神经网络
reference:Tensorflow in action
"""

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#1-载入数据，创建会话
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
sess = tf.InteractiveSession()

#2-权重和偏置的初始化函数
def weight_variable(shape):
    # 截断的正太分布噪声，标准差为0.1，打破完全对称
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)
    
def bias_variable(shape):
    # 偏置增加正值避免死亡节点
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
    
#3-卷积层和池化层
def conv2d(x,W):
    # 步长是1*1,
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    # ksize中，四个元素的1Dtensor
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    
#4-定义输入的placeholder
# x:特征 y_:真实label
x = tf.placeholder(tf.float32,[None,784])
y_ = tf.placeholder(tf.float32,[None,10])
# -1:样本数量不定，1:一通道，灰白图像
x_image = tf.reshape(x,[-1,28,28,1])

#5-第一个卷积层，感受野:5*5 颜色通道:1 卷积核大小:32 激活函数:relu 池化:2*2
W_conv1 = weight_variable([5,5,1,32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

#6-第二个卷积层，感受野:5*5 颜色通道:32 卷积核大小:64 激活函数:relu 池化:2*2
W_conv2 = weight_variable([5,5,32,64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#7-全连接层 tensor：7*7*64 隐层：1024 
W_fc1 = weight_variable([7*7*64,1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1) + b_fc1)

#8-dropout，训练:随机丢弃一部分节点数据来减轻拟合 预测：保留全部数据追求最好的预测性能 
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

#9-输出层，Softmax
W_fc2 = weight_variable([1024,10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2) + b_fc2)

#10-定义损失函数:注意负号，使用优化器，初始化学习速率
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv),reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#11-准确率操作
correct_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

#12-开始运行
# 初始化全部参数
tf.global_variables_initializer().run()
for i in range(20000):
    # 使用mini-batch:50
    batch = mnist.train.next_batch(50)
    # 每隔100次进行一次准确率评测，评测时keep_prob:1.0
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x:batch[0],y_:batch[1],keep_prob:1.0})
        print("step %d,training accuracy %g"%(i,train_accuracy))
    # 训练时keep_prob:1.0     
    train_step.run(feed_dict={x:batch[0],y_:batch[1],keep_prob:0.5})
    


