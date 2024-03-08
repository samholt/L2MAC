from flask import Flask, request, jsonify, redirect
from models import UrlData
from auth import users
import datetime

app = Flask(__name__)

url_data = {}

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	shortened_url = data.get('shortened_url', str(len(url_data)))
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')
	url_data[shortened_url] = UrlData(id=len(url_data), original_url=original_url, shortened_url=shortened_url, user_id=user_id, clicks=0, expiration_date=expiration_date, geographical_location=None)
	return jsonify({'message': 'URL shortened successfully', 'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_url(shortened_url):
	url = url_data.get(shortened_url)
	if not url or (url.expiration_date and datetime.datetime.now() > datetime.datetime.strptime(url.expiration_date, '%Y-%m-%d')):
		return jsonify({'message': 'URL not found or expired'}), 404
	url.clicks += 1
	return redirect(url.original_url, code=302)
