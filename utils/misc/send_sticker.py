import logging
from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from telebot.types import Message


def send_stickers(bot: TeleBot, chat_id: int, sticker: str) -> Message:
	"""
	Function for sending stickers to chat
	:param bot: TeleBot
	:param chat_id: int
	:param sticker: str
	:return: Message
	"""
	logger = logging.getLogger(__name__)
	stickers = {
		'hello': 'CAACAgIAAxkBAAEI3dBkVRccP9AjVrCRDBv48_3UmuXBFAACbwAD29t-AAGZW1Coe5OAdC8E',
		'load_city': 'CAACAgIAAxkBAAEI3dVkVRc_WosWSdCnBYkYGqUux6lq7wACYAAD29t-AAGGKUzOUOHn4S8E',
		'load_hotels': 'CAACAgIAAxkBAAEI3dlkVRdWvRhonPg5TdSvl3kUNzrftQACbQAD29t-AAF1HuyF8vtEpS8E',
	}
	try:
		load = bot.send_sticker(chat_id=chat_id, protect_content=True, sticker=stickers[sticker])
	except ApiTelegramException as exc:
		logger.exception(exc)
		load = bot.send_message(chat_id=chat_id, text='Ищем...')
	return load
