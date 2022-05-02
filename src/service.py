import os
import typing
from pathlib import Path

from gtts import gTTS
from langdetect import detect

from config import LANGUAGES, MP3_FILE_PATH, logger

def identify_language(text: str) -> typing.Union[str, None]:
    """
    The function for determining the language.
    :param text: Text for language detection
    """
    try:
        return detect(text)
    except Exception as error:
        logger.error(f"ERROR: {error}")
        return None

def str_to_mp3(text: str, language="en") -> typing.Union[str, None]:
    try:
        logger.error("STR TO MP3 STARTS")
        logger.error("PROCESSING...")
        audio = gTTS(
            text=text,
            lang=language if language in [_language for _language in LANGUAGES.keys()] else "ru",
            slow=False
        )
        audio.save(MP3_FILE_PATH)
        logger.error("[+] MP3 FILE SAVED SUCCESSFULLY!")
        return MP3_FILE_PATH
    except Exception as error:
        logger.error(f"ERROR: {error}")
        return None