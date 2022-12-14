from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from .text import textoOuvidoria, textoPrivadoOnly

class Form(StatesGroup):
    ouvidoriaMsg = State()  # Will be represented in storage as 'Form:ouvidoriaMsg'


# @dp.message_handler(commands=['ouvidoria'])
async def ouvidoria(message: types.Message):
    from main import bot
    print(message)
    if message.chat.type == 'private':
      await Form.ouvidoriaMsg.set()
      await bot.send_message(message.from_user.id, textoOuvidoria, parse_mode=ParseMode.MARKDOWN)
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
      await bot.send_message(message.from_user.id, textoPrivadoOnly, parse_mode=ParseMode.MARKDOWN)
      

# @dp.message_handler(state=Form.ouvidoriaMsg)
async def process_ouvidoria(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ouvidoriaMsg'] = message.text

    await message.send_copy(-1001767954388, data['ouvidoriaMsg'])
    await state.finish()


def register_handlers_ouvidoria(dp: Dispatcher):
    dp.register_message_handler(ouvidoria, commands="ouvidoria", state="*")
    dp.register_message_handler(process_ouvidoria, state=Form.ouvidoriaMsg)