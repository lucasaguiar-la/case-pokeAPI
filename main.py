import os
import random
from datetime import datetime
from utils.logger import logger
from services.api import get_pokemon
from services.image_getter import get_images

DEBUG=False

if __name__ == "__main__":
    logger.info(f"Programa inciado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    os.makedirs("/data/excel", exist_ok=True)
    os.makedirs("/data/images", exist_ok=True)

    ids = random.sample(range(1, 800), 3)
    logger.info(f"IDs sorteados: {ids}")

    poke_data = []
    for id in ids:
        data = get_pokemon(id)

        if data:
            if DEBUG:
                logger.info(
                    f"\nID: {data['run_id']}"
                    f"\n{data['name'].upper()} EU ESCOLHO VOCÊÊ!!!"
                    f"\nHP: {data['hp']}"
                    f"\nTipo: {data['types']}"
                    f"\nAltura: {data['height']}"
                    f"\nPeso: {data['weight']}"
                    f"\nAtaque: {data['attack']}"
                    f"\nDefesa: {data['defense']}"
                    f"\nAtaque especial: {data['sp_atk']}"
                    f"\nDefesa especial: {data['sp_def']}"
                    f"\nVelocidade: {data['speed']}\n"
                )

            images = get_images(data["name"])
            poke_data.append(data)
        
        if poke_data:
            ...

    logger.info(f"Programa finalizado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

