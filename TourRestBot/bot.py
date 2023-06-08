from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
BOT_TOKEN = '5945040028:AAGpfQGfPxEq8jAlv2HQs1I_8bYlOjjUr7w'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
