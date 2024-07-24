import tensorflow as tf
from tensorflow.keras import models, losses

def model():
    try:
        model_cnn = tf.keras.models.load_model('C:/UAO-Neumonia-main/WilhemNet_86.h5')        
        return model_cnn
    except OSError as e:
        print(f"Error al cargar el modelo: {e}")
        return None
