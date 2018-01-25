"""
function:增加隐藏层识别手写数字
reference:Tensorflow in action
"""

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#1-载入数据，默认会话
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
sess = tf.InteractiveSession()

#2-设置隐藏层输入输出参数
in_units = 784
h1_units = 300
#权重W1初始化为截断正态分布，标准差为0.1，偏置b1为0
W1 = tf.Variable(tf.truncated_normal([in_units,h1_units],stddev=0.1))
b1 = tf.Variable(tf.zeros([h1_units]))
#权重W2和偏置b2初始化为0
W2 = tf.Variable(tf.zeros([h1_units,10]))
b2 = tf.Variable(tf.zeros([10]))

#3-训练过程中防止过拟合的dropout阶段，由keep_prob控制
x = tf.placeholder(tf.float32,[None,in_units])
keep_prob = tf.placeholder(tf.float32)

#4-隐藏层激活函数为ReLU，随后进行dropout阶段，输出层激活函数为softmax
hidden1 = tf.nn.relu(tf.matmul(x,W1) + b1)
hidden1_drop = tf.nn.dropout(hidden1,keep_prob)
y = tf.nn.softmax(tf.matmul(hidden1_drop,W2) + b2)

#5-设置交叉熵为代价函数，使用优化器优化学习速率，最小化代价函数
y_ = tf.placeholder(tf.float32,[None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))
train_step = tf.train.AdagradOptimizer(0.3).minimize(cross_entropy)

#6-开始进行训练，dropout阶段的keep_prob不为0
tf.global_variables_initializer().run()
for i in range(3000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x:batch_xs,y_:batch_ys,keep_prob:0.75})

#7-计算预测准确率    
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
#eval:启动计算的方式
print(accuracy.eval({x:mnist.test.images,y_:mnist.test.labels,keep_prob:1.0}))