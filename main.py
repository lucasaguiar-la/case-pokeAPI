import os
import random
from utils.logger import logger
from services.api import get_pokemon

if __name__ == "__main__":
    os.makedirs("/data/excel", exist_ok=True)
    os.makedirs("/data/images", exist_ok=True)

    logger.info("Programa inciado")

    ids = random.sample(range(1, 800), 3)
    logger.info(f"IDs sorteados: {ids}")

    poke_data = []
    for id in ids:
        data = get_pokemon(id)

        if data:
            logger.info(f"{data['name'].upper()} EU ESCOLHO VOCÊÊ!!!")