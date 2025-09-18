import requests
from utils.logger import logger
from config import API_URL

def get_pokemon(pokemon_id):
    url = f"{API_URL}{pokemon_id}"
    logger.info(f"Quem é esse Pokemon? ID: {pokemon_id}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except Exception as error:
        logger.error(
            f"Erro ao buscar pokemon! ID: {pokemon_id}\nInfo: {error}"
        )
        return None