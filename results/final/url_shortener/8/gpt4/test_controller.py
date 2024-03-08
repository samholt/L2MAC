from controller import URLController
from datetime import datetime, timedelta


def test_controller():
	controller = URLController()
	short_url = controller.create_url('https://www.google.com')
	assert len(short_url) == 5
	original_url = controller.get_original_url(short_url)
	assert original_url == 'https://www.google.com'
	controller.delete_expired_urls()
	assert controller.get_original_url(short_url) is None

