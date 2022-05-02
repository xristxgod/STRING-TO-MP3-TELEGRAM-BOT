import os
import logging

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(ROOT_DIR, "files")
if "files" not in os.listdir(ROOT_DIR):
    os.mkdir(BASE_DIR)

LANGUAGES = {
    "en": "English",
    "ru": "Russian"
}

logger = logging.getLogger(__name__)

class Config(object):
    # Bot token
    TOKEN = os.getenv("TOKEN")