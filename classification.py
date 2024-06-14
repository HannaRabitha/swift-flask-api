import os
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

import utils as ut


MODEL_LOC = 'db/model.json'
WEIGHT_LOC = 'db/weights.h5'
LABEL_LOC = 'db/label.json'
img_path = 'path_to_your_image.jpg'

class classification:

    def start_classification(img_path):
        #load and preprocessing
        img_array = ut.load_and_preprocess_image(img_path)
        
        #get model data
        model = ut.getmodel(MODEL_LOC)
        
        # Predict the class
        predictions = ut.prediction(model,img_array)
        return predictions