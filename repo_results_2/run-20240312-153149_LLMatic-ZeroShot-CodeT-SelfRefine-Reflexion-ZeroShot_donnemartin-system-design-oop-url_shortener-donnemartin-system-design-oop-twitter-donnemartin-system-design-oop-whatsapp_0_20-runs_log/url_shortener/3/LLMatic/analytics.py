import datetime
import requests

# Mock database for analytics
analytics_database = {}


def track_click(short_url, ip_address):
	"""Track a click for a shortened URL.

	:param short_url: Shortened URL
	:param ip_address: IP address of the clicker
	"""
	if short_url not in analytics_database:
		analytics_database[short_url] = []

	# Get geographical location from IP address
	response = requests.get(f'http://ip-api.com/json/{ip_address}')
	location = response.json().get('country', 'Unknown')

	# Track click
	analytics_database[short_url].append({
		'time': datetime.datetime.now(),
		'location': location
	})


def get_statistics(short_url):
	"""Get statistics for a shortened URL.

	:param short_url: Shortened URL
	:return: List of clicks with time and location
	"""
	return analytics_database.get(short_url, [])
