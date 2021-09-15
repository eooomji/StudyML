import numpy as np
import tensorflow as tf

size, seq_len = 100, 3

X = np.empty(shape=(size, seq_len, 1))
Y = np.empty(shape=(size,))

for i in range(size):
  c = np.linspace(i/10., (i+seq_len-1)/10., seq_len)
  X[i] = c[:, np.newaxis]
  Y[i] = (i+seq_len) / 10

for i in range(len(X)):
  print(X[i], Y[i])
  
model = tf.keras.Sequential([tf.keras.layers.SimpleRNN(units=20, return_sequences=False, input_shape=[3,1]), tf.keras.layers.Dense(1)])

model.compile(optimizer='adam', loss='mse')
model.summary()

model2 = tf.keras.Sequential([tf.keras.layers.SimpleRNN(units=20, return_sequences=False, input_shape=[seq_len, 2]), tf.keras.layers.Dense(1)])

model2.compile(optimizer='adam', loss='mse')
model2.summary()
