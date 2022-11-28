from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import texto

# @dp.message_handler(commands=['ajuda', 'menu', 'help', 'start'])
async def ajuda(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await message.answer(texto, parse_mode=ParseMode.MARKDOWN)


def register_handlers_ajuda(dp: Dispatcher):
    dp.register_message_handler(ajuda, commands=['ajuda', 'menu', 'help', 'start'], state="*")