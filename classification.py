import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import EfficientNetB4
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Precision, Recall
import tensorflow_addons as tfa
from sklearn.metrics import precision_score, recall_score, f1_score
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image, ImageFilter
from skimage.filters import median, unsharp_mask

import utils as ut


MODEL_LOC = 'model-sarang-walet.h5'
# WEIGHT_LOC = 'db/weights.h5'
# LABEL_LOC = 'db/label.json'
# img_path = 'path_to_your_image.jpg'

class Classification:

    # def __init__(self, img_path):
    #     self.img_path = img_path

    # def start_classification(self):
    #     #load and preprocessing
    #     img_array = ut.load_and_preprocess_image(self.img_path)
        
    #     #get model data
    #     model = ut.getmodel(MODEL_LOC)
        
    #     # Predict the class
    #     predictions = ut.prediction(model,img_array)
    #     print(predictions)
    #     return predictions

    def start_classification(self, img_path, target_size=(380, 380)):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  
        img_array /= 255.0  
    
        model = load_model(MODEL_LOC)
    
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return predicted_class