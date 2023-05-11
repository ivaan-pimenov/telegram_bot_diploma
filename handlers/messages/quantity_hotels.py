import datetime
from telebot import TeleBot
from telebot.types import Message
from states.states import HotelsStates
from utils.misc.calendar import DetailedTelegramCalendar, LSTEP


def quantity(message: Message, bot: TeleBot) -> None:
	"""
	Handler gets quantity of hotels from user
	:param message: Message
	:param bot: TeleBot
	:param config: Config
	:return: None
	"""
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['quantity_display'] = int(message.text)
	bot.send_message(chat_id=message.chat.id, text="Планируемая дата заезда:")
	calendar, step = DetailedTelegramCalendar(locale='ru', min_date=datetime.date.today()).build()
	bot.send_message(chat_id=message.chat.id, text=f"Выберите {LSTEP[step]}", reply_markup=calendar)
	
	
def register_quantity(bot: TeleBot) -> None:
	bot.register_message_handler(quantity,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.quantity,
								 in_range=5)
	