from telebot import types, TeleBot
from states.states import HotelsStates


def get_min_price(message: types.Message, bot: TeleBot) -> None:
	"""
	Handler gets min price from user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	text = int(message.text)
	if text == 0:
		text = 1
	with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
		data['price_min'] = text
	bot.send_message(chat_id=message.chat.id, text="Введите максимальную цену (руб/сут):")
	bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=HotelsStates.distance)


def register_get_min_price(bot: TeleBot) -> None:
	bot.register_message_handler(get_min_price,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.price_min,
								 is_digit=True)
