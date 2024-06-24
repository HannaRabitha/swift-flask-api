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
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image, ImageFilter
from skimage.filters import median, unsharp_mask

from tensorflow.keras.models import load_model
import utils as ut
import subprocess


REPO_URL = 'https://github.com/HannaRabitha/model-sarang-walet.git'
REPO_DIR = 'model-sarang-walet'

# Clone the repository
if not os.path.exists(REPO_DIR):
    subprocess.run(['git', 'clone', REPO_URL])

# Function to find the model file
def find_model_file(repo_dir, extension=".h5"):
    for root, dirs, files in os.walk(repo_dir):
        for file in files:
            if file.endswith(extension):
                return os.path.join(root, file)
    return None

# Get the model path
MODEL_PATH = find_model_file(REPO_DIR)
if MODEL_PATH is None:
    raise FileNotFoundError("Model file not found in the repository")


class Classification:

    def start_classification(self, img_path, target_size=(380, 380)):
        img = load_img(img_path, target_size=target_size)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  
        img_array /= 255.0  
    
        model = load_model(MODEL_PATH)
    
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return predicted_class