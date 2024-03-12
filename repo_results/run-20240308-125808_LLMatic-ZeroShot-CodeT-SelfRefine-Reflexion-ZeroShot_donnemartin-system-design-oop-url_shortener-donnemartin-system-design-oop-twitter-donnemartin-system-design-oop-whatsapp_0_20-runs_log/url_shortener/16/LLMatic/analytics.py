import datetime

# Mock database
url_data = {}


def get_url_stats(short_url):
	"""Get statistics for a short URL.

	Args:
		short_url (str): The short URL.

	Returns:
		dict: The URL statistics.
	"""
	url_info = url_data.get(short_url, {'clicks': []})
	clicks = len(url_info['clicks'])
	click_info = [{'time': click['time'], 'location': click['location']} for click in url_info['clicks']]

	return {'clicks': clicks, 'click_info': click_info}


def record_click(short_url, location):
	"""Record a click for a short URL.

	Args:
		short_url (str): The short URL.
		location (str): The location of the click.
	"""
	if short_url not in url_data:
		url_data[short_url] = {'clicks': []}

	url_data[short_url]['clicks'].append({'time': datetime.datetime.now(), 'location': location})
