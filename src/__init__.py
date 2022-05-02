import typing

class Favorites:

    def __init__(self):
        self.favorites_list: typing.List[typing.Dict] = []

    def set_language(self, chat_id: int, language: str):
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