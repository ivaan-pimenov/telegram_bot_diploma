import datetime
from telebot import types, TeleBot
from keyboards.inline.photo_kb import get_photo_kb
from states.states import HotelsStates


def get_check_out(message: types.Message, bot: TeleBot) -> None:
	"""
	Get date of departure from the hotel from the user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
		check_out = datetime.datetime.strptime(data['check_in'], '%Y-%m-%d') + datetime.timedelta(days=int(message.text))
		data['check_out'] = check_out.strftime('%Y-%m-%d')
		data['period'] = int(message.text)
		command = data['command']
	if command == '/bestdeal':
		bot.send_message(chat_id=message.chat.id, text="Введите минимальную цену (руб/сут)")
		bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=HotelsStates.price_min)
	else:
		bot.send_message(chat_id=message.chat.id, text="Будем загружать фотографии?", reply_markup=get_photo_kb())
		bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=HotelsStates.photo)
		
		
def register_check_out(bot: TeleBot) -> None:
	bot.register_message_handler(get_check_out,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.check_out,
								 in_range=60)
		