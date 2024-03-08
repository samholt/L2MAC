import datetime
import requests

# Mock database for analytics data
analytics_db = {}


def track_click(short_url, ip_address):
	"""Track a click for a shortened URL.

	:param short_url: Shortened URL
	:param ip_address: IP address of the clicker
	"""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	# Get geographical location from IP address
	response = requests.get(f'http://ip-api.com/json/{ip_address}')
	location = response.json().get('country', 'Unknown')

	# Track click
	click_data = {
		'time': datetime.datetime.now(),
		'location': location
	}
	analytics_db[short_url].append(click_data)


def get_analytics(short_url):
	"""Retrieve analytics data for a shortened URL.

	:param short_url: Shortened URL
	:return: List of click data
	"""
	return analytics_db.get(short_url, [])
