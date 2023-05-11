import json
import logging
from site_API.request import get_request
from site_API.serialize import parse_result
from config_data.config import Config


def request_hotels(data: dict, config: Config) -> list[dict]:
	"""
	Get a list of hotels from api and return it
	:param data: dict
	:param config: Config
	:return: list
	"""
	logger = logging.getLogger(__name__)
	url = "https://hotels4.p.rapidapi.com/properties/list"
	check_in = data['check_in']
	check_out = data['check_out']
	sort_order = ''
	landmark_ids = ''
	price_min = ''
	price_max = ''
	page_size = data['quantity_display']
	if data['command'] == '/lowprice':
		sort_order = 'PRICE'
	elif data['command'] == '/highprice':
		sort_order = 'PRICE_HIGHEST_FIRST'
	elif data['command'] == '/bestdeal':
		sort_order = 'DISTANCE_FROM_LANDMARK'
		landmark_ids = 'Центр города'
		price_min = data['price_min']
		price_max = data['price_max']
		
	querystring = {"destinationId": data['destinationId'], "pageNumber": "1", "pageSize": page_size,
				   "checkIn": check_in, "checkOut": check_out, "adults1": "1", "priceMin": price_min,
				   "priceMax": price_max, "sortOrder": sort_order, "locale": "ru_RU", "currency": "RUB",
				   "landmarkIds": landmark_ids}
	try:
		request = get_request(url=url, params=querystring, config=config)
		if not request:
			return []
		data_request = json.loads(request.text)
		parsed = parse_result(parse_list=data_request['data']['body']['searchResults']['results'], data=data)
		return parsed
	except (LookupError, json.JSONDecodeError, TypeError) as exc:
		logger.error(exc, exc_info=exc)
		