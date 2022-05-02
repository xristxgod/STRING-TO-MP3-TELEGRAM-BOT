import typing
import os

from gtts import gTTS
from langdetect import detect

from config import LANGUAGES, BASE_DIR, logger

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

def str_to_mp3(username: str, text: str, language="en") -> typing.Union[str, None]:
    """
    Convert from string to audio file
    :param username: Username
    :param text: Text for voicing.
    :param language: The language for voicing.
    :return:
    """
    try:
        logger.error("STR TO MP3 STARTS")
        logger.error("PROCESSING...")
        audio = gTTS(
            text=text,
            lang=language if language in [_language for _language in LANGUAGES.keys()] else "ru",
            slow=False
        )
        audio_file = os.path.join(BASE_DIR, f"{username}-audio.mp3")
        audio.save(audio_file)
        logger.error("[+] MP3 FILE SAVED SUCCESSFULLY!")
        return audio_file
    except Exception as error:
        logger.error(f"ERROR: {error}")
        return None