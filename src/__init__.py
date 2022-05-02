import typing

from src.utils import Utils
from config import Config as setting

class Favorites:

    def __init__(self):
        self.favorites_list: typing.List[typing.Dict] = []

    def set_language(self, chat_id: int, language: str = "en"):
        for favorite in self.favorites_list:
            if favorite.get("id") == chat_id:
                favorite["language"] = language
                break
        else:
            self.favorites_list.append({
                "id": chat_id,
                "language": language
            })

    def clear_favorites(self):
        self.favorites_list = []

    def get_favorite(self, chat_id):
        for favorite in self.favorites_list:
            if favorite.get("id") == chat_id:
                break
        else:
            self.set_language(chat_id=chat_id)

class Config:

    def __init__(self):
        self.token = None

    def set(self, token: str = None):
        if token is None:
            self.token = setting.TOKEN
        elif Utils.check_token(token=token):
            self.token = token
        else:
            raise Exception("This token is not suitable. The correct token can be obtained here: @BotFather")

    @property
    def get(self):
        return self.token

    def delete(self):
        del self.token

cnf = Config()