import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from preprocess_img import preprocess
import grad_cam
import preprocess_img
import load_model

def predict(array):
    #   1. call function to pre-process image: it returns image in batch format
    batch_array_img = preprocess_img.preprocess(array)
    #   2. call function to load model and predict: it returns predicted class and probability
    #model = model_fun()
    model = load_model.model()
    # model_cnn = tf.keras.models.load_model('conv_MLP_84.h5')
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    elif prediction == 1:
        label = "normal"
    elif prediction == 2:
        label = "viral"
    #   3. call function to generate Grad-CAM: it returns an image with a superimposed heatmap
    heatmap = grad_cam.grad_cam(array)
    return (label, proba, heatmap)