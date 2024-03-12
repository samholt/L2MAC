from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	click_data: list
	expiration: datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	custom = data.get('custom')
	expiration = datetime.strptime(data.get('expiration'), '%Y-%m-%dT%H:%M:%SZ')

	# Generate a random string for the shortened URL
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom:
		shortened_url = custom

	# Create a new URL object and store it in the database
	new_url = URL(original_url, shortened_url, user, 0, [], expiration)
	urls[shortened_url] = new_url

	# If the user exists, add the URL to their list of URLs
	if user in users:
		users[user].urls.append(new_url)

	return jsonify({'shortened_url': shortened_url})

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	# If the URL exists in the database, redirect to the original URL
	if shortened_url in urls:
		url = urls[shortened_url]
		if datetime.now() > url.expiration:
			return jsonify({'error': 'URL has expired'}), 410
		url.clicks += 1
		url.click_data.append({'time': datetime.now(), 'location': request.remote_addr})
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# If the user exists, return their analytics data
	if user in users:
		user_urls = users[user].urls
		analytics_data = [{'original': url.original, 'shortened': url.shortened, 'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls]
		return jsonify({'analytics': analytics_data})
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# If the username is not already taken, create a new user
	if username not in users:
		new_user = User(username, password, [])
		users[username] = new_user
		return jsonify({'message': 'User registered successfully'})
	else:
		return jsonify({'error': 'Username already taken'}), 400

if __name__ == '__main__':
	app.run(debug=True)
