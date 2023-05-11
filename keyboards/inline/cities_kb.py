from telebot.callback_data import CallbackData
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


cities_factory = CallbackData('city_id', prefix='city')


def cities_keyboard(cities: dict) -> InlineKeyboardMarkup:
	"""
	Return InlineKeyboardMarkup for founded cities
	:param cities: dict
	:return: InlineKeyboardMarkup
	"""
	return InlineKeyboardMarkup(keyboard=[
		[InlineKeyboardButton(
			text=city['caption'],
		 	callback_data=cities_factory.new(city_id=destination_id)
		)] for destination_id, city in cities.items()
		]
	)
