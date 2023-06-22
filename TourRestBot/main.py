import logging
import requests
from PIL import Image
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import io

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота и диспетчера
bot = Bot(token='5945040028:AAFBmm5tSsQiXujlZPaSkojXXcz3gaIMNn0')
dp = Dispatcher(bot)

# URL REST API для получения туров
tours_api_url = 'http://127.0.0.1:8000/api/v1/tours/'

# URL REST API для получения деталей тура
tour_details_api_url = 'http://127.0.0.1:8000/api/v1/tourdetails/'

# URL REST API для бронирования
booking_api_url = 'http://127.0.0.1:8000/api/v1/booking/'


def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Посмотреть", callback_data="view_tours"))
    return keyboard


# Функция создания клавиатуры тура
def tour_keyboard(tour_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Показать детали", callback_data=f"tour_detail_{tour_id}"))
    return keyboard


# Функция создания клавиатуры турдеталей
def tour_detail_keyboard(tour_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Забронировать", callback_data=f"book_tour_{tour_id}"))
    return keyboard


# Функция для выполнения запроса к REST API
def make_api_request(url, method='GET', data=None):
    global response
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, data=data)
    if response.status_code == 200:
        return response
    return None


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    view_tours_button = InlineKeyboardButton(text="Посмотреть", callback_data='view_tours')
    keyboard.add(view_tours_button)
    await message.reply("Привет! Для просмотра действующих туров нажми кнопку 'Посмотреть'.", reply_markup=keyboard)


# Обработчик нажатия на кнопку

async def process_booking_data(message: types.Message, tour_id: int):
    name = message.text
    phone_number = message.contact.phone_number if message.contact else None
    booking_data = {
        'tour_id': tour_id,
        'name': name,
        'phone': phone_number
    }

    response = make_api_request(booking_api_url, method='POST', data=booking_data)
    if response:
        await message.reply("Ваши данные успешно отправлены.")
    else:
        await message.reply("Произошла ошибка при отправке данных.")


# Обработчик нажатия на кнопку тура
@dp.callback_query_handler(lambda query: query.data == 'view_tours')
async def tour_button_handler(query: types.CallbackQuery):
    tour_url = f'{tours_api_url}'
    tour_data_list = make_api_request(tour_url).json()

    if tour_data_list:
        for tour_data in tour_data_list:
            title = tour_data['title']
            description = tour_data['description']
            image_url = tour_data['image']

            # Загрузка изображения
            print(image_url)
            image_data = make_api_request(image_url, method='GET')
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                # Отправка изображения
                await bot.send_photo(query.message.chat.id, photo=image)

            text = f"Title: {title}\n"
            text += f"Description: {description}\n"

            keyboard = InlineKeyboardMarkup()
            button_text = "Показать детали"
            callback_data = f'tour_detail'
            keyboard.add(InlineKeyboardButton(text=button_text, callback_data=callback_data))

            message = await bot.send_message(query.message.chat.id, text, reply_markup=keyboard)
    else:
        await query.message.reply("Произошла ошибка при получении данных о туре.")


@dp.callback_query_handler(lambda query: query.data.startswith('tour_detail_'))
async def tour_detail_button_handler(query: types.CallbackQuery):
    tour_id = query.data.split('_')[2]
    tour_detail_url = f'{tour_details_api_url}{tour_id}/'
    tour_detail_data = make_api_request(tour_detail_url)
    if tour_detail_data:
        duration = tour_detail_data['duration']
        group_size = tour_detail_data['group_size']
        difficulty_level = tour_detail_data['difficulty_level']
        start_date = tour_detail_data['start_date']
        seasons = ', '.join(tour_detail_data['seasons'])
        itinerary = tour_detail_data['itinerary']
        highlights = tour_detail_data['highlights']
        price_includes = tour_detail_data['price_includes']

        text = f"Duration: {duration} days\n"
        text += f"Group size: {group_size}\n"
        text += f"Difficulty level: {difficulty_level}\n"
        text += f"Start date: {start_date}\n"
        text += f"Seasons: {seasons}\n"
        text += f"Itinerary: {itinerary}\n"
        text += f"Highlights: {highlights}\n"
        text += f"Price includes: {price_includes}\n"

        await query.message.reply(text)
    else:
        await query.message.reply("Произошла ошибка при получении данных о турдеталях.")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
