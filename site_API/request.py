import requests
from config_data.config import Config
import logging


def get_request(url: str, params: dict, config: Config) -> requests.Response:
	"""
	Common function for making request to api. Returns response.
	:param url: str
	:param params: dict
	:param config: Config
	:return: requests.Response
	"""
	logger = logging.getLogger(__name__)
	headers = {
		"X-RapidAPI-Key": config.rapid_api.rapid_api_key,
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
	}
	
	try:
		return requests.get(url=url, headers=headers, params=params, timeout=20)
	except requests.exceptions.RequestException as exc:
		logger.error(exc, exc_info=exc)
		