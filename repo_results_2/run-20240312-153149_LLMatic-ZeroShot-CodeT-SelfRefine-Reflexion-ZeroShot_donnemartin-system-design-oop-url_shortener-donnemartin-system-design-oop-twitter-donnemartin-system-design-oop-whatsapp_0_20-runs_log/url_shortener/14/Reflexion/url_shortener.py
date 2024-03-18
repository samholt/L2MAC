from flask import Flask, request, jsonify, redirect
from database import get_url, add_url, delete_url
from models import URL
import uuid
import datetime


app = Flask(__name__)


@app.route('/shorten', methods=['POST'])
def shorten():
	data = request.get_json()
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')
	if not original_url:
		return jsonify({'message': 'Missing original URL'}), 400
	url = URL(id=str(uuid.uuid4()), original_url=original_url, short_url=short_url, user_id=user_id, clicks=0, click_details=[], expiration_date=expiration_date)
	add_url(url)
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 200


@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = get_url(short_url)
	if not url:
		return jsonify({'message': 'URL not found'}), 404
	if url.expiration_date and datetime.datetime.now() > datetime.datetime.strptime(url.expiration_date, '%Y-%m-%d %H:%M:%S'):
		delete_url(short_url)
		return jsonify({'message': 'URL expired'}), 410
	url.clicks += 1
	url.click_details.append({'click_time': str(datetime.datetime.now()), 'click_location': request.remote_addr})
	return redirect(url.original_url, code=302)

