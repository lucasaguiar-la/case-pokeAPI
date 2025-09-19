import requests
import os
from utils.logger import logger
from config import IMAGES_DIR

def save_images(image_links, pokemon_name):
    saved_files = []

    logger.info(f"Salvando imagens do {pokemon_name.upper()}")

    for index, link in enumerate(image_links):
        try:
            response = requests.get(link, timeout=10)
            file_path = os.path.join(IMAGES_DIR, f"{pokemon_name}_{index + 1}.jpg")

            with open(file_path, "wb") as file:
                file.write(response.content)
            saved_files.append(file_path)
        except Exception as error:
            logger.error(f"Erro ao salvar imagem {index + 1} do Pokemon {pokemon_name.upper()}: {error}")

    return saved_files
