from flask import Flask, request, jsonify, redirect
from shortener import Shortener
from user import User, users
from admin import Admin

app = Flask(__name__)
shortener = Shortener()

@app.route('/', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	custom_short_link = data.get('custom_short_link')
	expiration_date = data.get('expiration_date')
	if not shortener.validate_url(original_url):
		return jsonify({'error': 'Invalid URL'}), 400
	short_url = shortener.shorten_url(original_url, custom_short_link, expiration_date)
	return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url_data = shortener.url_dict.get(short_url)
	if url_data and not shortener.is_expired(short_url):
		for user in users.values():
			if short_url in user.urls:
				user.analytics.record_click(short_url, request.remote_addr)
				break
		return redirect(url_data['url'])
	elif url_data and shortener.is_expired(short_url):
		return 'URL has expired', 410
	else:
		return 'URL not found', 404

@app.route('/user', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = User(username, password)
	user.create_account()
	return jsonify({'message': 'Account created successfully'})

@app.route('/user/<username>/urls', methods=['GET'])
def view_urls(username):
	user = users.get(username)
	if user:
		return jsonify(user.view_urls())
	else:
		return 'User not found', 404

@app.route('/user/<username>/urls', methods=['POST'])
def add_url(username):
	data = request.get_json()
	original_url = data.get('original_url')
	shortened_url = data.get('shortened_url')
	user = users.get(username)
	if user:
		user.add_url(original_url, shortened_url)
		return jsonify({'message': 'URL added successfully'})
	else:
		return 'User not found', 404

@app.route('/user/<username>/urls/<short_url>', methods=['PUT'])
def edit_url(username, short_url):
	data = request.get_json()
	new_url = data.get('new_url')
	user = users.get(username)
	if user:
		user.edit_url(short_url, new_url)
		return jsonify({'message': 'URL edited successfully'})
	else:
		return 'User not found', 404

@app.route('/user/<username>/urls/<short_url>', methods=['DELETE'])
def delete_url(username, short_url):
	user = users.get(username)
	if user:
		user.delete_url(short_url)
		return jsonify({'message': 'URL deleted successfully'})
	else:
		return 'User not found', 404

@app.route('/user/<username>/analytics/<short_url>', methods=['GET'])
def view_analytics(username, short_url):
	user = users.get(username)
	if user:
		return jsonify(user.view_analytics(short_url))
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
