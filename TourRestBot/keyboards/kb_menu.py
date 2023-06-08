from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

creat_participants = KeyboardButton('Create participants')
read_participants = KeyboardButton('Read participants')
update_participants = KeyboardButton('Update participants')
delete_participants = KeyboardButton('Delete participants')
back_participants = KeyboardButton('🔙 Back')

kb_menu_participants = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu_participants.row(creat_participants, read_participants).row(update_participants, delete_participants).add(back_participants)

cancel = KeyboardButton('Cancel')
cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_kb.add(cancel)