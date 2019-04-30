import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np


X = np.load("C:/Users/amman/Downloads/GSU/Senior/Spring 2019/Deep Learning/DL_Project/X_data.npy")
y = pickle.load(open("C:/Users/amman/Downloads/GSU/Senior/Spring 2019/Deep Learning/DL_Project/y.pickle", "rb"))

X = X/255.0

model = Sequential()
model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
#model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation("relu"))

model.compile(loss="binary_crossentropy",
             optimizer="adam",
             metrics=['accuracy'])

model.fit(X, y, batch_size=10, validation_split=0.2)