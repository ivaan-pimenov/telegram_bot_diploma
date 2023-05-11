import logging
from sqlalchemy.orm import Session
from telebot import TeleBot
from telebot.apihelper import ApiException
from telebot.types import Message
from database.get_photo_from_db import get_photo_db
from database.models import Hotels
from utils.misc.hotel_message import get_hotel_message
from utils.misc.media_group import form_media_group


def result_message(hotels: list[Hotels], data: dict, message: Message, bot: TeleBot, session: Session) -> None:
	"""
	Form final message with mediagroup and send it to chat
	:param hotels: list[Hotels]
	:param data: dict
	:param message: Message
	:param bot: TeleBot
	:param session: Session
	:return: None
	"""
	logger = logging.getLogger(__name__)
	for hotel in hotels:
		bot.send_message(chat_id=message.chat.id, text=get_hotel_message(hotel=hotel, period=data['period']),
						 disable_web_page_preview=True)
		if data['quantity_photo']:
			photo_h = get_photo_db(session=session, hotel_id=hotel.hotel_id, limit=data["quantity_photo"])
			if photo_h:
				media = form_media_group(photos=photo_h)
				if len(media):
					try:
						bot.send_media_group(chat_id=message.chat.id, media=media)
					except ApiException as exc:
						logger.error(exc, exc_info=exc)
						media = form_media_group(photos=photo_h, error=True)
						if len(media):
							bot.send_media_group(chat_id=message.chat.id, media=media)
						else:
							bot.send_message(chat_id=message.chat.id, text='Фотографии не найдены')
			else:
				bot.send_message(chat_id=message.chat.id, text='Фотографии не найдены')
				