# Performs training on train.csv. Then, the network is tested on 2017.csv. The model is then saved to model.h5 and js/model.json

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflowjs as tfjs

import os
import matplotlib.pyplot as plt
import csv

import tensorflow as tf

from datetime import date, timedelta


tf.set_random_seed(1234)

tf.enable_eager_execution()

print("Requires TensorFlow 1.14.0 Your version: {}".format(tf.__version__))
print("Eager execution: {}".format(tf.executing_eagerly()))

train_dataset_fp = "train.csv"

# Get column order in CSV file

r = csv.reader(open('train.csv'))
lines = list(r)

column_names = lines[0]

feature_names = column_names[:-1]
label_name = column_names[-1]

class_names = ['0', '1', '2', '3']

batch_size = 32

train_dataset = tf.contrib.data.make_csv_dataset(train_dataset_fp, batch_size, column_names=column_names, label_name=label_name, num_epochs=1)

features, labels = next(iter(train_dataset))

def pack_features_vector(features, labels):
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

train_dataset = train_dataset.map(pack_features_vector)

features, labels = next(iter(train_dataset))

model = tf.keras.Sequential([
  tf.keras.layers.Dense(90, activation=tf.nn.relu, input_shape=(252,)),
  tf.keras.layers.Dense(90, activation=tf.nn.relu),
  tf.keras.layers.Dense(4)
])

predictions = model(features)
predictions[:5]

tf.nn.softmax(predictions[:5])

def loss(model, x, y):
  y_ = model(x)
  return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)

l = loss(model, features, labels)

def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets)
  return loss_value, tape.gradient(loss_value, model.trainable_variables)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.02)

global_step = tf.Variable(0)

loss_value, grads = grad(model, features, labels)

optimizer.apply_gradients(zip(grads, model.trainable_variables), global_step)


from tensorflow import contrib
tfe = contrib.eager

train_loss_results = []
train_accuracy_results = []

num_epochs = 151

for epoch in range(num_epochs):
  epoch_loss_avg = tfe.metrics.Mean()
  epoch_accuracy = tfe.metrics.Accuracy()

  for x, y in train_dataset:
    loss_value, grads = grad(model, x, y)
    optimizer.apply_gradients(zip(grads, model.trainable_variables),
                              global_step)

    epoch_loss_avg(loss_value)
    epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

  train_loss_results.append(epoch_loss_avg.result())
  train_accuracy_results.append(epoch_accuracy.result())

  if epoch % 50 == 0:
    print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch, epoch_loss_avg.result(), epoch_accuracy.result()))

fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
fig.suptitle('Training Metrics')

axes[0].set_ylabel("Loss", fontsize=14)
axes[0].plot(train_loss_results)

axes[1].set_ylabel("Accuracy", fontsize=14)
axes[1].set_xlabel("Epoch", fontsize=14)
axes[1].plot(train_accuracy_results)
plt.show()


test_fp = "2017.csv"

test_dataset = tf.contrib.data.make_csv_dataset(test_fp, 1, column_names=column_names, label_name=label_name, num_epochs=1, shuffle=False)

test_dataset = test_dataset.map(pack_features_vector)

test_accuracy = tfe.metrics.Accuracy()

wrong = 0
right = 0

iteration = 0

eventWrong = 0
eventRight = 0
eventIteration = 0

start_date = date(year=2017, month=1, day=1)

for (x, y) in test_dataset:
  logits = model(x)
  prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
  
  per = tf.compat.v1.math.softmax(logits).numpy()
  
  test_accuracy(prediction, y)

  predicted = prediction.numpy()
  actual = y.numpy()

  predicted = predicted[0]
  actual = actual[0]

  if (predicted == actual):
    right += 1
    correct = "Correct: "
    if (predicted != 0 or actual != 0):
      eventRight += 1
  else:
    wrong += 1
    correct = "FALSE: "
    if (predicted != 0 or actual != 0):
      eventWrong += 1

  date = start_date + timedelta(iteration)
  date = date.strftime('%m/%d/%y')

  print(correct + date + " Predicted: " + str(predicted) + " Actual: " + str(actual) + " | 0: " + str(per[0][0]) + " 1: " + str(per[0][1]) + " 2: " + str(per[0][2]) + " 3: " + str(per[0][3]))

  if(predicted != actual):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

  iteration += 1

  if (predicted != 0 or actual != 0):
    eventIteration += 1


print("2017 Accuracy: " + str((right / iteration) * 100) + "%")

print("2017 Event Accuracy: " + str((eventRight / eventIteration) * 100) + "%")

model.save('model.h5')

tfjs.converters.save_keras_model(model, 'js')
