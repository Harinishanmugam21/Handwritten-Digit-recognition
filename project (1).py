# -*- coding: utf-8 -*-
"""project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KzRkjKvJ3cZ0FjcNzCCzchKTxlBkhsv2
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

from keras.models import Sequential
from keras.layers import Dense,Conv2D, Flatten
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import to_categorical

(X_train, y_train),(X_test, y_test)=mnist.load_data()

plt.imshow(X_train[23])

X_train[0].shape

X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)

X_train[0].shape

y_train[3]

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_train[0]

model = Sequential()

model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3,activation= 'relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=3)

model.predict(X_test[:4])

y_test[:4]