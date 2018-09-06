import tensorflow as tf
with tf.Graph().as_default():	
	primes=tf.constant([2,3,5,7,11,13],dtype=tf.int32)
	ones=tf.ones([6],dtype=tf.int32)
	beyond_primes=tf.add(primes,ones)
	with tf.Session() as sess:
		print "beyond primes:",beyond_primes.eval()

with tf.Graph().as_default():
	scalar=tf.zeros([])
	vector=tf.zeros([3])
	matrix=tf.zeros([4,5])
	with tf.Session() as sess:
		print "scalar has a shape of:",scalar.get_shape(),"and a value of:",scalar.eval()
		print "vector has a shape of:",vector.get_shape(),"and a value of:",vector.eval()
		print "matrix has a shape of:",matrix.get_shape(),"and a value of:",matrix.eval()
with tf.Graph().as_default():
	primes=tf.constant([2,3,5,7,11,13],dtype=tf.int32)
	ones=tf.ones([],dtype=tf.int32)
	beyond_primes=tf.add(primes,ones)
	with tf.Session() as sess:
		print "new beyond primes:",beyond_primes.eval()
with tf.Graph().as_default():
	#3x4 matrix
	mat1=tf.constant([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=tf.int32)
	#4x1 matrix
	mat2=tf.constant([[1],[2],[3],[4]],dtype=tf.int32)
	#3x1 matrix
	mat12=tf.matmul(mat1,mat2)
	with tf.Session() as sess:
		print "mat12:",mat12.eval()
with tf.Graph().as_default():
	#4x4 matrix
	matrix=tf.constant([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],dtype=tf.int32)
	reshaped_2x8_matrix=tf.reshape(matrix,[2,8])
	reshaped_8x2_matrix=tf.reshape(reshaped_2x8_matrix,[8,2])
	reshaped_2x2x4_matrix=tf.reshape(reshaped_8x2_matrix,[2,2,4])
	reshaped_vector=tf.reshape(reshaped_2x2x4_matrix,[16])
	with tf.Session() as sess:
		print "original matrix:"
		print matrix.eval()
		print "reshaped_2x8_matrix:"
		print reshaped_2x8_matrix.eval()
		print "reshaped_8x2_matrix:"
		print reshaped_8x2_matrix.eval()
		print "reshaped_2x2x4_matrix:"
		print reshaped_2x2x4_matrix.eval()
		print "reshaped_vector:"
		print reshaped_vector.eval()
g=tf.Graph()
with g.as_default():
	v=tf.Variable([3])
	w=tf.Variable(tf.random_normal([1],mean=1.0,stddev=0.35),dtype=tf.float32	)
with g.as_default():
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		print v.eval()
		print w.eval()
		assignment=tf.assign(v,[4])
		# v.eval() will not change. have to run the sess on assingment
		sess.run(assignment)
		print v.eval()
# Write your code for Task 2 here.
with tf.Graph().as_default(),tf.Session() as sess:
	dice1=tf.Variable(tf.random_uniform([10,1],minval=1,maxval=7,dtype=tf.int32))
	dice2=tf.Variable(tf.random_uniform([10,1],minval=1,maxval=7,dtype=tf.int32))
	dice=tf.concat([dice1,dice2],1)
	dicesum=tf.add(dice1,dice2)
	dice=tf.concat([dice,dicesum],1)
	sess.run(tf.global_variables_initializer())
	print dice.eval()
