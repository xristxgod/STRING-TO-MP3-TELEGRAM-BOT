import os
import logging

LANGUAGES = {
    "en": "English",
    "ru": "Russian",
}

logger = logging.getLogger(__name__)

class Config(object):

    TOKEN = os.getenv("TOKEN")
