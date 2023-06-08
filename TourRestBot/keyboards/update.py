from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def update_kb(id: int):
    kb = InlineKeyboardButton('Update', callback_data=f'post {id}')
    return InlineKeyboardMarkup().add(kb)