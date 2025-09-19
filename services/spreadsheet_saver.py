import openpyxl
import pandas as pd
from utils.logger import logger
from config import EXCEL_FILE

def save_excel(poke_data, images_data):
    logger.info(f"Criando DataFrames...")

    try:
        df_pokemons = pd.DataFrame(poke_data)
        df_images = pd.DataFrame(images_data)

        logger.info(f"Salvando dados em planilha: {EXCEL_FILE}")

        with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl") as writer:
            df_pokemons.to_excel(writer, sheet_name="Pokemons", index=False)
            df_images.to_excel(writer, sheet_name="Imagens", index=False)
        
        logger.info(f"Arquivo excel criado com sucesso em: {EXCEL_FILE}")

    except Exception as error:
        logger.error(f"Erro ao salvar dados em planilha: {error}")
