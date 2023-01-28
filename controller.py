from calculator import calculate as calc
from parser_calc import exp_to_list as pars
from bot_config import dp,bot
from aiogram import types

global exp_string
global value_type

@dp.message_handler(commands=['start'])
async def start_bot(message:types.message):
	await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
														f', привет! \n Всё, что я могу - предложить тебе - посчитать ответ на арифметическое выражение, даже с комплексными числами! \n Жми /game, если интересно!')

@dp.message_handler(commands=['game'])
async def game_start(message:types.message):
	global exp_string
	global value_type
	exp_string = ''
	value_type = ''
	await bot.send_message(message.from_user.id, text=f'Для начала нужно ввести тип чисел, которые будут в выражении. \n Введи "Тип=1" - если будешь вводить комплексные числа \n Введи "Тип=2" - если будешь вводить вещественные числа')

@dp.message_handler()
async def action(message:types.Message):
	global exp_string
	global value_type
	if '=' in message.text:
		if message.text.split('=')[0].lower()=='тип':
			if	message.text.split('=')[-1]=='1':
				value_type = '1'
				value_type_str='комплексные'
			elif	message.text.split('=')[-1]=='2':
				value_type = '2'
				value_type_str='вещественные'
			else:
				await bot.send_message(message.from_user.id, text= f'Неизвестный тип чисел, выбери: 1 или 2\n ')
				return
			await bot.send_message(message.from_user.id, text=
														f'Ты выбрал тип чисел: {value_type_str}\n '
														f'Теперь введи выражение x=[твоё выражение с вещественными или комплексными числами] \n'
														f'Например: х=3+4*(3/2)*10+3*5')         

		elif message.text.split('=')[0].lower()=='х' or message.text.split('=')[0].lower()=='х':
			if value_type=='1' or value_type=='2':
				exp_string=message.text.split('=')[1]	
				expression=pars(exp_string)
				result=calc(expression,value_type)
				await bot.send_message(message.from_user.id, text=f'х={result[0]} \n')
				exp_str=''
				value_type=''
			else:
				await bot.send_message(message.from_user.id, text=
																	f'Ты ещё не выбрал тип чисел: введи "Тип=Х",где Х - "1" или "2". \n'
																	f'1 - комплексные '
																	f'2 - вещественные ')
			
	else:
		await bot.send_message(message.from_user.id, text=
																	f'Я знаю только команды:. \n'
																	f'/start \n '
																	f'/game \n'
																	f'Тип=Х \n'
																	f'х=[Выражение]')