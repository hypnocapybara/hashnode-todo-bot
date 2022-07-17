from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from config import settings
from bot.models import db
from bot.middlewares import UserStorageMiddleware

storage = MemoryStorage()
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot, storage=storage)
Dispatcher.set_current(dispatcher)

dispatcher.middleware.setup(UserStorageMiddleware(database=db))


import bot.dialogs
