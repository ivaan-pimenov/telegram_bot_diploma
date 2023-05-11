from sqlalchemy.orm import Session
from database.models import History, Hotels


def set_hotels(hotels: list[dict], record_history: History, session: Session) -> list[Hotels]:
	"""
	Write hotels to db
	:param hotels: list[dict]
	:param record_history: History
	:param session: Session
	:return: list[Hotels]
	"""
	
	written_hotels = []
	for hotel in hotels:
		record_hot = Hotels()
		record_hot.history_id = record_history.id
		record_hot.hotel_id = hotel['hotel_id']
		record_hot.center = hotel['center']
		record_hot.coordinates = hotel['coordinates']
		record_hot.adress = hotel['adress']
		record_hot.name = hotel['name']
		record_hot.price = hotel['price']
		record_hot.star_rates = hotel['star_rating']
		record_hot.user_rates = hotel['user_rating']
		session.add(record_hot)
		written_hotels.append(record_hot)
	return written_hotels
