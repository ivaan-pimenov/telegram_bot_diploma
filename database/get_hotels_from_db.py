from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import History, Hotels


def get_hotels_db(record_history: History, session: Session) -> list[Hotels]:
	"""
	Get hotels from db
	:param record_history: History
	:param session: Session
	:return: list[Hotels]
	"""
	hotels_request = session.execute(
		select(Hotels).where(Hotels.history_id == record_history.id)
	)
	return hotels_request.scalars().all()