import os
from datetime import datetime

IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/images/"))
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/logs/"))
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y%m%d')}.log")

API_URL = "https://pokeapi.co/api/v2/pokemon/"
IMAGE_URL = "https://www.google.com/search"

QTY_IMAGES = 3