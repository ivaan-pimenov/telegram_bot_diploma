from telebot import types, TeleBot
from bot.states.states import HotelsStates


def get_min_price_wrong(message: types.Message, bot: TeleBot) -> None:
	"""
	Handler works with wrong min price messages from user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	bot.send_message(chat_id=message.chat.id, text="Некорректный ввод, введите минимальную цену (руб/сут)")
	return


def register_get_min_price_wrong(bot: TeleBot) -> None:
	bot.register_message_handler(get_min_price_wrong,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.price_min,
								 is_digit=False)
