import numpy as np
import tensorflow as tf
# coefficients=np.array([[1.],[-10.],[25]])
coefficients=np.array([[1.],[-20.],[100]])
x=tf.placeholder(tf.float32,[3,1])
w=tf.Variable(0,dtype=tf.float32)
# cost is minimised at w=5
# cost=tf.add(tf.add(w**2,tf.multiply(-10.0,w)),25)
# or
# cost=w**2-10*w+25
# cost function is the heart of the program
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train=tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
print sess.run(w)
# sess.run(train)
sess.run(train,feed_dict={x:coefficients})
print sess.run(w)
for i in range(0,10000):
	# sess.run(train)
	sess.run(train,feed_dict={x:coefficients})
print sess.run(w)
sess.close()
# or
# with tf.Session() as sess:
# 	sess.run(init)
# 	print sess.run(w)
# 	sess.run(train)
# 	print sess.run(w)
# 	for i in range(0,10000):
# 		sess.run(train)
# 	print sess.run(w)