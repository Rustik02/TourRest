# Определение состояний
from aiogram.dispatcher.filters.state import StatesGroup, State


class Participants(StatesGroup):
    method = State()
    id = State()
    first_name = State()
    last_name = State()
    age = State()
    phone = State()
    tour = State()
    flights = State()
    hotels = State()



class LanguageState(StatesGroup):
    choosing_language = State()


class ModelState(StatesGroup):
    choosing_model = State()
    choosing_operation = State()
