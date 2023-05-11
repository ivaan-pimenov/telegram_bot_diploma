from telebot import types, TeleBot
from states.states import HotelsStates


def get_max_price(message: types.Message, bot: TeleBot) -> None:
	"""
	Handler gets max price from user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
		data['price_max'] = int(message.text)
	bot.send_message(chat_id=message.chat.id, text="Введите максимальное расстояние от центра (км)")
	bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=HotelsStates.distance)
	
	
def register_get_max_price(bot: TeleBot) -> None:
	bot.register_message_handler(get_max_price,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.price_max,
								 price_max=True)
	