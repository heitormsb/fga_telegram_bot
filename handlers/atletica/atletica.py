from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from .text import textoAtletica

# @dp.message_handler(commands=['atletica', 'atleticas'])
async def atletica(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoAtletica, parse_mode=ParseMode.MARKDOWN)

def register_handlers_atletica(dp: Dispatcher):
    dp.register_message_handler(atletica, commands=['atletica', 'atleticas'])