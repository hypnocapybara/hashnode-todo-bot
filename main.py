from aiogram import executor

from bot.models import db
from bot.main import dispatcher
from config import settings


async def on_startup(dispatcher):
    await db.set_bind(settings.DATABASE_CONNECTION)


async def on_shutdown(dispatcher):
    await db.pop_bind().close()


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dispatcher,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
