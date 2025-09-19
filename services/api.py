import requests
from utils.logger import logger
from config import (
    API_URL,
    IMAGES_DIR
)
from datetime import datetime
from time import sleep

def get_pokemon(pokemon_id):
    sleep(0.5)
    INDEX = datetime.now().strftime("%Y%m%d%H%M%S")
    url = f"{API_URL}{pokemon_id}"

    logger.info(f"Buscando Pokemon ID: {pokemon_id}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Pokemon encontrado: {data['name'].upper()}")

        return {
            "run_id": INDEX,
            "pokemon_id": data["id"],
            "name": data["name"].upper(),
            "types": data["types"][0]["type"]["name"],
            "height": data["height"],
            "weight": data["weight"],
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "sp_atk": data["stats"][3]["base_stat"],
            "sp_def": data["stats"][4]["base_stat"],
            "speed": data["stats"][5]["base_stat"],
            "api_source": API_URL,
            "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "images_folder": IMAGES_DIR
        }

    except Exception as error:
        logger.error(
            f"Erro ao buscar pokemon! ID: {pokemon_id}\nInfo: {error}"
        )
        return None