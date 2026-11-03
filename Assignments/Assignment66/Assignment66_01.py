# 1: Write a Python program to simulate a single artificial neuron.
# Input:
# x1 = 2
# x2 = 3
# w1 = 0.4
# w2 = 0.6
# bias = 0.5 

# Tasks:
# 1. Calculate weighted sum.
# 2. Apply sigmoid activation function.
# 3. Display final output.
# 4. Explain whether output is close to 0 or 1.

import tensorflow as tf 

inputs = tf.constant([2.0,3.0]) 

weights = tf.constant([0.4,0.6])

bias = tf.constant(0.5)

weighted_sum = tf.reduce_sum(inputs*weights) + bias

print("Inputs :",inputs.numpy())
print("Weights :",weights.numpy())
print("Bias :",bias.numpy())

print("Weighted Sum :",weighted_sum.numpy())

output = tf.sigmoid(weighted_sum)

print("Output is :",output.numpy())

# Output is : 0.9568927 means it is closed to 1






