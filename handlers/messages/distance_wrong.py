from telebot import types, TeleBot
from states.states import HotelsStates


def get_distance_wrong(message: types.Message, bot: TeleBot) -> None:
	"""
	Handler works with wrong distance messages from user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	bot.send_message(chat_id=message.chat.id, text="Некорректный ввод, введите максимальное расстояние от центра (км):")
	return


def register_distance_wrong(bot: TeleBot) -> None:
	bot.register_message_handler(get_distance_wrong,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.distance,
								 is_digit=False)
	