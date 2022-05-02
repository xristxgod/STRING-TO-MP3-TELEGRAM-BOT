from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.__init__ import Favorites
from config import Config, LANGUAGES, logging, logger

storage = MemoryStorage()
bot = Bot(Config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

favorites = Favorites()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton("Set base language:", callback_data='set_language'))
    favorites.set_language(chat_id=message.from_user.id)
    await message.answer(
        (
            "<b> Welcome to our bot </b> \n"
            "He knows how to voice your text. \n"
            "Just write to him and he will voice it.\n"
            "By default, the language to be voiced in is English."
        ),
        reply_markup=keyboard_markup,
        parse_mode=types.ParseMode.HTML
    )

@dp.callback_query_handler(lambda c: c.data == 'set_language')
async def set_language(callback_query: types.CallbackQuery):
    keyboard_markup = types.InlineKeyboardMarkup()
    btn_s = []
    for language_key, language_value in LANGUAGES.items():
        btn_s.append(
            types.InlineKeyboardButton(
                f"Set base {language_value.title()}:",
                callback_data=f'language_{language_key.lower()}'
            )
        )
    keyboard_markup.row(*btn_s)
    await callback_query.message.answer(
        "Choose a language for voice-over:",
        reply_markup=keyboard_markup,
        parse_mode=types.ParseMode.HTML
    )

@dp.callback_query_handler(
    lambda c: c.data[0:9] == 'language_' and c.data[9: 11] in [_language.lower() for _language in LANGUAGES.keys()]
)
async def language(callback_query: types.CallbackQuery):
    logger.error(f"SET LANGUAGE: {callback_query.from_user.id} == {LANGUAGES.get(callback_query.data[9: 11])}")
    favorites.set_language(chat_id=callback_query.from_user.id, language=callback_query.data[9: 11])
    await callback_query.answer(
        f"Language: {LANGUAGES.get(callback_query.data[9: 11])} has been successfully installed!", True
    )

@dp.message_handler()
async def process_message(message: types.Message):
    await message.answer(message.text)