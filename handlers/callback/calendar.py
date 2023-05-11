import datetime
from sqlalchemy.orm import Session
from telebot import TeleBot, types
from config_data.config import Config
from states.states import HotelsStates
from utils.misc.calendar import DetailedTelegramCalendar, LSTEP
from utils.main_functions.finish import final


def calendar(call: types.CallbackQuery, bot: TeleBot, config: Config, session: Session) -> None:
	"""
	Callback for calendar
	:param call: telebot.types.CallbackQuery
	:param bot: TeleBot
	:param config: Config
	:param session: Session
	:return: None
	"""
	result, key, step = DetailedTelegramCalendar(locale='ru', min_date=datetime.date.today()).process(call.data)
	if call.data == "cbcal_0_n":
		bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
		final(bot=bot, message=call.message, config=config, session=session)
	if not result and key:
		bot.edit_message_text(text=f"Выберите {LSTEP[step]}",
							  chat_id=call.message.chat.id,
							  message_id=call.message.message_id,
							  reply_markup=key)
	elif result:
		bot.edit_message_text(text=f"Вы выбрали {result.strftime('%d.%m.%Y')}",
							  chat_id=call.message.chat.id,
							  message_id=call.message.message_id)
		bot.set_state(user_id=call.from_user.id, state=HotelsStates.check_out, chat_id=call.message.chat.id)
		with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data:
			data['check_in'] = result.strftime('%Y-%m-%d')
		bot.send_message(chat_id=call.message.chat.id, text="Введите количество дней для бронирования (максимум 60):")
		

def register_calendar_callback(bot: TeleBot) -> None:
	bot.register_callback_query_handler(calendar,
										func=DetailedTelegramCalendar.func(),
										pass_bot=True,
										state=HotelsStates.check_in)
	