from aiogram import types

from bot import bot


# Handler for the /start command
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Please choose a models command:")

