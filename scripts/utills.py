import numpy as np
from tensorflow.keras.models import load_model
from scipy.spatial.distance import cdist

def load_model(model_path):
    """
    Carrega o modelo pré-treinado.
    
    Args:
        model_path (str): Caminho para o modelo salvo.
    
    Returns:
        keras.Model: Modelo carregado.
    """
    return load_model(model_path)

def find_similar_images(model, image, dataset_features, dataset_paths, top_n=5):
    """
    Encontra imagens similares com base nas características.

    Args:
        model (keras.Model): Modelo para extração de características.
        image (np.array): Imagem pré-processada.
        dataset_features (np.array): Características do dataset.
        dataset_paths (list): Caminhos das imagens do dataset.
        top_n (int): Número de imagens similares a retornar.

    Returns:
        list: Caminhos das imagens similares.
    """
    query_features = model.predict(image)
    distances = cdist(query_features, dataset_features, metric='euclidean')[0]
    indices = np.argsort(distances)[:top_n]
    return [dataset_paths[idx] for idx in indices]
