from sqlalchemy.orm import Session
from telebot import TeleBot, types
from config_data.config import Config
from states.states import HotelsStates
from utils.main_functions.finish import final


def get_quantity_photo(message: types.Message, bot: TeleBot, config: Config, session: Session) -> None:
	bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=HotelsStates.final)
	with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
		data['quantity_photo'] = int(message.text)
	final(bot=bot, message=message, config=config, session=session)
	
	
def register_get_quantity_photo(bot: TeleBot):
	bot.register_message_handler(get_quantity_photo,
								 pass_bot=True,
								 content_types=['text'],
								 is_private=True,
								 state=HotelsStates.quantity_photo,
								 in_range=5)
	