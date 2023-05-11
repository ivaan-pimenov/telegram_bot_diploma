from telebot import TeleBot
from telebot.types import Message
from config_data.config import Config
from states.states import HotelsStates


def get_quantity_photo_wrong(message: Message, bot: TeleBot, config: Config) -> None:
	"""
	Handler works with wrong quantity photo messages from user
	:param message: Message
	:param bot: TeleBot
	:param config: Config
	:return: None
	"""
	bot.send_message(chat_id=message.chat.id,
					 text=f"Некорректный ввод, введите кол-во фотографий ({config.rapid_api.max_photo}):")
	return


def register_get_quantity_photo_wrong(bot: TeleBot) -> None:
	bot.register_message_handler(get_quantity_photo_wrong,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.quantity_photo)
