from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoEJ

# @dp.message_handler(commands=['ej', 'ejs'])
async def ej(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEJ, parse_mode=ParseMode.MARKDOWN)

def register_handlers_ej(dp: Dispatcher):
    dp.register_message_handler(ej, commands=['ej', 'ejs'])