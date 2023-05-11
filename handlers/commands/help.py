from telebot import TeleBot, types
from utils.main_functions.help_func import help_message


def helps(message: types.Message, bot: TeleBot) -> None:
	"""
	For help command
	:param message: Message
	:param bot: TeleBot
	:return: None
	"""
	help_message(message=message, bot=bot)
	
	
def register_helps(bot: TeleBot) -> None:
	bot.register_message_handler(helps,
								 pass_bot=True,
								 is_private=True,
								 content_types=['text'],
								 commands=["help"],
								 states=None)
	