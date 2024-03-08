from model import URL
from datetime import datetime, timedelta


def test_url():
	url = URL('https://www.google.com', 'abcde', datetime.now(), datetime.now() + timedelta(days=30), 0)
	assert url.original_url == 'https://www.google.com'
	assert url.short_url == 'abcde'
	assert url.click_count == 0

