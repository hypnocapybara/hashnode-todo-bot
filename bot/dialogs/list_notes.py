from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.emoji import emojize

from bot.texts import KEYBOARDS
from bot.models import User
from bot.services import notes as notes_service
from bot.keyboards import main_keyboard


dp = Dispatcher.get_current()


@dp.message_handler(Text(equals=emojize(KEYBOARDS['list_notes'])))
async def handler_list_notes(message: types.Message, user: User):
    notes = await notes_service.get_notes(user)

    if not notes:
        answer_text = "You don't have any actual notes"
    else:
        notes_text = '\n\n'.join([
            f'{n.created_at.isoformat()}\n{n.text}' for n in notes
        ])
        answer_text = 'Your notes:\n\n' + notes_text

    await message.answer(
        answer_text,
        reply_markup=main_keyboard()
    )
