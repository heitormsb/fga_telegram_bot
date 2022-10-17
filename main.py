import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

import fluxos

buttonSW = InlineKeyboardButton(text='Software', callback_data='fluxo_software')
buttonAE = InlineKeyboardButton(text='Aeroespacial' , callback_data='fluxo_aeroespacial')
buttonEN = InlineKeyboardButton(text='Energia' , callback_data='fluxo_energia')
buttonAT = InlineKeyboardButton(text='Automotiva' , callback_data='fluxo_automotiva')
buttonET = InlineKeyboardButton(text='Eletrônica' , callback_data='fluxo_eletronica')

keybFluxo = InlineKeyboardMarkup().add(buttonSW).add(buttonAE).add(buttonEN).add(buttonAT).add(buttonET)


buttonCalendMatricula = InlineKeyboardButton(text='Calendario de Matricula', callback_data='calendario_matricula')
buttonCalendAtividade = InlineKeyboardButton(text='Calendario de Atividades', callback_data='calendario_atividades')
keybCalend = InlineKeyboardMarkup().add(buttonCalendMatricula, buttonCalendAtividade)

API_TOKEN = ""

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['ajuda', 'menu', 'help'])
async def ajuda(message: types.Message):
    texto = """
    *Bot Engenharias FGA*

FGA\_UnBot
/ajuda , /help  Comandos do Bot
  
/grupos - Link grupos Engenharias
/fluxos - Fluxogramas das Engenharias

/estagio - Estágio
/emails - Emails importantes
/calendario - Calendário acadêmico
/creditos - Aproveitamento de créditos por atividade complementar

/atleticas - Atleticas
/ej - Empresas juniores
/competicao - Equipes de competição
    """

    await message.answer(texto, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['grupos', 'grupo'])
async def grupos(message: types.Message):
    textoGrupos = """
    *GRUPOS DOS CURSOS:*
*Eng de Software*
[https://t.me/+UnsasFZt5yRC_pvE]

*Eng de Energia*
[https://t.me/+Js1m7GFq1t4yZjk5]

*Eng Eletrônica*
[https://t.me/joinchat/NlbRCBOe7gbb0ziQI4JQOw]

*Eng Aeroespacial* 
[https://t.me/+M9WovwjctUNhM2Yx]

*Eng Automotiva*
[https://t.me/+obxLHSewaq43YTFh]

    """

    await message.answer(textoGrupos, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['fluxos', 'fluxo'])
async def fluxos(message: types.Message):
    textoFluxo = """
    *FLUXO DOS CURSOS:*
    """

    await message.answer(textoFluxo, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybFluxo)

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

    await message.answer(textoEstagio, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['emails', 'email'])
async def email(message: types.Message):
    textoEmail = """
    *EMAILS IMPORTANTES:*

Email da Secretaria
unbgama@unb.br

Email da coordenação FGA
coordenacaofga@unb.br

Coordenadores do curso:
Software:
Tiago Fonseca: fonsecafga@unb.br

Aeroespacial:
Thiago Felippe K. Cordeiro: thiagocordeiro@unb.br

Automotiva:
Fábio Cordeiro de Lisboa: fabiolisboa@unb.br

Eletrônica:
Fabiano Araujo Soares: fabianosoares@unb.br

Energia:
Luciano Gonçalves Noleto: lucianonoleto@unb.br; 

    """

    await message.reply(textoEmail, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['calendario', 'calend'])
async def calendario(message: types.Message):
    textoCalend = """
    *CALENDARIOS IMPORTANTES:*
    """
    await message.reply(textoCalend, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybCalend)

@dp.message_handler(commands=['creditos', 'credito'])
async def creditos(message: types.Message):
    textoCredito = """
    *APROVEITAMENTO DE CREDITOS:*

É possivel aproveitar na graduação de engenharias na FGA um total de 8 creditos com atividades complementares, podendo ser cursos online, projeto de pesquisa/extenxão, EJs, estagio não obrigatorio, etc.

Para isso é necessario preencher este [formulário](https://john.pro.br/estagios/formulario_atividades_complementares.pdf) e enviar para xborges@unb.br com os devidos documentos necessarios.
    """

    await message.answer(textoCredito, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['atletica', 'atleticas'])
async def atletica(message: types.Message):
    textoAtletica = """
Atlética Pesadelo:
[Instagram](https://www.instagram.com/atleticapesadelo/?hl=en)
   """

    await message.answer(textoAtletica, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['ej', 'ejs'])
async def ej(message: types.Message):
    textoEJ = """
    *EMPRESAS JUNIORES:*

Zenit Aerospace

Orc'estra Gamificação

Matriz Engenharia De Energia

Engrena

Eletronjun 

   """

    await message.answer(textoEJ, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['competicao', 'compet'])
async def competicao(message: types.Message):
    textoCompeticao = """
UnBaja

Capital Rocket Team
   """

    await message.answer(textoCompeticao, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(text=['fluxo_software', 'fluxo_aeroespacial', 'fluxo_energia', 'fluxo_automotiva', 'fluxo_eletronica'])
async def fluxos(call: types.CallbackQuery):
    if call.data == "fluxo_software":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_software.pdf')
    if call.data == "fluxo_aeroespacial":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_aeroespacial.pdf')
    if call.data == "fluxo_energia":
      await bot.send_document(call.message.chat.id, '')
    if call.data == "fluxo_automotiva":
      await bot.send_document(call.message.chat.id, 'https://raw.githubusercontent.com/heitormsb/fga_telegram_bot/7d114f93108324a8a84f4f55a94187a3d9c2a0ca/fluxos/fluxo_automativa.pdf')
    if call.data == "fluxo_eletronica":
      await bot.send_document(call.message.chat.id, '')


@dp.callback_query_handler(text=['calendario_atividades', 'calendario_matricula'])
async def fluxos(call: types.CallbackQuery):
    if call.data == "calendario_atividades":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Atividades/2022_2/2022_2_Calend_Atv_Grad_28_09_22.pdf')
    if call.data == "calendario_matricula":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Matricula/2022_2/2022_2_Calend_Matricula_Grad.pdf')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)