from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Photo


def get_photo_db(hotel_id: int, session: Session, limit: int) -> list[Photo]:
	"""
	Get photo from db
	:param hotel_id: int
	:param session: Session
	:param limit: int
	:return: list[Photo]
	"""
	photo_request = session.execute(
		select(Photo).where(Photo.hotel_id == hotel_id).limit(limit)
	)
	return photo_request.scalars().all()
