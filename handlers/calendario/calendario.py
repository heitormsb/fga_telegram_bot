from aiogram import Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from .text import textoCalend

buttonCalendMatricula = InlineKeyboardButton(text='Calendario de Matricula', callback_data='calendario_matricula2022')
buttonCalendAtividade = InlineKeyboardButton(text='Calendario de Atividades', callback_data='calendario_atividades2022')
keybCalends = InlineKeyboardMarkup().add(buttonCalendMatricula, buttonCalendAtividade)


# @dp.message_handler(commands=['calendario', 'calend'])
async def calendario(message: types.Message):
    from main import bot

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCalend, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybCalends)

# @dp.callback_query_handler(text=['calendario_atividades2022', 'calendario_matricula2022'])
async def fluxos(call: types.CallbackQuery):
    from main import bot
    if call.data == "calendario_atividades2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Atividades/2022_2/2022_2_Calend_Atv_Grad_28_09_22.pdf')
    if call.data == "calendario_matricula2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Matricula/2022_2/2022_2_Calend_Matricula_Grad.pdf')
   

def register_handlers_calendario(dp: Dispatcher):
    dp.register_message_handler(calendario, commands=['calendario', 'calend'])
    dp.register_callback_query_handler(fluxos, text=['calendario_atividades2022', 'calendario_matricula2022'])