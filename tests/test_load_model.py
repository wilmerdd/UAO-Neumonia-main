import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import patch
from load_model import model

@patch('tensorflow.keras.models.load_model')
def test_model_load_success(mock_load_model):
    # Crear un mock modelo para simular la carga exitosa
    mock_model = "Modelo de prueba"
    mock_load_model.return_value = mock_model

    # Llamar a la función model
    result = model()

    # Verificar que el resultado sea el modelo mock creado
    assert result == mock_model, "El modelo cargado no es el esperado"

    # Verificar que load_model haya sido llamado exactamente una vez con la ruta correcta del modelo
    mock_load_model.assert_called_once_with('C:/UAO-Neumonia-main/WilhemNet_86.h5')