from telebot import TeleBot, types
from telebot.custom_filters import TextFilter
from config_data.config import Config
from states.states import HotelsStates


def load_photo(call: types.CallbackQuery, bot: TeleBot, config: Config) -> None:
	"""
	Callback if user choose to load photo
	:param call: CallbackQuery
	:param bot: TeleBot
	:param config: Config
	:return: None
	"""
	bot.set_state(user_id=call.from_user.id, state=HotelsStates.quantity_photo, chat_id=call.message.chat.id)
	bot.edit_message_text(message_id=call.message.id,
						  chat_id=call.message.chat.id,
						  text=f"Введите кол-во фотографий будем загружать для каждого отеля "
							   f"(максимум {config.rapid_api.max_photo}):",
						  reply_markup=None)


def register_load_photo_callback(bot: TeleBot) -> None:
	bot.register_callback_query_handler(load_photo,
										func=None,
										pass_bot=True,
										state=HotelsStates.photo,
										text=TextFilter(equals='yes'))
