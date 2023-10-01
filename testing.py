import tensorflow as tf
import numpy as np

t = tf.zeros([5,5,5,5])

print(t)

t = tf.reshape(t, [625])
print(t)