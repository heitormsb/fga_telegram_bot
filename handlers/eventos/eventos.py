from aiogram import Dispatcher, types
from aiogram.types import ParseMode
from telegram_bot_calendar import DetailedTelegramCalendar
from datetime import date, timedelta
from aiogram.dispatcher.filters import IDFilter


max_date = date.today() + timedelta(days=365*2)

LSTEP = {'y': 'ano', 'm': 'mês', 'd': 'dia'}
your_translation_months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
your_translation_days_of_week = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

class MyTranslationCalendar(DetailedTelegramCalendar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.days_of_week['en'] = your_translation_days_of_week
        self.months['en'] = your_translation_months


# @dp.message_handler(commands='cal')
async def calend(message):
    from main import bot
    calendar, step = MyTranslationCalendar(min_date=date.today() ,max_date = max_date).build()
    await bot.send_message(message.chat.id,
                           f"Data do evento: \nSelecione o {LSTEP[step]}",
                           reply_markup=calendar)


# @dp.callback_query_handler(DetailedTelegramCalendar.func())
async def inline_kb_answer_callback_handler(query):
    from main import bot
    result, key, step = DetailedTelegramCalendar(min_date=date.today() ,max_date = max_date).process(query.data)

    if not result and key:
        await bot.edit_message_text(f"Selecione o {LSTEP[step]}",
                                    query.message.chat.id,
                                    query.message.message_id,
                                    reply_markup=key)
    elif result:
        await bot.edit_message_text(f"Data final: {result}",
                                    query.message.chat.id,
                                    query.message.message_id)

def register_handlers_eventos(dp: Dispatcher):
    from env import admins_id
    dp.register_message_handler(calend, commands=['evento', 'eventos'], state="*")
    dp.register_callback_query_handler(inline_kb_answer_callback_handler, state="*")
    # dp.register_message_handler(add_event, IDFilter(user_id=admin_id), commands=['add'], state="*")
    # dp.register_message_handler(edit_event, IDFilter(user_id=admin_id), commands=['add'], state="*")
    # dp.register_message_handler(remove_event, IDFilter(user_id=admin_id), commands=['add'], state="*")
    