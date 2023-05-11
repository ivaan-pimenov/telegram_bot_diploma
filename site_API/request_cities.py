import json
import logging

from site_API.request import get_request
from utils.request.clean_html import remove_span
from config_data.config import Config


def request_city(city: str, config: Config) -> dict[any, dict[str, any]]:
	"""
	Get info about cities from api
	:param city: str
	:param config: Config
	:return: dict
	"""
	logger = logging.getLogger(__name__)
	url = "https://hotels4.p.rapidapi.com/locations/v2/search"
	
	querystring = {"query": city, "locale": "ru_RU", "currency": "RUB"}
	response = {}
	try:
		request = get_request(url=url, config=config, params=querystring)
		if request.status_code != 200:
			raise LookupError(f"Status code {request.status_code}")
		if not request:
			return {}
		data = json.loads(request.text)
		if not data:
			raise LookupError('Response is empty')
		for entity in data["suggestions"][0]["entities"]:
			response[entity['destinationId']] = {
				'name': entity['name'],
				'caption': remove_span(entity['caption']),
				'latitude': entity['latitude'],
				'longitude': entity['longitude']
			}
		
		return response
	except (LookupError, TypeError) as exc:
		logger.error(exc, exc_info=exc)
		