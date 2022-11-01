import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

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

API_TOKEN = "***REMOVED***"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['ajuda', 'menu', 'help', 'start'])
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

Continue conversando pelo privado @FGA\_UnBot.
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

    await bot.send_message(message.from_user.id, textoGrupos, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['fluxos', 'fluxo'])
async def fluxos(message: types.Message):
    textoFluxo = """
    *FLUXO DOS CURSOS:*
    """

    await bot.send_message(message.from_user.id, textoFluxo, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybFluxos)

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

    await bot.send_message(message.from_user.id, textoEstagio, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

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

    await bot.send_message(message.from_user.id, textoEmail, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@dp.message_handler(commands=['calendario', 'calend'])
async def calendario(message: types.Message):
    textoCalend = """
    *CALENDARIOS IMPORTANTES:*
    """
    await bot.send_message(message.from_user.id, textoCalend, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=keybCalends)

@dp.message_handler(commands=['creditos', 'credito'])
async def creditos(message: types.Message):
    textoCredito = """
    *APROVEITAMENTO DE CREDITOS:*

É possivel aproveitar na graduação de engenharias na FGA um total de 8 creditos com atividades complementares, podendo ser cursos online, projeto de pesquisa/extenxão, EJs, estagio não obrigatorio, etc.

Para isso é necessario preencher este [formulário](https://john.pro.br/estagios/formulario_atividades_complementares.pdf) e enviar para xborges@unb.br com os devidos documentos necessarios comprobatórios.
    """

    await bot.send_message(message.from_user.id, textoCredito, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['atletica', 'atleticas'])
async def atletica(message: types.Message):
    textoAtletica = """
    *ATLETICAS:*

Atlética Pesadelo:
[Instagram](https://www.instagram.com/atleticapesadelo/?hl=en)

Obs: Caso seje de algumas dessa(s) atletica(s) (ou outras da FGA) mande para @heitormsb uma pequena descrição/introdução da sua atletica e forma de contato, para colocar aqui. Obrigado.
   """

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

    await bot.send_message(message.from_user.id, textoEJ, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['competicao', 'compet'])
async def competicao(message: types.Message):
    textoCompeticao = """
    *EQUIPES DE COMPETIÇÃO:*

*EDRA*
Somos uma equipe de competição da FGA dedicada a desenvolver aeronaves autônomas de voo vertical (drones). Integramos conhecimentos de todas as áreas da engenharia em nossos projetos, por isso estamos sempre em busca de novos talentos para nos ajudar a crescer. 
Saiba mais em: [@edraunb](https://www.instagram.com/edraunb/) no instagram.

UnBaja

Team Titans

FGR

Capital Rocket Team

Obs: Caso seje de algumas dessas equipes (ou outras da FGA) mande para @heitormsb uma pequena descrição/introdução da sua equipe e forma de contato, para colocar aqui. Obrigado.
   """

    await bot.send_message(message.from_user.id, textoCompeticao, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(text=['fluxo_software2017', 'fluxo_aeroespacial2018', 'fluxo_energia2018', 'fluxo_automotiva2018', 'fluxo_eletronica2019', 'fluxo_eletronica_2021'])
async def fluxos(call: types.CallbackQuery):
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

@dp.callback_query_handler(text=['calendario_atividades2022', 'calendario_matricula2022'])
async def fluxos(call: types.CallbackQuery):
    if call.data == "calendario_atividades2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Atividades/2022_2/2022_2_Calend_Atv_Grad_28_09_22.pdf')
    if call.data == "calendario_matricula2022":
      await bot.send_document(call.message.chat.id, 'https://saa.unb.br/images/documentos/graduacao/Calendarios/Matricula/2022_2/2022_2_Calend_Matricula_Grad.pdf')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)