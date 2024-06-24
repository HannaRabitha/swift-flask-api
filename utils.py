import os
import cv2
import json
import numpy as np
import numpy as np
import pandas as pd
from os import listdir
import tensorflow as tf
import matplotlib as mpl
from os.path import isfile, join
from keras.models import model_from_json
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import EfficientNetB4
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img


class utils:
    def load_and_preprocess_image(img_path, target_size=(380, 380)):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  
        img_array /= 255.0  
        return img_array
    
    def getmodel(MODEL_LOC):
        model = load_model(MODEL_LOC)
        return model
    
    def prediction(model,img_array):
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return predicted_class


def load_and_preprocess_image(img_path, target_size=(380, 380)):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  
        img_array /= 255.0  
    
        model = load_model(MODEL_LOC)
    
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return predicted_class