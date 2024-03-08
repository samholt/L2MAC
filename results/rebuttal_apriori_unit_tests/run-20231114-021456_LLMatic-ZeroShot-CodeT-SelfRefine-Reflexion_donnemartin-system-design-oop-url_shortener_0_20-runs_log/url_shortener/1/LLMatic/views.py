from flask import Blueprint, request, redirect, jsonify
import utils

# Mock database
url_db = utils.url_db
click_db = utils.click_db

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return 'Hello, World!'

@views.route('/shorten', methods=['POST'])
def shorten():
	url = request.json.get('url')
	if not utils.validate_url(url):
		return {'error': 'Invalid URL'}, 400
	short_url = utils.shorten_url(url)
	# Store the mapping between the shortened URL and the original URL in the mock database
	url_db[short_url] = url
	return {'short_url': short_url}, 200

@views.route('/redirect/<short_url>')
def redirect_url(short_url):
	# Retrieve the original URL from the mock database
	original_url = url_db.get(short_url)
	if original_url is None:
		return {'error': 'URL not found'}, 404
	# Record the click
	click = utils.record_click(short_url, original_url, 'Unknown')
	# Store the click in the mock database using the short URL as the key
	if short_url in click_db:
		click_db[short_url].append(click)
	else:
		click_db[short_url] = [click]
	# Redirect to the original URL
	return redirect(original_url, code=302)

@views.route('/analytics/<short_url>')
def analytics(short_url):
	# Retrieve the clicks from the mock database
	clicks = click_db.get(short_url)
	if clicks is None:
		return jsonify({'error': 'No clicks found'}), 404
	# Return the click data
	click_data = [{'click_time': click.click_time.isoformat(), 'location': click.location} for click in clicks]
	return jsonify({'clicks': click_data}), 200
