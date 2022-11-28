from aiogram import Dispatcher, types
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttonSW = InlineKeyboardButton(text='Software 2017', callback_data='fluxo_software2017') #2017
buttonAE = InlineKeyboardButton(text='Aeroespacial 2018' , callback_data='fluxo_aeroespacial2018') #2018
buttonEN = InlineKeyboardButton(text='Energia 2018' , callback_data='fluxo_energia2018') #2018
buttonAT = InlineKeyboardButton(text='Automotiva 2018' , callback_data='fluxo_automotiva2018') #2018
buttonET = InlineKeyboardButton(text='Eletrônica 2019' , callback_data='fluxo_eletronica2019') #2019
buttonET_2021 = InlineKeyboardButton(text='Eletrônica 2021' , callback_data='fluxo_eletronica_2021') #2021

keybFluxos = InlineKeyboardMarkup().add(buttonSW).add(buttonAE).add(buttonAT).add(buttonET,buttonET_2021).add(buttonEN)

async def fluxos(message: types.Message):
    from main import bot
    textoFluxo = """
    *FLUXO DOS CURSOS:*
    """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoFluxo, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybFluxos)


# @dp.callback_query_handler(text=['fluxo_software2017', 'fluxo_aeroespacial2018', 'fluxo_energia2018', 'fluxo_automotiva2018', 'fluxo_eletronica2019', 'fluxo_eletronica_2021'])
async def fluxosC(call: types.CallbackQuery):
    from main import bot
    if call.data == "fluxo_software2017":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_software.pdf')
    if call.data == "fluxo_aeroespacial2018":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_aeroespacial.pdf')
    if call.data == "fluxo_energia2018":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7b6e0660caee2831dc77ff1586f4715eaa6e8e69/fluxos/fluxo_energia.pdf')
    if call.data == "fluxo_automotiva2018":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_automativa.pdf')
    if call.data == "fluxo_eletronica2019":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/61e728d0d1209e469aaae3067d93d20725e003da/fluxos/fluxo_eletronica.pdf')
    if call.data == "fluxo_eletronica_2021":
      await bot.send_document(call.message.chat.id, 'https://github.com/heitormsb/fga_telegram_bot/raw/main/fluxos/fluxo_eletronica_2021.pdf')

def register_handlers_fluxos(dp: Dispatcher):
    dp.register_message_handler(fluxos, commands=['fluxo', 'fluxos'], state="*")
    dp.register_callback_query_handler(fluxosC, text=['fluxo_software2017', 'fluxo_aeroespacial2018', 'fluxo_energia2018', 'fluxo_automotiva2018', 'fluxo_eletronica2019', 'fluxo_eletronica_2021'])

