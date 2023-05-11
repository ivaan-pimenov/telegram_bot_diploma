from telebot import TeleBot
from telebot.types import Message
from site_API.request_cities import request_city
from config_data.config import Config
from keyboards.inline.cities_kb import cities_keyboard
from states.states import HotelsStates
from utils.main_functions.reset_all import reset
from utils.misc.send_sticker import send_stickers


def city(message: Message, bot: TeleBot, config: Config) -> None:
	"""
	Handler send a request to api to get list of cities and  send Inline keybiard with founded cities
	:param message: Message
	:param bot: TeleBot
	:param config: Config
	:return: None
	"""
	load = send_stickers(bot=bot, chat_id=message.chat.id, sticker='load_city')
	cities = request_city(city=message.text, config=config)
	if cities:
		bot.set_state(user_id=message.from_user.id, state=HotelsStates.enter_city, chat_id=message.chat.id)
		with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
			data['cities'] = cities
		bot.delete_message(message_id=load.id, chat_id=message.chat.id)
		bot.send_message(chat_id=load.chat.id,
						 text='Вот что удалось найти:',
						 reply_markup=cities_keyboard(cities))
	else:
		bot.edit_message_text(message_id=load.id, chat_id=load.chat.id, text="Ничего не нашлось!")
		reset(bot=bot, message=message)
		
		
def register_city(bot: TeleBot) -> None:
	bot.register_message_handler(city,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.start)
	