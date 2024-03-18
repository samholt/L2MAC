from flask import Flask, request, redirect
from database import users, urls, URL, User

app = Flask(__name__)


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	user_id = data['user_id']
	expiration_date = data['expiration_date']
	url = URL(original_url, short_url, 0, user_id, expiration_date)
	urls[short_url] = url
	if user_id in users:
		users[user_id].urls.append(url)
	else:
		users[user_id] = User(user_id, [url])
	return {'short_url': short_url}, 201


@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url in urls and urls[short_url].expiration_date > datetime.now():
		urls[short_url].clicks += 1
		return redirect(urls[short_url].original_url)
	else:
		return {'error': 'URL not found or expired'}, 404


@app.route('/user_urls/<user_id>', methods=['GET'])
def get_user_urls(user_id):
	if user_id in users:
		return {'urls': [url.short_url for url in users[user_id].urls]}, 200
	else:
		return {'error': 'User not found'}, 404


@app.route('/all_data', methods=['GET'])
def get_all_data():
	return {'users': {user_id: [url.short_url for url in user.urls] for user_id, user in users.items()},'urls': {short_url: url.original_url for short_url, url in urls.items()}}, 200
