from flask import Flask, request, redirect
from database import users, urls, clicks
from models import User, URL, Click
from utils import generate_short_url, validate_url, get_current_time


app = Flask(__name__)


@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	user_id = data.get('user_id')
	expiration = data.get('expiration')

	if not validate_url(original_url):
		return {'error': 'Invalid URL'}, 400

	shortened_url = generate_short_url()
	url = URL(id=shortened_url, original_url=original_url, shortened_url=shortened_url, user_id=user_id, expiration=expiration, clicks=0, click_data=[])
	urls[shortened_url] = url

	return {'shortened_url': shortened_url}, 200


@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)

	if not url:
		return {'error': 'URL not found'}, 404

	if url.expiration and url.expiration < get_current_time():
		return {'error': 'URL expired'}, 410

	url.clicks += 1
	click = Click(id=short_url, url_id=url.id, timestamp=get_current_time(), location=request.remote_addr)
	clicks[click.id] = click
	url.click_data.append(click)

	return redirect(url.original_url, code=302)
