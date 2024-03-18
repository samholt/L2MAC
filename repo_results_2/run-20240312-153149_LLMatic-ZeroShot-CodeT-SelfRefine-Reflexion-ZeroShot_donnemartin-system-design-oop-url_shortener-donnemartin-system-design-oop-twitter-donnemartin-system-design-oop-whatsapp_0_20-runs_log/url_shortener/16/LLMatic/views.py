from flask import Flask, request, jsonify, redirect
from services import generate_short_link, get_original_url, record_click, get_clicks, create_user, get_user, edit_user, delete_user, get_all_urls, delete_url, get_all_users

app = Flask(__name__)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_short_link = request.json.get('custom_short_link')
	shortened_url = generate_short_link(url, custom_short_link)
	return jsonify({'shortened_url': shortened_url.shortened_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url is None:
		return jsonify({'error': 'URL not found'}), 404
	record_click(original_url, request.remote_addr)
	return redirect(original_url)

@app.route('/stats/<short_url>', methods=['GET'])
def get_stats(short_url):
	original_url = get_original_url(short_url)
	if original_url is None:
		return jsonify({'error': 'URL not found'}), 404
	clicks = get_clicks(original_url)
	return jsonify({'clicks': [click.__dict__ for click in clicks]})

@app.route('/create_user', methods=['POST'])
def create_user_route():
	username = request.json.get('username')
	password = request.json.get('password')
	user = create_user(username, password)
	return jsonify({'user': user.__dict__})

@app.route('/user/<username>', methods=['GET'])
def get_user_route(username):
	user = get_user(username)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify({'user': user.__dict__})

@app.route('/user/<username>', methods=['PUT'])
def edit_user_route(username):
	new_password = request.json.get('new_password')
	user = edit_user(username, new_password)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify({'user': user.__dict__})

@app.route('/user/<username>', methods=['DELETE'])
def delete_user_route(username):
	message = delete_user(username)
	return jsonify({'message': message})

@app.route('/admin/urls', methods=['GET'])
def get_all_urls_route():
	urls = get_all_urls()
	return jsonify({'urls': [url.__dict__ for url in urls]})

@app.route('/admin/url/<short_url>', methods=['DELETE'])
def delete_url_route(short_url):
	message = delete_url(short_url)
	return jsonify({'message': message})

@app.route('/admin/users', methods=['GET'])
def get_all_users_route():
	users = get_all_users()
	return jsonify({'users': [user.__dict__ for user in users]})
