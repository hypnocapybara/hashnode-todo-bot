import asyncio

from bot.models import db
from config import settings
from bot.services import notes as notes_service


async def main():
    await db.set_bind(settings.DATABASE_CONNECTION)
    await notes_service.process_expired_notes()
    # user = await User.query.where(User.username == 'test').gino.first()
    #
    # notes = await notes_service.get_notes(user)
    #
    # note = await notes_service.add_note(user, 'Test note')
    #
    # notes = await notes_service.get_notes(user)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
