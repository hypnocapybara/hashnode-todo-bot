from datetime import datetime, timedelta
from typing import List

from bot.models import User, Note


async def add_note(user: 'User', text: str) -> 'Note':
    return await Note.create(
        user_id=user.id,
        text=text
    )


async def get_notes(user: 'User') -> List['Note']:
    return await Note.query.where(Note.user_id == user.id).gino.all()


async def process_expired_notes():
    await Note.delete.where(
        Note.created_at < datetime.now() - timedelta(days=1)
    ).gino.status()
