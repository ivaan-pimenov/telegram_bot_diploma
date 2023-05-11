from sqlalchemy import select
from  sqlalchemy.orm import Session
from database.models import History


def get_history_db(user_id: int, session: Session) -> list[History]:
	"""
	Get history records from db
	:param user_id: int
	:param session: Session
	:return: list[History]
	"""
	history_request = session.execute(
		select(History).where(History.telegram_id == user_id)
	)
	
	return history_request.scalars().all()
