import asyncio

from bot.models import db
from config import settings


async def main():
    await db.set_bind(settings.DATABASE_CONNECTION)
    await db.gino.create_all()
    await db.pop_bind().close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
