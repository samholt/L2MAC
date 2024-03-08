from datetime import datetime
from url_shortener.models import User, URL, Click
from url_shortener.analytics import get_clicks


def test_get_clicks():
	# Create a User, URL, and Clicks
	user = User('test_user', 'password')
	url = URL('https://example.com', 'https://short.url', user, datetime.now(), datetime.now())
	clicks = [Click(url, datetime.now(), 'USA'), Click(url, datetime.now(), 'Canada')]

	# Add the Clicks to the database
	DB[url.shortened_url] = clicks

	# Retrieve the Clicks from the database
	retrieved_clicks = get_clicks(url)

	# Assert that the retrieved Clicks are the same as the original Clicks
	assert retrieved_clicks == clicks

