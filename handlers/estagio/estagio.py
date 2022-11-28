from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoEstagio

# @dp.message_handler(commands=['estagio', 'estagios'])
async def estagio(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEstagio, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

def register_handlers_estagio(dp: Dispatcher):
    dp.register_message_handler(estagio, commands=["estagio", "estagios"])