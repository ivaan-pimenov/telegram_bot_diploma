from telebot.types import InputMediaPhoto
from utils.request.check_photo_in_group import check_photo


def form_media_group(photos: list, error:bool = False) -> list[InputMediaPhoto]:
	"""
	Form media group and check photo if send group failed
	:param photos: list
	:param error: bool
	:return: list[InputMediaPhoto]
	"""
	media = []
	for photo in photos:
		if error and check_photo(photo=photo.photo):
			continue
		media.append(InputMediaPhoto(media=photo.photo))
	return media
