import numpy as np
from PIL import Image
import cv2
import pydicom as dicom

def read_dicom_file(path):
    try:
        img = dicom.read_file(path)
        img_array = img.pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show
    
    except Exception as e:
        print(f"Error reading DICOM file {path}: {str(e)}")
        return None, None

def read_jpg_file(path):
    try:
        img = cv2.imread(path)
        img_array = np.asarray(img)
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        return img2, img2show
    
    except Exception as e:
        print(f"Error reading JPEG file {path}: {str(e)}")
        return None, None