from aiogram import types
from aiogram.utils.emoji import emojize

from bot.texts import KEYBOARDS


def main_keyboard() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton(emojize(KEYBOARDS['list_notes'])),
        types.KeyboardButton(emojize(KEYBOARDS['add_note']))
    )
    return markup


def cancel_keyboard() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton(emojize(KEYBOARDS['cancel'])))
    return markup
