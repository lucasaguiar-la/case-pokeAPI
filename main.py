import os
import random
from datetime import datetime
from utils.logger import logger
from config import (
    QUANTITY_IDS,
    IMAGES_DIR,
    EXCEL_DIR
)
from services.api import get_pokemon
from services.image_getter import get_images
from services.image_saver import save_images
from services.spreadsheet_saver import save_excel

if __name__ == "__main__":
    logger.info(f"Programa inciado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    os.makedirs(EXCEL_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR , exist_ok=True)

    ids = random.sample(range(1, 800), QUANTITY_IDS)
    logger.info(f"IDs sorteados: {ids}")

    poke_data = []
    images_data = []

    for pokemon_id in ids:
        poke_info = get_pokemon(pokemon_id)

        if poke_info:
            image_links = get_images(poke_info["name"])
            saved_images_details = save_images(
                image_links,
                poke_info["run_id"],
                poke_info["pokemon_id"],
                poke_info["name"]
            )

            poke_data.append(poke_info)
            images_data.extend(saved_images_details)

    if poke_data and images_data:
        save_excel(poke_data, images_data)

    logger.info(f"Programa finalizado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

