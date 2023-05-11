from telebot import types, TeleBot
from bot.states.states import HotelsStates


def get_max_price_wrong(message: types.Message, bot: TeleBot) -> None:
	"""
	Handler works with wrong max price messages from user
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	bot.send_message(chat_id=message.chat.id, text="Некорректный ввод, введите максимальную цену (руб/сут)")
	return


def register_get_max_price_wrong(bot: TeleBot) -> None:
	bot.register_message_handler(get_max_price_wrong,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.price_max,
								 price_max=False)
	