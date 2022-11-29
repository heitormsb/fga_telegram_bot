from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoCredito

# @dp.message_handler(commands=['creditos', 'credito'])
async def creditos(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCredito, parse_mode=ParseMode.MARKDOWN)

def register_handlers_creditos(dp: Dispatcher):
    dp.register_message_handler(creditos, commands=['creditos', 'credito'])