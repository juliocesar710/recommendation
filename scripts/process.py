import numpy as np
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def preprocess_image(image_path, target_size=(299, 299)):
    """
    Carrega e pré-processa uma imagem.
    
    Args:
        image_path (str): Caminho para a imagem.
        target_size (tuple): Tamanho desejado para a imagem.
    
    Returns:
        np.array: Imagem pré-processada.
    """
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Adicionar dimensão de batch
    return preprocess_input(img_array)
