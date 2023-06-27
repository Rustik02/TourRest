import logging
import requests
from PIL import Image
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import io

# Создание экземпляра бота и диспетчера
bot = Bot(token='5945040028:AAFBmm5tSsQiXujlZPaSkojXXcz3gaIMNn0')
dp = Dispatcher(bot)

tours_api_url = 'http://127.0.0.1:8000/api/v1/tours/'

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот. Как могу помочь?")


if __name__ == '__main__':
    executor.start_polling(dp)
