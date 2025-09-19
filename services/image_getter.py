import requests
from config import IMAGE_URL
from bs4 import BeautifulSoup
from config import QTY_IMAGES
from utils.logger import logger

def get_images(pokemon_name):
    url = f"{IMAGE_URL}?q={pokemon_name}+pokemon&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0"}

    logger.info(f"Buscando imagens do Pokemon {pokemon_name.upper()}")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        images = [
            img["src"]
            for img in soup.find_all("img")
            if "src" in img.attrs
        ]
        return images[:QTY_IMAGES]

    except Exception as error:
        logger.error(f"Erro ao buscar imagens do Pokemon {pokemon_name.upper()}: {error}")
