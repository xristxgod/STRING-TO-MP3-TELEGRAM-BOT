import os
from pathlib import Path

from config import MP3_FILE_PATH, logger

class Utils:

    @staticmethod
    def del_mp3_file() -> bool:
        try:
            logger.error("START DEL MP3 FILE!")
            if Path(MP3_FILE_PATH).is_file():
                logger.error("[-] THE MP3 FILE HAS BEEN DELETED!")
                os.remove(MP3_FILE_PATH)
            else:
                logger.error("THE FILE WAS NOT FOUND!")
            return True
        except Exception as error:
            logger.error(f"ERROR: {error}")
            return False

    @staticmethod
    def check_token(token: str) -> bool:
        """
        Checks whether the token is similar to the token for the bot.
        :param token: Bot token @BotFather
        :return:
        """
        if 46 > len(token) > 46:
            return False
        elif not token[:10].isdigit():
            return False
        elif token.find(":") < 0:
            return False
        return True