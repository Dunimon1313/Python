# -*- coding: utf-8 -*-
"""AS5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oPM05M_O5p9vOXp4wh7OKaaSD7X_bbpZ
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import backend as kbe
import math
import matplotlib.pyplot as plt
import os
import cv2
import csv
import keras
from tensorflow import keras
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from tensorflow.keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

#loads variables with filepaths and csv's
dftrain = pd.read_csv("/content/drive/MyDrive/assignment5_training_data_metadata.csv")
dftrain.drop('id', axis = 1, inplace=True)
trainpath = "/content/drive/MyDrive/images/train"

dftest = pd.read_csv("/content/drive/MyDrive/assignment5_test_data_metadata.csv")
testpath = "/content/drive/MyDrive/images/test"

#initializes IDG with desired settings
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=.2,
        height_shift_range=.2,
        rescale=1./255,
        shear_range=.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split = .2,
        )
#fills the healthy "Nan" slots with "normal"
dftrain.fillna("normal",inplace=True)

#intializes the training flow settings
trainAlpha =datagen.flow_from_dataframe(
    dataframe = dftrain,
    directory="/content/drive/MyDrive/images/train",
    x_col="image_name",
    y_col="type",
    subset = "training",
    batch_size = 16,
    target_size=(196, 196),
    color_mode="grayscale",
    class_mode="sparse",
    seed = 42
    )
dftrain

trainAlpha.class_indices
dftest

trainBeta = datagen.flow_from_dataframe(
    dataframe = dftrain,
    directory="/content/drive/MyDrive/images/train",
    x_col="image_name",
    y_col="type",
    subset = "validation",
    batch_size = 16,
    target_size=(196, 196),
    color_mode="grayscale",
    class_mode="sparse",
    seed = 42
    )

trainBeta.class_indices

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', input_shape=(196,196,1), activation='relu'))
model.add(Conv2D(25, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(Conv2D(32, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))
model.compile(optimizer = "Adam", loss = "sparse_categorical_crossentropy",
              metrics ="SparseCategoricalAccuracy" )

model.fit(x = trainAlpha, validation_data=trainBeta, epochs = 50)

testgen = ImageDataGenerator(rescale = 1./255)

test_gen = testgen.flow_from_dataframe(
    shuffle = False,
    target_size=(196,196),
    dataframe = dftest,
    directory="/content/drive/MyDrive/images/test",
    x_col="image_name",
    batch_size = 1,
    color_mode="grayscale",
    class_mode=None,
    )

red = pd.DataFrame({'id':dftest['id'], "type" :np.argmax(model.predict(test_gen), axis = -1)})
red.replace(3,4, inplace =True)#normal
red.replace(2,3, inplace =True)#bacteria
red.replace(1,2, inplace =True)#virus
red.replace(0,1, inplace =True)#Stress-smoking

with pd.option_context('display.max_rows', None):
  display(red)
  red.to_csv("predictions.csv", index= False)