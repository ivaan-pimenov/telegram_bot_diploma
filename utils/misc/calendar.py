from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

LSTEP = {'y': 'год', 'm': 'месяц', 'd': 'день'}


class MyStyleCalendar(DetailedTelegramCalendar):
	"""
	Just customize calendar
	"""
	prev_button = "⬅️"
	next_button = "➡️"
	empty_month_button = ""
	empty_year_button = ""
	