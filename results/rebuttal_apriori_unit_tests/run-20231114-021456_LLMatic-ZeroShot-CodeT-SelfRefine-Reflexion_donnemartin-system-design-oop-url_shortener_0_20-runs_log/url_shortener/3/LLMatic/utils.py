import random
import string
from urllib.parse import urlparse
from datetime import datetime
from models import URL

# Mock database
DATABASE = {}

# Function to validate URL
def validate_url(url):
	try:
		parsed_url = urlparse(url)
		return all([parsed_url.scheme, parsed_url.netloc])
	except ValueError:
		return False

# Function to generate a unique shortened URL
def shorten_url(original_url):
	if not validate_url(original_url):
		return 'Invalid URL'
	shortened_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	while shortened_url in DATABASE:
		shortened_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	DATABASE[shortened_url] = URL(original_url, shortened_url)
	return shortened_url

# Function to get the original URL from the shortened URL
def get_original_url(shortened_url):
	return DATABASE.get(shortened_url).original_url if DATABASE.get(shortened_url) else None

# Function to update analytics data
def update_analytics(shortened_url, geolocation):
	url = DATABASE.get(shortened_url)
	if url:
		url.clicks += 1
		url.click_dates.append(datetime.now().isoformat())
		url.click_geolocations.append(geolocation)

# Function to retrieve analytics data
def get_analytics(shortened_url):
	url = DATABASE.get(shortened_url)
	if url:
		return {'clicks': url.clicks, 'click_dates': url.click_dates, 'click_geolocations': url.click_geolocations}
	else:
		return None
