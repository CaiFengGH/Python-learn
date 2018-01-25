"""
function:softmax regression实现mnist
reference:Tensorflow in action
"""
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 1- 读取数据
mnist = input_data.read_data_sets('MNIST_data/',one_hot=True)
# 2- 查看数据集的特征
print(mnist.train.images.shape,mnist.train.labels.shape)
print(mnist.test.images.shape,mnist.test.labels.shape)
print(mnist.validation.images.shape,mnist.validation.labels.shape)

# 1-注册session
sess = tf.InteractiveSession()
# 2-输入数据
x = tf.placeholder(tf.float32,[None,784])
# 3-初始化权重和偏置
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# 4-实现softmax算法
y = tf.nn.softmax(tf.matmul(x,W) + b)
# 5-交叉熵损失函数,输入真实类别
y_ = tf.placeholder(tf.float32,[None,10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))
# 6-定义优化算法
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 7-使用全局优化器
tf.global_variables_initializer.run()
# 8-迭代执行
for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x:batch_xs,y_:batch_ys})
    
# 9-计算准确率,argmax(y,1):1所在的索引 cast:实现数据类型间的转换
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
