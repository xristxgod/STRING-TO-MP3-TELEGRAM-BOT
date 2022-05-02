import os
from pathlib import Path

from config import BASE_DIR, logger

class Utils:

    @staticmethod
    def del_mp3_file(username) -> bool:
        try:
            logger.error("START DEL MP3 FILE!")
            if Path(os.path.join(BASE_DIR, f"{username}-audio.mp3")).is_file():
                logger.error("[-] THE MP3 FILE HAS BEEN DELETED!")
                os.remove(os.path.join(BASE_DIR, f"{username}-audio.mp3"))
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