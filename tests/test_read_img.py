import pytest
from unittest.mock import patch, MagicMock
import numpy as np
from PIL import Image
import cv2
import pydicom as dicom
from read_img import read_dicom_file, read_jpg_file

# Mock para simular pydicom.read_file
@patch('read_img.dicom.read_file')
def test_read_dicom_file(mock_read_file):
    # Configurar el mock para devolver un objeto dicom simulado
    mock_dicom = MagicMock()
    mock_dicom.pixel_array = np.array([[255, 0], [0, 255]])  # Simulación de un array de píxeles
    mock_read_file.return_value = mock_dicom
    
    # Llamar a la función read_dicom_file con un path ficticio
    path = '/path/to/fake.dcm'
    img_RGB, img2show = read_dicom_file(path)
    
    # Verificar que la función retorna valores correctos
    assert isinstance(img_RGB, np.ndarray), "img_RGB debería ser un numpy array"
    assert isinstance(img2show, Image.Image), "img2show debería ser una instancia de PIL Image"

    # Verificar que se llamó a read_file con el path correcto
    mock_read_file.assert_called_once_with(path)

# Mock para simular cv2.imread
@patch('read_img.cv2.imread')
def test_read_jpg_file(mock_imread):
    # Configurar el mock para devolver una imagen simulada
    mock_img = np.array([[255, 0], [0, 255]])  # Simulación de una imagen
    mock_imread.return_value = mock_img
    
    # Llamar a la función read_jpg_file con un path ficticio
    path = '/path/to/fake.jpg'
    img2, img2show = read_jpg_file(path)
    
    # Verificar que la función retorna valores correctos
    assert isinstance(img2, np.ndarray), "img2 debería ser un numpy array"
    assert isinstance(img2show, Image.Image), "img2show debería ser una instancia de PIL Image"

    # Verificar que se llamó a imread con el path correcto
    mock_imread.assert_called_once_with(path)

# Ejecutar las pruebas si este archivo es ejecutado directamente
if __name__ == '__main__':
    pytest.main()
