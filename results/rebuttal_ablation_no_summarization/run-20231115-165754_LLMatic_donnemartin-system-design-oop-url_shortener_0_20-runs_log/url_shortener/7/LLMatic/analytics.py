import datetime
import requests

# Mock database for analytics
ANALYTICS_DB = {}


def track_click(short_url, ip_address):
	if short_url not in ANALYTICS_DB:
		ANALYTICS_DB[short_url] = []
	
	# Get geographical location from IP address
	try:
		response = requests.get(f'http://ip-api.com/json/{ip_address}')
		geo_location = response.json().get('country', 'Unknown')
	except Exception:
		geo_location = 'Unknown'
	
	# Record click data
	click_data = {
		'time': datetime.datetime.now(),
		'location': geo_location
	}
	ANALYTICS_DB[short_url].append(click_data)


def get_analytics(short_url):
	return ANALYTICS_DB.get(short_url, [])
