import logging

from handlers.ajuda.ajuda import register_handlers_ajuda
from handlers.grupos.grupos import register_handlers_grupos
from handlers.fluxos.fluxos import register_handlers_fluxos
from handlers.estagio.estagio import register_handlers_estagio
from handlers.ouvidoria.ouvidoria import register_handlers_ouvidoria
from handlers.secretaria.secretaria import register_handlers_secretaria
from handlers.coordenadores.coordenadores import register_handlers_coordenadores
from handlers.calendario.calendario import register_handlers_calendario
from handlers.creditos.creditos import register_handlers_creditos
from handlers.atletica.atletica import register_handlers_atletica
from handlers.ej.ej import register_handlers_ej
from handlers.competicao.competicao import register_handlers_competicao

from handlers.eventos.eventos import register_handlers_eventos

from env import API_TOKEN

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage



# Configure logging
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
    
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("ajuda", "Mostra os comandos disponíveis"),
        BotCommand("grupos", "Link grupos Engenharias"),
        BotCommand("fluxos", "Fluxogramas das Engenharias"),
        BotCommand("estagio", "Estágio"),
        BotCommand("secretaria", "Contatos da secretaria"),
        BotCommand("coordenadores", "Coordenadores das Engenharias"),
        BotCommand("calendario", "Calendário acadêmico"),
        BotCommand("creditos", "Aproveitamento de créditos por atividade complementar"),
        BotCommand("atleticas", "Atleticas"),
        BotCommand("ej", "Empresas juniores"),
        BotCommand("competicao", "Equipes de competição"),
    ])

# Comando de menu de ajuda inicial | comandos: 'ajuda', 'menu', 'help', 'start'
register_handlers_ajuda(dp)

# Comando de menu de grupos | comandos: 'grupos', 'grupo'
register_handlers_grupos(dp)

# Comando de menu dos fluxos | comandos: 'fluxos', 'fluxo'
register_handlers_fluxos(dp)

# Comando de estagios | comandos: 'estagio', 'estágios'
register_handlers_estagio(dp)

# Comando contato da secretaria | comandos: 'secretaria', 'sec'
register_handlers_secretaria(dp)

# Comando contato de coordenadores | comandos: 'coordenadores', 'coord'
register_handlers_coordenadores(dp)

# Comando calendarios | comandos: 'calendario', 'calend'
register_handlers_calendario(dp)

# Comando creditos | comandos: 'creditos', 'credito'
register_handlers_creditos(dp)

# Comando atletica | comandos: 'atletica', 'atleticas'
register_handlers_atletica(dp)

# Comando EJs | comandos: 'ej', 'ejs'
register_handlers_ej(dp)

# Comando competições | comandos: 'competicao', 'compet'
register_handlers_competicao(dp)

# Comando ouvidoria | comandos: 'ouvidoria'
register_handlers_ouvidoria(dp)

# Comando eventos | comandos: 'eventos', 'evento'
register_handlers_eventos(dp) 

# Apagar comandos invalidos do chat
@dp.message_handler()
async def invalidCommand(message: types.Message):
    if message.text[0] == '/' and not " " in message.text:
        await bot.delete_message(message.chat.id, message.message_id)  


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)