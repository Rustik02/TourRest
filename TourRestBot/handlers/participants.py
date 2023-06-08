from io import BytesIO

import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot import bot, dp
from keyboards.kb_menu import kb_menu_participants, cancel_kb
from keyboards.states import Participants


async def participants(message: types.Message):
    await message.reply("Please choose a model's command", reply_markup=kb_menu_participants)


async def create_participants(message: types.Message):
    await Participants.method.set()
    state = dp.get_current().current_state()
    async with state.proxy() as data:
        data['method'] = 'create'
    await Participants.first_name.set()
    await message.reply("Enter first name", reply_markup=cancel_kb)


async def first_name_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text

    await Participants.next()
    await message.reply("Enter last name")


async def last_name_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await Participants.next()

    await message.reply("Enter age")


async def age_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await Participants.next()
    await message.reply("Enter phone number")


async def phone_handler(message: types.Message, state: FSMContext):
    send = {}
    async with state.proxy() as data:
        data['phone'] = message.text
    send['first_name'] = data['first_name']
    send['last_name'] = data['last_name']
    send['age'] = data['age']
    send['phone'] = data['phone']
    response = requests.post(f"http://127.0.0.1:8000/api/v1/participants/", data=send)
    await bot.send_message(message.from_user.id, f"Данные добавлены в БД:\n\n"
                                                 f"First name: {response.json()['first_name']}\n"
                                                 f"Last name: {response.json()['last_name']}\n"
                                                 f"Age: {response.json()['age']}\n"
                                                 f"Phone: {response.json()['phone']}",
                           reply_markup=kb_menu_participants)
    await state.finish()


async def read_participants(message: types.Message):  # new
    posts = requests.get(f'http://127.0.0.1:8000/api/v1/participants/').json()
    for post in posts:
        text = f"""{post['first_name']}\n\n{post['last_name']}\n\n{post['age']}\n\n{post['phone']}"""
        await bot.send_message(message.from_user.id, text, reply_markup=kb_menu_participants)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Cancelled.', reply_markup=kb_menu_participants)


async def update_participants(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/v1/participants/').json()
    for i in response:
        text = (f"Данные добавлены в БД:\n\nID: "
                f"{i['id']}\n"
                f"First name: {i['first_name']}\n"
                f"Last name: {i['last_name']}\n"
                f"Age: {i['age']}\n"
                f"Phone: {i['phone']}")
        await bot.send_message(message.chat.id, text)
    await Participants.method.set()
    state = dp.get_current().current_state()
    async with state.proxy() as data:
        data['method'] = 'update'
    await Participants.id.set()
    await message.answer("Enter the ID of the destination you want to update:")


async def id_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['participants_id'] = message.text
    participants_id = data['participants_id']
    try:
        participants_id = int(participants_id)
    except ValueError:
        await message.answer("Invalid ID. Enter a number.")
        return

    await message.answer("Select the fields you want to update:")
    await message.answer("1. First name")
    await message.answer("2. Last name")
    await message.answer("3. Age")
    await message.answer("4. Phone")
    await message.answer("5. All fields")
    await message.answer("Enter the field numbers: ")
    fields = await message.text
    data = {}
    if "5" in fields:
        await message.answer("Enter a new value for the 'First name' field:")
        async with state.proxy() as data:
            data['first_name'] = message.text
        await message.answer("Enter a new value for the 'Last name' field:")
        async with state.proxy() as data:
            data['last_name'] = message.text
        await message.answer("Enter a new value for the 'Age' field:")
        async with state.proxy() as data:
            data['age'] = message.text
        await message.answer("Enter a new value for the 'Phone' field:")
        async with state.proxy() as data:
            data['phone'] = message.text
    else:
        for field in fields:
            if field.strip() == "1":
                await message.answer("Enter a new value for the 'First name' field:")
                async with state.proxy() as data:
                    data['first_name'] = message.text
            elif field.strip() == "2":
                await message.answer("Enter a new value for the 'Last name' field:")
                async with state.proxy() as data:
                    data['last_name'] = message.text
            elif field.strip() == "3":
                await message.answer("Enter a new value for the 'Age' field:")
                async with state.proxy() as data:
                    data['age'] = message.text
            elif field.strip() == "4":
                await message.answer("Enter a new value for the 'Phone' field:")
                async with state.proxy() as data:
                    data['phone'] = message.text

    url = f"http://127.0.0.1:8000/api/v1/participants/{participants_id}/"
    response = requests.put(url, json=data)
    if response.status_code == 200:
        await message.answer("Data has been successfully updated", reply_markup=kb_menu_participants)
    else:
        await message.answer("Error updating data")


async def delete_participants(message: types.Message):
    await message.answer("Enter the ID of the destination you want to delete:")
    participants_id = await bot.wait_for_message(chat_id=message.chat.id)
    try:
        participants_id = int(participants_id.text)
    except ValueError:
        await message.answer("Invalid ID. Enter a number.")
        return
    url = f"http://127.0.0.1:8000/api/v1/participants/{participants_id}/"
    response = requests.delete(url)
    if response.status_code == 204:
        await message.answer("Participant successfully deleted")
    else:
        await message.answer("Error when deleting a participant")


def register_handlers_destination(dp: Dispatcher):
    dp.register_message_handler(participants, commands=['participants'])
    '''*************************READ***************************'''
    dp.register_message_handler(read_participants, Text(equals='Read participants'))
    '''*************************CREATE***************************'''
    dp.register_message_handler(create_participants, Text(equals='Create participants'))
    dp.register_message_handler(cancel_handler, Text(equals='Cancel'), state='*')
    dp.register_message_handler(first_name_handler, state=Participants.first_name)
    dp.register_message_handler(last_name_handler, state=Participants.last_name)
    dp.register_message_handler(age_handler, state=Participants.age)
    dp.register_message_handler(phone_handler, state=Participants.phone)
    '''*************************Update***************************'''
    dp.register_message_handler(update_participants, Text(equals='Update participants'))
    dp.register_message_handler(id_handler, state=Participants.id)
    dp.register_message_handler(delete_participants, Text(equals='Delete participants'))
