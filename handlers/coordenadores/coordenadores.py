from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoEmailCoord

# @dp.message_handler(commands=['coord', 'coordenadores'])
async def email(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEmailCoord, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)



def register_handlers_coordenadores(dp: Dispatcher):
    dp.register_message_handler(email, commands=['coord', 'coordenadores'])