import logging
from handlers.common import register_handlers_common
from handlers.ajuda.ajuda import register_handlers_ajuda
from handlers.grupos.grupos import register_handlers_grupos
from handlers.ouvidoria.ouvidoria import register_handlers_ouvidoria
from handlers.fluxos.fluxos import register_handlers_fluxos
from handlers.estagio.estagio import register_handlers_estagio

from config import API_TOKEN

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import fluxos

buttonSW = InlineKeyboardButton(text='Software 2017', callback_data='fluxo_software2017') #2017
buttonAE = InlineKeyboardButton(text='Aeroespacial 2018' , callback_data='fluxo_aeroespacial2018') #2018
buttonEN = InlineKeyboardButton(text='Energia 2018' , callback_data='fluxo_energia2018') #2018
buttonAT = InlineKeyboardButton(text='Automotiva 2018' , callback_data='fluxo_automotiva2018') #2018
buttonET = InlineKeyboardButton(text='Eletrônica 2019' , callback_data='fluxo_eletronica2019') #2019
buttonET_2021 = InlineKeyboardButton(text='Eletrônica 2021' , callback_data='fluxo_eletronica_2021') #2021

keybFluxos = InlineKeyboardMarkup().add(buttonSW).add(buttonAE).add(buttonAT).add(buttonET,buttonET_2021).add(buttonEN)


buttonCalendMatricula = InlineKeyboardButton(text='Calendario de Matricula', callback_data='calendario_matricula2022')
buttonCalendAtividade = InlineKeyboardButton(text='Calendario de Atividades', callback_data='calendario_atividades2022')
keybCalends = InlineKeyboardMarkup().add(buttonCalendMatricula, buttonCalendAtividade)

# API_TOKEN = "***REMOVED***"

# Configure logging
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


# Comando de menu de ajuda inicial | comandos: 'ajuda', 'menu', 'help', 'start'
register_handlers_ajuda(dp)

# Comando de menu de grupos | comandos: 'grupos', 'grupo'
register_handlers_grupos(dp)

# Comando de menu dos fluxos | comandos: 'fluxos', 'fluxo'
register_handlers_fluxos(dp)

# comando de ajuda estagio | comandos: 'estagio', 'estágios'
register_handlers_estagio(dp)

@dp.message_handler(commands=['estagio', 'estagios'])
async def estagio(message: types.Message):
    textoEstagio = """
    *ESTÁGIOS:*

Diretrizes de estágios importantes:
- [Lei 11.788 de 25 de setembro de 2008](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm)
- [Regulamento geral de estágios de graduação da Universidade de Brasília](https://john.pro.br/estagios/docs/Resolucao_Estagios_UnB.pdf)
- [Regulamento de estágios da FGA](https://john.pro.br/estagios/docs/Resolucao_Estagios_FGA.pdf)

Cordenadores de estágio:
*Engenharia Aeroespacial:* Prof. Artem Andrianov (andrianov@unb.br)

*Engenharia Automotiva:* Prof.ª Rita de Cássia Silva (ritasilva@unb.br)

*Engenharia de Energia:* Prof.ª Maria Del Pilar Hidalgo Falla (pilar@unb.br)

*Engenharia de Software:* Prof. John L. C. Gardenghi (john.gardenghi@unb.br)

*Engenharia Eletrônica:* Prof. Guillermo Alvarez Bestard (guillermo@unb.br)

*Estagio Supervisionado:*
A matrícula não é feita junto com a matrícula das demais disciplinas. A solicitação de matrícula é feita por inscrição pelo Microsoft Forms, geralmente depois do início das aulas do semestre em questão.

Requisitos para cursar estágio supervisionado:
- Ter concluído 70% da carga horária total do curso
- Apresentar 210h de atividades técnicas supervisionadas até a conclusão da disciplina
- Não exceder o limite de 32 créditos no total em disciplinas matriculadas (a não ser que seja um provável formando)

*Estágio não obrigatório*
Para iniciar um estagio não supervisionado:
- É necessario realizar o pré-cadastro no SIGAA conforme o [Vídeo](https://web.microsoftstream.com/video/3db310fa-ea33-4fff-84f7-f6886c70cf74)
- Enviar os documentos de assinatura para o coodenador de estágio do seu respectivo curso

Mais informações relevantes neste [Link](https://john.pro.br/estagios/)

   """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEstagio, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@dp.message_handler(commands=['secretaria', 'sec'])
async def email(message: types.Message):
    textoEmailSec = """
    *CONTATOS SECRETARIA:*

Email da Secretaria
unbgama@unb.br

Email da coordenação FGA
coordenacaofga@unb.br

    """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEmailSec, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@dp.message_handler(commands=['coord', 'coordenadores'])
async def email(message: types.Message):
    textoEmailCoord = """
    *CONTATOS COORDENADORES:*

Coordenadores do curso:
Software:
Ricardo Chaim: ricardoc@unb.br

Aeroespacial:
Thiago Felippe K. Cordeiro: thiagocordeiro@unb.br

Automotiva:
Fábio Cordeiro de Lisboa: fabiolisboa@unb.br

Eletrônica:
Marcelino Andrade: andrade@unb.br

Energia:
Luciano Gonçalves Noleto: lucianonoleto@unb.br; 

    """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEmailCoord, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['calendario', 'calend'])
async def calendario(message: types.Message):
    textoCalend = """
    *CALENDARIOS IMPORTANTES:*
    """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCalend, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybCalends)

@dp.message_handler(commands=['creditos', 'credito'])
async def creditos(message: types.Message):
    textoCredito = """
    *APROVEITAMENTO DE CREDITOS:*

É possivel aproveitar na graduação de engenharias na FGA um total de 8 creditos com atividades complementares, podendo ser cursos online, projeto de pesquisa/extenxão, EJs, estagio não obrigatorio, etc.

Para isso é necessario preencher este [formulário](https://john.pro.br/estagios/formulario_atividades_complementares.pdf) e enviar para xborges@unb.br com os devidos documentos necessarios comprobatórios.
    """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCredito, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['atletica', 'atleticas'])
async def atletica(message: types.Message):
    textoAtletica = """
    *ATLETICAS:*

Atlética Pesadelo:
[Instagram](https://www.instagram.com/atleticapesadelo/?hl=en)

Obs: Caso seje de algumas dessa(s) atletica(s) (ou outras da FGA) mande para @heitormsb uma pequena descrição/introdução da sua atletica e forma de contato, para colocar aqui. Obrigado.
   """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoAtletica, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['ej', 'ejs'])
async def ej(message: types.Message):
    textoEJ = """
    *EMPRESAS JUNIORES:*
- As Empresas juniores tem o propósito de formar líderes comprometidos e capazes para o mercado
- Todas as EJs aceitam os 5 cursos da FGA

*Orc'estra Gamificação*
Empresa Júnior de Engenharia de Software. Tem o propósito em trazer soluções de software e gamificação para o mercado. 
Saiba mais em: [@orcgamificacao](https://www.instagram.com/orcgamificacao/) no instagram.

*Zenit Aerospace*

*Matriz Engenharia De Energia*

*Engrena*

*Eletronjun*

Obs: Caso seje de algumas dessas EJs (ou outras da FGA) mande para @heitormsb uma pequena descrição/introdução da sua EJ e forma de contato, para colocar aqui. Obrigado.
   """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoEJ, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['competicao', 'compet'])
async def competicao(message: types.Message):
    textoCompeticao = """
    *EQUIPES DE COMPETIÇÃO:*

*EDRA*
Somos uma equipe de competição da FGA dedicada a desenvolver aeronaves autônomas de voo vertical (drones). Integramos conhecimentos de todas as áreas da engenharia em nossos projetos, por isso estamos sempre em busca de novos talentos para nos ajudar a crescer. 
Saiba mais em: [@edraunb](https://www.instagram.com/edraunb/) no instagram.

*Capital Rocket Team*
A Capital Rocket Team(CRT) é uma equipe de foguetes da categoria high power rocketry do curso de engenharia aeroespacial da UnB, campus do gama, foi fundado no ano de 2015, e é composta por membros de diversos cursos da universidade de Brasília. A equipe é conhecida nacional e internacionalmente por trabalhar como propulsão híbrida, sendo pioneira nesse tipo de propulsão no meio das equipes de competição no Brasil, e tendo se consagrado como a primeira a lançar um foguete movido a propulsão híbrida em uma competição na América Latina, na Latin America Space Challenge 2022.
Saiba mais em: [@capitalrocketteam](https://www.instagram.com/capitalrocketteam/) no instagram ou pelo [Site](www.capitalrocketteam.com).

UnBaja

Team Titans

FGR


Obs: Caso seje de algumas dessas equipes (ou outras da FGA) mande para @heitormsb uma pequena descrição/introdução da sua equipe e forma de contato, para colocar aqui. Obrigado.
   """

    if(message.chat.type != 'private'):
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, textoCompeticao, parse_mode=ParseMode.MARKDOWN)


register_handlers_common(dp)
register_handlers_ouvidoria(dp)

# Apagar comandos invalidos do chat
@dp.message_handler()
async def invalidCommand(message: types.Message):
    if message.text[0] == '/' and not " " in message.text:
        await bot.delete_message(message.chat.id, message.message_id)

@dp.callback_query_handler(text=['calendario_atividades2022', 'calendario_matricula2022'])
async def fluxos(call: types.CallbackQuery):
    if call.data == "calendario_atividades2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Atividades/2022_2/2022_2_Calend_Atv_Grad_28_09_22.pdf')
    if call.data == "calendario_matricula2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Matricula/2022_2/2022_2_Calend_Matricula_Grad.pdf')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)