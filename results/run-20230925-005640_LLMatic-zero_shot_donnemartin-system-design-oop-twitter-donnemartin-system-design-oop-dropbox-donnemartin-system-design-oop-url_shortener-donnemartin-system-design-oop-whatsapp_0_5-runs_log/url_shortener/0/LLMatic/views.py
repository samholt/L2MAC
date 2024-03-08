from flask import Flask, request, jsonify, redirect
from services import create_user, edit_user, delete_user, generate_short_url, get_original_url, record_click, get_analytics, get_all_urls, get_all_users, delete_url, get_system_performance

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user_endpoint():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = create_user(username, password)
	if user == 'User created successfully':
		return jsonify({'message': 'User created'}), 200
	else:
		return jsonify({'error': 'User already exists'}), 400

@app.route('/edit_user', methods=['POST'])
def edit_user_endpoint():
	data = request.get_json()
	username = data.get('username')
	new_password = data.get('new_password')
	user = edit_user(username, new_password)
	if user == 'User updated successfully':
		return jsonify({'message': 'User edited'}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/delete_user', methods=['POST'])
def delete_user_endpoint():
	data = request.get_json()
	username = data.get('username')
	deleted = delete_user(username)
	if deleted == 'User deleted successfully':
		return jsonify({'message': 'User deleted'}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	user = data.get('user')
	custom_short_link = data.get('custom_short_link')
	shortened_url = generate_short_url(url, user, custom_short_link)
	if shortened_url:
		return jsonify({'shortened_url': shortened_url}), 200
	else:
		return jsonify({'error': 'Invalid URL'}), 400

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url:
		record_click(short_url, request.remote_addr)
		return redirect(original_url, code=302)
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/analytics/<short_url>', methods=['GET'])
def view_analytics(short_url):
	analytics = get_analytics(short_url)
	if analytics:
		return jsonify(analytics), 200
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/admin/urls', methods=['GET'])
def view_all_urls():
	urls = get_all_urls()
	return jsonify(urls), 200

@app.route('/admin/users', methods=['GET'])
def view_all_users():
	users = get_all_users()
	return jsonify(users), 200

@app.route('/admin/delete_url', methods=['POST'])
def delete_url_endpoint():
	data = request.get_json()
	short_url = data.get('short_url')
	deleted = delete_url(short_url)
	if deleted:
		return jsonify({'message': 'URL deleted'}), 200
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/admin/performance', methods=['GET'])
def view_system_performance():
	performance = get_system_performance()
	return jsonify(performance), 200

