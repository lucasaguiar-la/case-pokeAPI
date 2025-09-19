import requests
import os
from utils.logger import logger
from config import IMAGES_DIR
from time import sleep
from datetime import datetime

def save_images(image_links, run_id, pokemon_id, pokemon_name):
    image_details  = []
    sleep(0.5)
    INDEX = datetime.now().strftime("%Y%m%d%H%M%S")

    logger.info(f"Salvando imagens do {pokemon_name.upper()}")

    for index, link in enumerate(image_links):
        file_path = os.path.join(IMAGES_DIR, f"{pokemon_name}_{index + 1}.jpg")
        details = {
            "run_id": run_id,
            "pokemon_id": pokemon_id,
            "image_index": INDEX,
            "image_url": link,
            "local_path": None,
            "download_status": "Failed"
        }

        try:
            response = requests.get(link, timeout=10)
            response.raise_for_status()

            with open(file_path, "wb") as file:
                file.write(response.content)

            details["local_path"] = file_path
            details["download_status"] = "Success"
        except Exception as error:
            logger.error(f"Erro ao salvar imagem {index + 1} do Pokemon {pokemon_name.upper()}: {error}")
        
        image_details.append(details)

    return image_details
