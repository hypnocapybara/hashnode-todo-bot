from typing import TYPE_CHECKING
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.emoji import emojize
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.texts import KEYBOARDS, RESPONSES
from bot.keyboards import cancel_keyboard, main_keyboard
from bot.services import notes as notes_service

if TYPE_CHECKING:
    from bot.models import User


dp = Dispatcher.get_current()


class AddNoteState(StatesGroup):
    enter_text = State()


@dp.message_handler(Text(equals=emojize(KEYBOARDS['add_note'])))
async def handler_add_note(message: types.Message):
    await AddNoteState.enter_text.set()
    await message.answer(
        RESPONSES['add_note']['prompt'],
        reply_markup=cancel_keyboard(),
    )


@dp.message_handler(state=AddNoteState.enter_text)
async def handler_note_text(message: types.Message, state: FSMContext, user: 'User'):
    await notes_service.add_note(user, message.text)
    await state.finish()
    await message.answer(
        RESPONSES['add_note']['success'],
        reply_markup=main_keyboard(),
    )
