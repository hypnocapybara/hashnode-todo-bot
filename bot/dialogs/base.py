from typing import TYPE_CHECKING
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.emoji import emojize

from bot.texts import KEYBOARDS, RESPONSES
from bot.keyboards import main_keyboard

if TYPE_CHECKING:
    from bot.models import User


dp = Dispatcher.get_current()


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, user: 'User'):
    await message.answer(
        RESPONSES['welcome'].format(user=user.first_name),
        reply_markup=main_keyboard(),
    )


@dp.message_handler(commands='cancel', state='*')
@dp.message_handler(Text(equals=emojize(KEYBOARDS['cancel'])), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        RESPONSES['cancel'],
        reply_markup=main_keyboard(),
    )
