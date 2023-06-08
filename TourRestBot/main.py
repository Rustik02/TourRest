from aiogram import types
from aiogram.utils import executor
from bot import dp
from handlers import participants
from handlers.start import start_command


@dp.message_handler(commands=['start'])
async def start_wrapper(message: types.Message):
    await start_command(message)

participants.register_handlers_destination(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
