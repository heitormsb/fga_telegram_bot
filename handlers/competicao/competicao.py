from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoCompeticao

# @dp.message_handler(commands=['competicao', 'compet'])
async def competicao(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCompeticao, parse_mode=ParseMode.MARKDOWN)

def register_handlers_competicao(dp: Dispatcher):
    dp.register_message_handler(competicao, commands=['competicao', 'compet'])