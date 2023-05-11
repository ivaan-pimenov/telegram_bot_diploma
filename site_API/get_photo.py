import json
import logging
from site_API.request import get_request
from config_data.config import Config


def request_photo(id_hotel: str, config: Config) -> list[dict]:
	"""
	Make request to api for getting photo's urls
	:param id_hotel: str
	:param config: Config
	:return: list[dict]
	"""
	logger = logging.getLogger(__name__)
	url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
	querystring = {"id": id_hotel}
	photos = []
	try:
		response = get_request(url=url, params=querystring, config=config)
		if not response:
			return []
		data = json.loads(response.text)
		for photo in data['hotelImages']:
			photo_url = photo['baseUrl'].replace('_{size}', '_z')
			photos.append({'id_hotel': id_hotel, 'url': photo_url})
		return photos
	except (json.JSONDecodeError, TypeError) as exc:
		logger.error(exc, exc_info=exc)
		