import logging
from sqlalchemy.orm import Session
from telebot import TeleBot
from telebot.types import Message
from site_API.get_photo_and_hotels import photo_and_hotels
from config_data.config import Config
from database.write_history import set_history
from database.write_hotels import set_hotels
from database.write_photo import set_photo
from utils.main_functions.final_message import result_message
from utils.main_functions.reset_all import reset
from utils.misc.send_sticker import send_stickers


def final(bot: TeleBot, message: Message, config: Config, session: Session) -> None:
	"""
	Make final work as write result in db and send final message to user
	:param bot: TeleBot
	:param message: Message
	:param config: Config
	:param session: Session
	:return: None
	"""
	logger = logging.getLogger(__name__)
	error = False
	written_hotels = []
	load = send_stickers(bot=bot, chat_id=message.chat.id, sticker='load_hotels')
	with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
		send_data = data
	hotels, photo = photo_and_hotels(data=send_data, config=config, session=session)
	if hotels is None:
		error = True
	if not error:
		record_history = set_history(data=data, error=error, session=session)
		if record_history:
			written_hotels = set_hotels(hotels=hotels, record_history=record_history, session=session)
			if len(photo):
				set_photo(photo=photo, session=session)
			session.commit()
	bot.delete_message(chat_id=message.chat.id, message_id=load.message_id)
	if error:
		bot.send_message(chat_id=message.chat.id, text='Что-то пошло не так')
		reset(bot=bot, message=message)
	if not len(hotels):
		bot.send_message(chat_id=message.chat.id, text='По вашему запросу ничего не найдено')
	else:
		result_message(hotels=written_hotels, data=data, message=message, bot=bot, session=session)
	reset(bot=bot, message=message)
	