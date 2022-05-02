from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.__init__ import Favorites
from config import Config, logging

storage = MemoryStorage()
bot = Bot(Config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

favorites = Favorites()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer((
        "Welcome to our bot. \n"
        "He knows how to voice your text. \n"
        "Just write to him and he will voice it."
    ))