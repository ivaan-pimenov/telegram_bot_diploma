from sqlalchemy.orm import Session
from typing import Union
from site_API.get_hotels import request_hotels
from site_API.get_photo import request_photo
from config_data.config import Config
from utils.db.check_photo import photo_exist


def photo_and_hotels(data: dict, config: Config, session: Session) -> \
	Union[tuple[list[dict], list[dict]], tuple[None, None]]:
	"""
	Main function for getting hotels and photo from api
	:param data: dict
	:param config: Config
	:param session: Session
	:return: tuple[list[dict], list[dict]]
	"""
	photos = []
	hotels = request_hotels(data=data, config=config)
	if hotels:
		for hotel in hotels:
			if not data['quantity_photo']:
				break
			if not photo_exist(hotel_id=hotel["hotel_id"], session=session):
				request_p = request_photo(id_hotel=hotel["hotel_id"], config=config)
				if request_p:
					photos.extend(request_p)
		return hotels, photos
	return None, None
