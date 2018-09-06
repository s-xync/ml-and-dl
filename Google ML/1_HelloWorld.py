import tensorflow as tf
# x=tf.constant("Hello World")
# sess=tf.Session()
# print sess.run(x)
g=tf.Graph()
with g.as_default():
	x=tf.constant(1,name="x_const")
	y=tf.constant(2,name="y_const")
	sum1=tf.add(x,y,"x_y_sum")
	z=tf.constant(3,name="z_const")
	sum2=tf.add(sum1,z,"x_y_z_sum")
	with tf.Session() as sess:
		# sess.run(g)
		# print sum2.eval()
		print sum1.eval()