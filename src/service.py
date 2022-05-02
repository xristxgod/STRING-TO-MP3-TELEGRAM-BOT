import typing

from langdetect import detect

from config import LANGUAGES, logger

def identify_language(text: str) -> typing.Union[str, None]:
    """
    The function for determining the language.
    :param text: Text for language detection
    """
    try:
        language = detect(text)
        return language if language in [_language for _language in LANGUAGES.keys()] else None
    except Exception as error:
        logger.error(f"ERROR: {error}")
        return None

if __name__ == '__main__':
   assert identify_language("Привет, давай я тебе расскажу кое что!!") == "ru"
   assert identify_language("Hello world!") == "en"