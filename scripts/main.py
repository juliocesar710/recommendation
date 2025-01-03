import os
from scripts.preprocess import preprocess_image
from scripts.utils import load_model, find_similar_images
from PIL import Image

# Configurações
INPUT_IMAGE = "data/input/input_image.jpg"
OUTPUT_DIR = "data/output/"
MODEL_PATH = "models/pretrained/inception_v3.h5"

# Carregar o modelo pré-treinado
model = load_model(MODEL_PATH)

# Processar imagem de entrada
processed_image = preprocess_image(INPUT_IMAGE)

# Encontrar imagens similares
similar_images = find_similar_images(model, processed_image)

# Salvar resultados
os.makedirs(OUTPUT_DIR, exist_ok=True)
for idx, img_path in enumerate(similar_images):
    output_path = os.path.join(OUTPUT_DIR, f"similar_image_{idx + 1}.jpg")
    Image.open(img_path).save(output_path)

print(f"Imagens similares salvas em {OUTPUT_DIR}")
